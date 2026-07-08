# dbo.build_message_$sp

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.build_message_$sp"]
    process_error_log(["process_error_log"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| process_error_log |

## Stored Procedure Code

```sql
create proc dbo.build_message_$sp 
@entry_id	numeric(18,0),
@message_text	nvarchar(1024) OUTPUT   --- never null when called by common_error_handling

AS

/* 

  Proc Name : build_message_$sp
       Desc : To build message with embedded memo fields from the process_error_log.
       Called by common_error_handling_$sp. 

  HISTORY
  Date     Name		Def# Desc
  Nov05,13 Paul       145958 print error message if an error occurs inside this proc, use try .. catch
  Sep06,06 Daphna      75320 MSSQL2005 prevent null string
  May03,02 Ian       1-CD0IX Add R3 Error Handling
  APR29,02 Daphna    1-COKT3 correct assignment of @memo3 from process_error_log
  Oct16,01 Winnie       8748 Author

*/

DECLARE @errmsg		nvarchar(2000),
        @errno		int,
	@memo1		nvarchar(255),
	@memo2		nvarchar(255),
	@memo3		nvarchar(255),
	@memo_date	smalldatetime,
	@memo_date2	smalldatetime,
	@memo_date3	smalldatetime,
	@position	int,
	@rows		int,
	@seg		nvarchar(3),
	@length 	int,
	-- error handling
        @process_name           nvarchar(100),
        @process_no             smallint,
        @operation_name         nvarchar(100),
        @object_name            nvarchar(255),
        @message_id             int,
        @log_flag               tinyint

SELECT  @process_name = 'build_message_$sp',
        @message_id   = 201068,
        @log_flag     = 0,
        @process_no   = 36;

BEGIN TRY

SELECT @errmsg         = 'Unable to select from process_error_log',
         @object_name    = 'process_error_log',
         @operation_name = 'SELECT';

SELECT @memo1 = ISNULL(memo1,' '),
       @memo2 = ISNULL(memo2,' '), 	
       @memo3 = ISNULL(memo3,' '),  -- DEF 1-COKT3
       @memo_date =  ISNULL(memo_date,'01-JAN-1970'),	
       @memo_date2 = ISNULL(memo_date2,'01-JAN-1970'),		
       @memo_date3 = ISNULL(memo_date3,'01-JAN-1970')
  FROM process_error_log
 WHERE entry_id = @entry_id;	

SELECT @rows = @@rowcount
IF @rows = 0 -- safety code
  SELECT @message_text = 'Entry not found in process_error_log: ' + @message_text

SELECT @errmsg         = 'Unable to read message_text variable (loop)',
         @object_name    = '@message_text';

WHILE 1 = 1
  BEGIN

    SELECT @length = LEN(@message_text),
           @position = CHARINDEX('|', @message_text);

    IF @position = 0 
      BREAK;
    
    IF SUBSTRING (@message_text, @position, 2) <> '|d'
      BEGIN 
        SELECT @seg = SUBSTRING (@message_text, @position, 2)
        IF @seg = '|1' 
          SELECT @message_text = SUBSTRING (@message_text, 1, @position -1) + @memo1 + 
                 		 SUBSTRING (@message_text, @position + 2, @length - @position -1)
          ELSE IF @seg = '|2'
            SELECT @message_text = SUBSTRING (@message_text, 1, @position -1) + @memo2 + 
                		 SUBSTRING (@message_text, @position + 2, @length - @position -1 )

	  ELSE IF @seg = '|3'
            SELECT @message_text = SUBSTRING (@message_text, 1, @position -1) + @memo3 + 
                 		 SUBSTRING (@message_text, @position + 2, @length - @position -1)                 		 
      END;

      ELSE
        BEGIN
          SELECT @seg = SUBSTRING (@message_text, @position, 3)
          IF @seg = '|d1' 
            SELECT @message_text = SUBSTRING (@message_text, 1, @position -1) + CONVERT(VARCHAR, @memo_date,101) + 
                 		 SUBSTRING (@message_text, @position + 3, @length - @position -2 )
          ELSE IF @seg = '|d2'
            SELECT @message_text = SUBSTRING (@message_text, 1, @position -1) +CONVERT(VARCHAR, @memo_date2,101) + 
                 		 SUBSTRING (@message_text, @position + 3, @length - @position -2 )

	  ELSE IF @seg = '|d3'
            SELECT @message_text = SUBSTRING (@message_text, 1, @position -1) + CONVERT(VARCHAR, @memo_date3,101) + 
                 		 SUBSTRING (@message_text, @position + 3, @length - @position -2)                 		 	      

         END;

  END; -- While


RETURN;

END TRY

BEGIN CATCH;

   /* Common error handler. Customized for this proc to print error message as a warning
       because this proc is called from common_error_handling_$sp */

   SELECT @errno = ERROR_NUMBER(),
		@errmsg = ':LOG EXECWARN:build_message_$sp:' + COALESCE(@errmsg, ' ') + ERROR_MESSAGE();

   PRINT @errmsg;

   RETURN;

END CATCH;
```

