# dbo.get_next_doc_no_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.get_next_doc_no_$sp"]
    dbo_add_to_masked_string__sp(["dbo.add_to_masked_string_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.add_to_masked_string_$sp |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[get_next_doc_no_$sp]
	@mask        NVARCHAR(20),
	@min_no      NVARCHAR(20),
	@max_no      NVARCHAR(20),
	@last_gen_no NVARCHAR(20),
	@doc_table   NVARCHAR(24),
	@doc_no_col  NVARCHAR(27),
	@rec_flag    BIT OUTPUT,
	@new_no      NVARCHAR(20) OUTPUT
AS
/*
Proc name: 	add_to_masked_string_$sp
Description: Get the next available document number for a given type of IM document.

HISTORY: 
Date            Name       Desc
July 28, 2010   Yan Ding   Defect 109993 failed to generate store xfer # with alphanumeric mask 
*/
DECLARE
	@msg    NVARCHAR(255),
	@result NVARCHAR(20),
	@found  bit

SET @found = 0

IF @last_gen_no IS NULL
	SET @last_gen_no = @max_no

IF @last_gen_no = @max_no
	SET @rec_flag = 1

IF @rec_flag = 1
	BEGIN
   	IF @last_gen_no IS NULL OR @last_gen_no = N'' OR @last_gen_no = @max_no
			SET @new_no = @min_no
		ELSE
			BEGIN
				EXEC add_to_masked_string_$sp @mask, @last_gen_no, 1, @new_no OUTPUT
				IF @new_no IS NULL
					GOTO ErrHandler
			END
		
		EXEC(
			N'DECLARE no_list CURSOR FOR ' +
			N'SELECT ' + @doc_no_col + N' ' +
			N'FROM   ' + @doc_table + N' WITH (NOLOCK) ' +
			N'WHERE  ' + @doc_no_col + N' BETWEEN ''' + @new_no + N''' AND ''' + @max_no + N''' ' +
			N'AND    LEN(' + @doc_no_col + N') = LEN(''' + @mask + N''') ' +
			N'ORDER  BY ' + @doc_no_col
			 )
		

		OPEN no_list

		FETCH no_list INTO @result
		
		WHILE @new_no BETWEEN @min_no AND @max_no AND @found = 0
			BEGIN
				
				IF @@FETCH_STATUS <> 0
					BEGIN
						SET @found = 1
						BREAK
					END
				
				IF @result <> @new_no
					BEGIN
						SET @found = 1
						BREAK
					END
				ELSE
					BEGIN
						EXEC add_to_masked_string_$sp @mask, @new_no, 1, @new_no OUTPUT
						IF @new_no IS NULL
							GOTO ErrHandler

						FETCH no_list INTO @result
					END
			END
		
		CLOSE no_list
		DEALLOCATE no_list
		
		IF @found = 1
			RETURN
		
		SET @new_no = @min_no
		
		EXEC(
			N'DECLARE no_list CURSOR FOR ' +
			N'SELECT ' + @doc_no_col + N' ' +
			N'FROM   ' + @doc_table + N' WITH (NOLOCK) ' +
			N'WHERE  ' + @doc_no_col + N' BETWEEN ''' + @min_no + N''' AND ''' + @last_gen_no + N''' ' +
			N'AND    LEN(' + @doc_no_col + N') = LEN(''' + @mask + N''') ' +
			N'ORDER  BY ' + @doc_no_col
			 )

		OPEN no_list

		FETCH no_list INTO @result
		
		WHILE @new_no BETWEEN @min_no AND @last_gen_no AND @found = 0
			BEGIN
				
				IF @@FETCH_STATUS <> 0
					BEGIN
						SET @found = 1
						BREAK
					END
				
				IF @result <> @new_no
					BEGIN
						SET @found = 1
						BREAK
					END
				ELSE
					BEGIN
						EXEC add_to_masked_string_$sp @mask, @new_no, 1, @new_no OUTPUT
						IF @new_no IS NULL
							GOTO ErrHandler

						FETCH no_list INTO @result
					END
			END
		
		CLOSE no_list
		DEALLOCATE no_list

	END
ELSE
	BEGIN
		IF @last_gen_no IS NULL OR @last_gen_no = N''
			BEGIN
				SET @new_no = @min_no
				SET @found = 1
			END
		ELSE
			BEGIN
				EXEC add_to_masked_string_$sp @mask, @last_gen_no, 1, @new_no OUTPUT
				IF @new_no IS NULL
					GOTO ErrHandler
				SET @found = 1
			END

	END

IF @found = 0
	GOTO ErrHandler

RETURN

ErrHandler:

	BEGIN
		SET @new_no = NULL
		SET @msg = N'Failed to find the next available document number from the range ' + @min_no + N' - ' + @max_no
		
		RAISERROR (N'Message: %s ', 16, 1, @msg)
	END
	
	RETURN
```

