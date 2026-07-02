# dbo.get_document_numbers_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.get_document_numbers_$sp"]
    dbo_gen_strings_in_range__sp(["dbo.gen_strings_in_range_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.gen_strings_in_range_$sp |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[get_document_numbers_$sp]
	@mask				NVARCHAR(20),
	@min_no				NVARCHAR(20),
	@max_no				NVARCHAR(20),
	@last_saved_doc_no	NVARCHAR(20),
	@doc_table			NVARCHAR(24),
	@count_to_gen		INT,
	@rec_flag			BIT OUTPUT

AS

/*
	Version		: 1.00
	Created		: Jun 2011
	Description	: Intended to be called by the Generate Transfers from Distribution process.
				  Call gen_strings_in_range_$sp to generate the next 'x' document numbers within a
				  given range. Return to this stored procedure to filter out the numbers that can be assigned to
				  the new transfer documents. 
				  Additional calls to generate more document numbers may be required if:
						- A suggested document number already exists in the main table (ie. transfer) and cannot be reused.
						- The pass from mid range to the max number failed to generate the requested number of documents. 
*/

BEGIN
	DECLARE @count				INT,
			@count_validated	INT, 
			@last_gen_no		NVARCHAR(20),
			@restarted_at_min	BIT,
			@insert_min_no		BIT,
			@reached_max_no		BIT,
			@can_continue		BIT,
            @err_no				INT,
            @err_msg			NVARCHAR(2000)

	
	-- If last_saved_doc_no is not defined or the last_saved_doc_no exceeds the max, restart at the min.
	IF ((@last_saved_doc_no = NULL) OR (@last_saved_doc_no >= @max_no))
		BEGIN
			SET @insert_min_no = 1
			SET @last_saved_doc_no = @min_no
			SET @restarted_at_min = 1
		END
	ELSE
		BEGIN
			SET @insert_min_no = 0
			SET @restarted_at_min = 0
		END
		
		
	-- Loop while there are document numbers to generate and entire range has not been cycled thru.
	SET @last_gen_no = @last_saved_doc_no
	SET @reached_max_no = 0
	SET @count = @count_to_gen
	SET @can_continue = 1
	WHILE ((@count > 0) AND (@can_continue = 1))
		BEGIN
		
			-- Call SP to gen x document numbers
			BEGIN TRY
				EXEC gen_strings_in_range_$sp @mask, @last_gen_no, @min_no, @max_no, @count, @insert_min_no, @reached_max_no OUTPUT
			END TRY
			
			BEGIN CATCH
				SET @err_no = ERROR_NUMBER()
				SET @err_msg = N'get_document_numbers_$sp. Failed calling stored procedure. ' + ERROR_MESSAGE()
				GOTO ErrHandler
			END CATCH
			
		
			-- Merge what we can
			BEGIN TRY
				EXEC (
						N' INSERT INTO #_validated_doc_table (document_no) ' +
						N' SELECT document_no ' + 
						N' FROM #_suggested_doc_table ' +
						N' WHERE document_no NOT IN (SELECT document_no FROM ' + @doc_table + N' WHERE document_no BETWEEN ''' + @last_gen_no + N''' AND ''' + @max_no + N''')' +
								N' AND document_no <= ''' + @max_no + N''''
 					)
			END TRY
			
			BEGIN CATCH
				SET @err_no = ERROR_NUMBER()
				SET @err_msg = N'get_document_numbers_$sp. INSERT INTO #_validated_doc_table failed. ' + ERROR_MESSAGE()
				GOTO ErrHandler
			END CATCH
			

			-- Check if need to generate more document numbers
			BEGIN TRY
				SET @count_validated = (SELECT COUNT(*) FROM #_validated_doc_table)
				SET @count = @count_to_gen - @count_validated
			END TRY
			
			BEGIN CATCH
				SET @err_no = ERROR_NUMBER()
				SET @err_msg = N'get_document_numbers_$sp. Failed to set count values. ' + ERROR_MESSAGE()
				GOTO ErrHandler
			END CATCH
			
			-- If more document numbers are required, check if the entire range has been cycled.
			IF (@count > 0)
				BEGIN
					IF (@reached_max_no = 1)
						BEGIN
							IF (@restarted_at_min = 0)
								BEGIN
									-- Max has been reached but we started in the middle of the range.
									-- New range will be from @min_no to @last_saved_doc_no
									-- Flag to insert min_no
									SET @last_gen_no = @min_no
									SET @max_no = @last_saved_doc_no
									SET @restarted_at_min = 1
									SET @insert_min_no = 1
									SET @reached_max_no = 0
								END
							ELSE
								BEGIN
									-- Max has been reached and entire range from min to max has been cycled.
									SET @can_continue = 0
								END
						END
					ELSE
						BEGIN
							-- Max not not reached yet. Can continue till max.
							SET @last_gen_no = (SELECT MAX(document_no) FROM #_suggested_doc_table)
							SET @insert_min_no = 0
						END
				END
		END

		IF (@count > 0)
			BEGIN
				-- Failed to generate the requested doc numbers
				SET @err_no = 100
				SET @err_msg = N'get_document_numbers_$sp. Failed to generate requested number of documents. Requested: '+ CONVERT(NVARCHAR(20), @count_to_gen) + N'   Missing: ' + CONVERT(NVARCHAR(20), @count)
				GOTO ErrHandler
			END
		ELSE
			BEGIN
				-- Generated the requested doc number.
				-- Update the recycle flag
				IF ((@rec_flag = 0) AND (@restarted_at_min = 1))
					SET @rec_flag = 1
					
			END

   RETURN
   
   
   ErrHandler:
	  SET @err_no = ISNULL(@err_no, 0)
	  
	  IF ((@err_msg = NULL) OR (LEN(@err_msg) = 0))
		SET @err_msg = N'Failed in get_document_numbers_$sp.'
		
      RAISERROR (N'Message: %s   err_no: %d', 16, 1, @err_msg, @err_no)
	
END
```

