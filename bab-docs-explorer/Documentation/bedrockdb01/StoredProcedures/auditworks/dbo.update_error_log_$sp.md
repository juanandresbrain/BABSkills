# dbo.update_error_log_$sp

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.update_error_log_$sp"]
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| common_error_handling_$sp |

## Stored Procedure Code

```sql
create proc dbo.update_error_log_$sp 
@process_no	smallint,
@error_code	int,
@error_msg	nvarchar(255) = NULL,
@raiserror_flag   tinyint = 0,
@abort_flag	tinyint = 0

AS

/* Proc Name: update_error_log_$sp
   Desc: To log errors in batch processes to the process_error_log.
      This proc will eventually become obsolete. 

HISTORY
Date     Name           Def# Desc
Aug15,13 Paul         145958 call common_error_handling_$sp, use try .. catch
Sep15,04 IanK        DV-1146 Nullify verified_by_user_id as only called by powerbuilder
Jul09,04 ShuZ        DV-1071 Expand user name to nvarchar(50)
Apr20,04 Maryam      DV-1071 Modified to receive @process_id as input parameter
                             changed the data type of bit to smallint.
Apr04,01 Phu            7501 Use system function to retrieve user name
Feb12,01 David Ch       7311 Modify conditions to also insert if called from trigger
Oct10,00 Paul           6824 Add return to make raise error logic more explicit
Feb07,00 Maryam         5013 changed the size of @error_msg from 120 to 255 
Oct02,97 Paul                author
*/

DECLARE
  @errmsg                  nvarchar(1024),
  @errno                   int,
  @object_name		nvarchar(255),
  @process_name		nvarchar(100),
  @operation_name	nvarchar(100),
  @message_id		int,
  @verified		smallint;


  SELECT @process_name = 'update_error_log_$sp',
	@operation_name = 'SELECT',
	@object_name = 'error_code',
	@message_id = 201068,
	@errmsg = 'Unable to log message'; -- used for system error in this proc

BEGIN TRY

IF ( @error_code = 201572 OR @error_code = 1205 )
  SELECT @verified = 1;
ELSE
  SELECT @verified = 0;

IF @abort_flag = 1
  SELECT ':ABORT requested by application.';


business_error:   /* Business Rule handler. Custom for this proc since using passed in error message. */

	SELECT @errmsg = COALESCE(@error_msg, 'update_error_log_$sp:');

	EXEC common_error_handling_$sp @process_no, @error_code, @errmsg, 0, @message_id, 
	  @process_name, @object_name, @operation_name, 0, 1, 0, null, 0, null, null, 
	  null, null, null, null, 0, null, 0;

	RETURN;

END TRY

BEGIN CATCH;

     /* Common error handler. Custom for this proc since appending passed in error message. */

	SELECT @errno = ERROR_NUMBER(),
		@errmsg = 'update_error_log_$sp:' + COALESCE(@error_msg, ' ');

	EXEC common_error_handling_$sp @process_no, @errno, @errmsg, 0, @message_id, 
	  @process_name, @object_name, @operation_name, 0, 1, 0, null, 0, null, null, 
	  null, null, null, null, 0, null, 0;

	RETURN;
END CATCH;
```

