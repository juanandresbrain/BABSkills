# dbo.get_pin_$sp

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.get_pin_$sp"]
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| common_error_handling_$sp |

## Stored Procedure Code

```sql
create proc dbo.get_pin_$sp  (@pin	nchar(4) OUTPUT
)

AS

/* 
Proc name:   get_pin_$sp
Description: Returns random number

HISTORY
Date     Name           Defect# Description
Jan04,11 Paul            105313 Use unicode datatypes
Oct29,10 Vicci           122164 Author
*/

DECLARE
  @errno 		int,
  @errmsg		nvarchar(255),
  @object_name          nvarchar(255),
  @process_no		smallint,
  @process_name         nvarchar(100),
  @operation_name	nvarchar(100),
  @message_id		int,
  @binpin 		binary(16)

SET CONCAT_NULL_YIELDS_NULL OFF

SELECT @process_no = 290, --WIPWIPWIP fix
       @process_name = 'get_pin_$sp',
       @message_id = 201068,
       @binpin = newid()

SELECT @pin = right('0000' + convert(nvarchar, convert(int, @binpin)), 4)

PRINT @pin

RETURN

error:   /* Common error handler */

          
  EXEC common_error_handling_$sp @process_no, @errno, @errmsg, 0, @message_id, 
       @process_name, @object_name, @operation_name, 1, 
       1,  0, null, 0, null, null, null, null, null, null, 0, null, null

  RETURN
```

