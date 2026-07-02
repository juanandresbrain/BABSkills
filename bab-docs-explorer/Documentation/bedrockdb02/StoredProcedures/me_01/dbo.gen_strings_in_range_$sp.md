# dbo.gen_strings_in_range_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.gen_strings_in_range_$sp"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[gen_strings_in_range_$sp] 
   @mask			NVARCHAR(20), 
   @last_gen_no		NVARCHAR(20),
   @min_no			NVARCHAR(20),
   @max_no			NVARCHAR(20),
   @count_to_gen	INT, 
   @insert_min_no	BIT,
   @reached_max_no	BIT	OUTPUT
AS

/*
	Version		: 1.00
	Created		: Jun 2011
	Description	: Intended to be called by the Generate Transfers from Distribution process.
				  Given a mask, a range and a starting point, determine the next 'x' document
				  numbers and insert into #_suggested_doc_table.
*/

BEGIN
   DECLARE @carry   INT,
           @i       INT,
           @digit   INT,
           @c       NCHAR(1),
           @m       NCHAR(1),
           @new_no  NVARCHAR(20),
           @can_continue BIT,
           @err_no  INT,
           @err_msg NVARCHAR(2000)
   
           
	--  Cleanup temp table  ------------------------------------------------------------------------------------------
	BEGIN TRY
		EXEC (N'DELETE FROM #_suggested_doc_table')
    END TRY
    
    BEGIN CATCH
		SET @err_no = ERROR_NUMBER()
		SET @err_msg = N'gen_next_strings_in_range_$sp. DELETE FROM #_suggested_doc_table: ' + ERROR_MESSAGE()
		GOTO ErrHandler
    END CATCH
   
   
    --  Check if need to start from the beginning  --------------------------------------------------------------------
    BEGIN TRY
		IF ((@insert_min_no = 1) OR (@last_gen_no = NULL) OR (@last_gen_no >= @max_no))
		BEGIN
			SET @count_to_gen = @count_to_gen - 1
			EXEC (N'INSERT INTO #_suggested_doc_table VALUES (''' + @min_no + N''')')
			SET @last_gen_no = @min_no
		END
	END TRY
	
	BEGIN CATCH
		SET @err_no = ERROR_NUMBER()
		SET @err_msg = N'gen_next_strings_in_range_$sp. INSERT INTO #_suggested_doc_table: ' + ERROR_MESSAGE()
		GOTO ErrHandler
	END CATCH
	
	
    --  Verify if @last_gen_no matches @mask  --------------------------------------------------------------------
	BEGIN
	   SET @i = LEN(@last_gen_no)
	   
	   -- Compare length of @mask and @last_gen_no
	   IF (LEN(@mask) <> LEN(@last_gen_no))
		  BEGIN
			 SET @err_no = 1
			 SET @err_msg = N'gen_next_strings_in_range_$sp. Failed: ' + @last_gen_no + N' doesn''t match the mask ' + @mask
			 GOTO ErrHandler
		  END
	   
	   -- Verify @last_gen_no adheres to the @mask format
	   WHILE @i > 0
		  BEGIN
			 SET @c = SUBSTRING(@last_gen_no, @i, 1)
			 SET @m = SUBSTRING(@mask, @i, 1)
	         
			 IF UNICODE(N'A') <= UNICODE(@c) AND UNICODE(@c) <= UNICODE(N'Z')  -- alpha: A-Z
				BEGIN
				   IF @m <> N'A' AND @m <> N'C'
					  BEGIN
						 SET @err_no = 2
						 SET @err_msg = N'gen_next_strings_in_range_$sp. Failed: ' + @last_gen_no + N' doesn''t match the mask ' + @mask
						 GOTO ErrHandler
					  END
				END
			 ELSE IF UNICODE(N'0') <= UNICODE(@c) AND UNICODE(@c) <= UNICODE(N'9')  -- numeric: 0-9
				BEGIN
				   IF @m <> N'A' AND @m <> N'Z' AND @m <> N'9'
					  BEGIN
						 SET @err_no = 3
						 SET @err_msg = N'gen_next_strings_in_range_$sp. Failed: ' + @last_gen_no + N' doesn''t match the mask ' + @mask
						 GOTO ErrHandler
					  END
				END
			 ELSE
				BEGIN
				   SET @err_no = 4
				   SET @err_msg = N'gen_next_strings_in_range_$sp. Failed: ' + @last_gen_no + N' contains the non-alphanumeric character ' + @c
				   GOTO ErrHandler
				END
	         
			 SET @i = @i - 1
		  END
	END   
		
   --  Generate number of requested document numbers  --------------------------------------------------------------------
   SET @new_no = @last_gen_no
   SET @can_continue = 1
   WHILE ((@count_to_gen > 0) AND (@new_no < @max_no) AND (@can_continue = 1))
	  BEGIN		
		   SET @carry = 1
		   SET @i = LEN(@new_no)
		   
		   WHILE @i > 0 AND @carry > 0
			  BEGIN
				 SET @c = SUBSTRING(@new_no, @i, 1)
		         
				 IF UNICODE(N'A') <= UNICODE(@c) AND UNICODE(@c) <= UNICODE(N'Z')
					BEGIN
					   SET @digit = UNICODE(@c) - UNICODE(N'A') + @carry
					   SET @carry = @digit / 26
					   SET @digit = @digit % 26
					   SET @c = NCHAR(@digit + UNICODE(N'A'))
					END
				 ELSE IF UNICODE(N'0') <= UNICODE(@c) and UNICODE(@c) <= UNICODE(N'9')
					BEGIN
					   SET @digit = UNICODE(@c) - UNICODE(N'0') + @carry
					   SET @carry = @digit / 10
					   SET @digit = @digit % 10
					   SET @c = NCHAR(@digit + UNICODE(N'0'))
					END
		         
				 SET @new_no = STUFF(@new_no, @i, 1, @c)
		         
				 SET @i = @i - 1
			  END
		   
		   IF @carry > 0
			  BEGIN
				 -- Max reached. Time to exit. 
				 SET @can_continue = 0
			  END
		   ELSE
			  BEGIN
				IF (@new_no <= @max_no)
					BEGIN
						SET @count_to_gen = @count_to_gen - 1
						EXEC (N'INSERT INTO #_suggested_doc_table VALUES (''' + @new_no + N''')')
					END
				ELSE
					BEGIN
						-- Max reached. Time to exit. 
						SET @can_continue = 0
					END
						
			  END 
	  END
	  
	  IF ((@can_continue = 0) OR (@new_no >= @max_no))
		SET @reached_max_no = 1
		
   RETURN
   
   ErrHandler:
      SET @err_no = ISNULL(@err_no, 0)
      RAISERROR (N'Message: %s   err_no: %d', 16, 1, @err_msg, @err_no)
END
```

