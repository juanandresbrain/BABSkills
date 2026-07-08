# dbo.filter_digit_$sp

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.filter_digit_$sp"]
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| common_error_handling_$sp |

## Stored Procedure Code

```sql
create proc dbo.filter_digit_$sp 

( @data_string		nvarchar(255),
  @return_data		nvarchar(255) OUTPUT 
)
AS

DECLARE
  @current_char 	nchar(1),
  @errmsg 		nvarchar(1024),
  @errno			int,
  @end_pos		smallint,
  @object_name		nvarchar(255),
  @process_name		nvarchar(100),
  @operation_name		nvarchar(100),
  @message_id		int,
  @start_pos		smallint


/* Proc Name: 

Desc:	To filter and return the string with digits only
HISTORY:
Date     Name          Def# Desc
Aug14,13 Paul        145958 call common_error_handling_$sp, use try .. catch
Jun22,01 Winnie        8100 Author

*/

SELECT @process_name = 'filter_digit_$sp',
	@operation_name = 'SELECT',
	@object_name = 'string',
	@message_id = 201068,
	@errmsg = 'Failed to parse @data_string';

BEGIN TRY

SELECT @start_pos = 1,
       @end_pos = LEN(@data_string);

WHILE @start_pos <= @end_pos
BEGIN
  SELECT @current_char = SUBSTRING(@data_string,@start_pos,1);
  IF @current_char >= '0' AND @current_char <= '9'
    SELECT @return_data = @return_data + @current_char;
   
  SELECT @start_pos = @start_pos + 1; 

END; -- While

RETURN;

END TRY

BEGIN CATCH;

     /* Common error handler */

	SELECT @errno = ERROR_NUMBER(),
		@errmsg = COALESCE(@errmsg, ' ') + ERROR_MESSAGE();

	EXEC common_error_handling_$sp 0, @errno, @errmsg, 0, @message_id, 
	  @process_name, @object_name, @operation_name, 0, 1, 0, null, 0, null, null, 
	  null, null, null, null, 0, null, 0;

	RETURN;

END CATCH;
```

