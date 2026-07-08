# dbo.get_authorization_$sp

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.get_authorization_$sp"]
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| common_error_handling_$sp |

## Stored Procedure Code

```sql
create proc dbo.get_authorization_$sp  (@process_id 			binary(16) = NULL,
  @user_id			int = NULL,
  @edit_process_no		int = 1,
  @store_no 			int = 9999,
  @register_no			smallint = 10,
  @reference_no			nvarchar(80) = '4055011111111111',
  @card_type            	nchar(1) = '?',
  @expiry_date                  int = 1210,
  @orig_authorization_no        nvarchar(50) = NULL,
  @orig_swipe_indicator         tinyint = NULL,
  @orig_approval_message        nvarchar(255) = NULL,
  @current_amount		money = 7100,
  @balance_amount		money = 0,
  @current_authorization_no     nvarchar(50) = NULL OUTPUT,
  @current_approval_message     nvarchar(255) = NULL OUTPUT,
  @balance_authorization_no     nvarchar(50) = NULL OUTPUT,
  @balance_approval_message     nvarchar(255) = NULL OUTPUT,
  @errmsg 			nvarchar(255) = NULL OUTPUT
)

AS

/* 
Proc name:   get_authorization_$sp
Description: Returns authorization# for amount being shipped and authorization# for balance
	     Called by transl_auto_complete_order_$sp and reval_auto_complete_order_$sp

HISTORY
Date     Name       Defect# Description
Jan04,11 Paul        105313 Use unicode datatypes
Oct12,10 Vicci       122164 Author
*/

DECLARE
  @errno 		int,
  @object_name          nvarchar(255),
  @process_no		smallint,
  @process_name         nvarchar(100),
  @operation_name	nvarchar(100),
  @message_id		int,
  @company_no		int,
  @server_name		nvarchar(255),
  @port_no		int,
  @log_path		nvarchar(255),
  @errdesc		nvarchar(255),
  @expiry_date_string	nvarchar(8)

SET CONCAT_NULL_YIELDS_NULL OFF

SELECT @process_no = 290, --WIPWIPWIP fix
       @process_name = 'get_authorization_$sp',
       @message_id = 201068,
       @server_name = 'COMM1',
       @port_no = 20437,
       @company_no = 99,
       @log_path = '',
       @expiry_date_string = RIGHT('0' + CONVERT(nvarchar, @expiry_date), 4)

IF @user_id IS NULL 
  SELECT @user_id = -1
  
IF @process_id IS NULL
  SELECT @process_id = newid()

PRINT 'Connecting to port ' + convert(nvarchar, @port_no) + ' on ' + @server_name + '...'
/*
--Must rem out since Assemblies are only valid for MSSQL Server 2008
EXEC Connect @log_path, @server_name, @port_no, @company_no, @store_no, @register_no, @errno output, @errdesc output
SELECT @errno = @@error
IF @errno <> 0
BEGIN
  SELECT @errmsg = 'Failed to exec Connect',
         @object_name    = 'Connect',
         @operation_name = 'EXEC'
  GOTO error
END
*/
PRINT Str(@errno) + ' ' + @errdesc

PRINT 'Authorizing reference number ' + @reference_no 
/*
--Must rem out since Assemblies are only valid for MSSQL Server 2008
EXEC AuthOnly 69, 'Order1', '4055011111111111','1210', '7100', '2800 Trans-Canada, Pointe-Claire, Quebec', 'H0H0H0', @current_approval_message output, @current_authorization_no output, @errno output, @errmsg output
SELECT @errno = @@error
IF @errno <> 0
BEGIN
  SELECT @errmsg = 'Failed to exec AuthOnly',
         @object_name    = 'AuthOnly',
         @operation_name = 'EXEC'
  GOTO error
END
*/
print '@current_approval_message= ' + @orig_approval_message 
print '@current_authorization_no= ' + @orig_authorization_no 
print Str(@errno) + ' ' + @errmsg


SELECT @current_approval_message = @orig_approval_message
SELECT @current_authorization_no = @orig_authorization_no
PRINT 'Current Authorization No:  ' + @current_authorization_no
PRINT 'Reversing Visa...'
/*
EXEC VisaReversal 69, 'Order1', '4055011111111111','1210', '1100', '095627', @orig_approval_message output, @orig_authorization_no output, @errno output, @errmsg output
SELECT @errno = @@error
IF @errno <> 0
BEGIN
  SELECT @errmsg = 'Failed to exec AuthOnly',
         @object_name    = 'AuthOnly',
         @operation_name = 'EXEC'
  GOTO error
END
print '@orig_approval_message= ' + @orig_approval_message 
print '@orig_authorization_no= ' + @orig_authorization_no 
print Str(@errno) + ' ' + @errmsg
*/

PRINT 'Disconnecting...'
/*
--Must rem out since Assemblies are only valid for MSSQL Server 2008
EXEC Disconnect
SELECT @errno = @@error
IF @errno <> 0
BEGIN
  SELECT @errmsg = 'Failed to exec Disconnect',
         @object_name    = 'Disconnect',
         @operation_name = 'EXEC'
  GOTO error
END
*/

RETURN

error:   /* Common error handler */

          
  EXEC common_error_handling_$sp @process_no, @errno, @errmsg, 0, @message_id, 
       @process_name, @object_name, @operation_name, 1, 
       @edit_process_no,  0, null, 0, null, null, null, null, null, null, 0, @process_id, @user_id

  RETURN
```

