# dbo.always_fail_$sp

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.always_fail_$sp"]
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| common_error_handling_$sp |

## Stored Procedure Code

```sql
create proc dbo.always_fail_$sp 

 @queue_id			int,
 @object_id			int
 
AS

DECLARE @edit_complete          tinyint,
        -- error handling
        @process_name           nvarchar(100),
        @process_no             smallint,
        @operation_name         nvarchar(100),
        @object_name            nvarchar(255),
        @message_id             int,
        @log_flag               tinyint,
	@errno			int,
        @errmsg                 nvarchar(255)
        
SELECT  @process_name = 'always_fail_$sp',
        @message_id   = 201068,
        @log_flag     = 0,
        @process_no   = 36

/* 

  PROC NAME: always_fail_$sp
       DESC: Used by exports and corresponds to new application logic record in the metadata.
             Called from smartview for exports.

  HISTORY:
  Date     Name           Def# Desc
  Jan04,11 Paul         105313 Use unicode datatypes
  May03,02 Ian         1-CD0IX Add R3 Error Handling
  Jun11,01 Winnie         8096 add object_id as an input value for Smartlook 4.0
  Apr04,01 Winnie         7511 copied SmartView proc from Stuart.

*/

  SELECT @edit_complete = 0

  SELECT @errno = @@error
  IF @errno !=0
  BEGIN
    SELECT @errmsg         = 'Failed to select 0 into @edit_complete',
           @object_name    = '@edit_complete',
           @operation_name = 'SELECT'
    GOTO error
  END	

RETURN 0

error:
  
  EXEC common_error_handling_$sp @process_no, @errno, @errmsg, 0, @message_id,
                                 @process_name, @object_name, @operation_name, @log_flag
  RETURN
```

