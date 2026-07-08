# dbo.ecp_commission_rate_del_$sp

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.ecp_commission_rate_del_$sp"]
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
    ecp_system_flag(["ecp_system_flag"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| common_error_handling_$sp |
| ecp_system_flag |

## Stored Procedure Code

```sql
create proc [dbo].[ecp_commission_rate_del_$sp] @clone_column	  nvarchar(30), --valid values are employee_commission_code, employee_transaction_role, item_commission_code, store_commission_code, transaction_commission_code
@dest_code_list nvarchar(3000),
@process_id int = null
AS
/* 
Proc Name: ecp_commission_rate_del_$sp 
Desc:   Called by front end.
        Removes commission codes specified from the employee_commission_rate_def table.

HISTORY:  
Date     Name           Def#    Desc
Apr14,11 Paul          126153   Use unicode datatypes
Apr18,08 Vicci          98558   Remove item_commission_code reference which had been hard-code for testing.
Feb27,08 Vicci          98558   Author
*/

SET NOCOUNT ON
DECLARE @errmsg                      nvarchar(255),
        @errno                       int,
        @errno2			     int,
        @message_id                  int,
        @object_name                 nvarchar(255),
        @operation_name              nvarchar(100),
        @process_name                nvarchar(100),
        @process_no                  int,
        @stream_no                   tinyint,
        @user_name                   nvarchar(30),
        @position		     smallint,
        @sql_command 	             nvarchar(3000),
        @sql_command2 	             nvarchar(3000),
        @issue			     tinyint,
        @dest_code		     nvarchar(20),
        @all			     nvarchar(3000),
        @quoted_dest_code	     nvarchar(22),
        @comma_quoted_dest_code      nvarchar(23),
        @quoted_dest_code_comma      nvarchar(23)
  
SELECT @errno = 0,
       @message_id = 201068,
       @object_name = 'Unknown',
       @operation_name = 'Unknown',
       @process_name = 'ecp_commission_rate_del_$sp',
       @process_no = 0,
       @stream_no = 1,
       @user_name = suser_sname(),
       @issue = 0,
       @all = '''-1''' 

IF IsNull(@dest_code_list, '') = '' 
BEGIN
  SELECT @object_name = '@dest_code_list',
         @errmsg = 'Cannot proceed:  the @dest_code_list input parameter is invalid.',
         @operation_name = 'SELECT'
  GOTO error
END

IF IsNull(@clone_column, '') NOT IN ('employee_commission_code', 'employee_transaction_role', 'item_commission_code', 'store_commission_code', 'transaction_commission_code') 
BEGIN
  SELECT @object_name = '@clone_column',
         @errmsg = 'Cannot proceed:  the @clone_column input parameter is invalid.',
         @operation_name = 'SELECT'
  GOTO error
END

IF EXISTS (SELECT 1 
             FROM ecp_system_flag
            WHERE flag_name = 'ecp_rebuild_commission_rate' AND flag_numeric_value = 1)
BEGIN
  SELECT @errmsg = 'Recent configuration changes have not yet been processed.  Please try again later.',
         @message_id = 202018,
         @errno = 202018,
         @object_name = 'ecp_system_flag',
         @operation_name = 'SELECT'
  GOTO error
END

SELECT @sql_command = '
       UPDATE employee_commission_rate_def 
          SET ' + @clone_column + '= stuff(' + @clone_column + ', CHARINDEX(@quoted_dest_code,' + @clone_column + ' ), datalength(@quoted_dest_code), '''')
         FROM employee_commission_rate_def
        WHERE employee_ecp_rate_id IN (SELECT DISTINCT employee_ecp_rate_id
                                              FROM employee_commission_rate_dtl
                                              WHERE ' + @clone_column + ' = @dest_code) 
          AND ' + @clone_column + ' <> @all
          AND ' + @clone_column + ' like ''%'' + @quoted_dest_code + ''%'''
          
SELECT @sql_command2 = '
       DELETE employee_commission_rate_def 
         FROM employee_commission_rate_def
        WHERE employee_ecp_rate_id IN (SELECT DISTINCT employee_ecp_rate_id
                                              FROM employee_commission_rate_dtl
                                              WHERE ' + @clone_column + ' = @dest_code) 
          AND ' + @clone_column + ' = @quoted_dest_code'

--Remove quotes from comma delimited list
SELECT @position = CHARINDEX('''', @dest_code_list)
WHILE @position > 0
BEGIN

  SELECT @dest_code_list = stuff(@dest_code_list, CHARINDEX('''', @dest_code_list), 1, '')  
  SELECT @position = CHARINDEX('''', @dest_code_list)

END

SELECT @position = CHARINDEX(',', @dest_code_list)
WHILE @position > 0
BEGIN

  SELECT @dest_code = ltrim(rtrim(substring(@dest_code_list, 1, @position - 1)))

  SELECT @quoted_dest_code = '''' + @dest_code + ''''
  SELECT @comma_quoted_dest_code = ',' + @quoted_dest_code
  SELECT @quoted_dest_code_comma = @quoted_dest_code + ','

  EXEC sp_executesql @sql_command, N'@dest_code nvarchar(20), @quoted_dest_code nvarchar(22), @all nvarchar(3000), @errno int OUT', @dest_code, @comma_quoted_dest_code, @all, @errno OUT   
  SELECT @errno2 = @@error
  IF @errno <> 0 OR @errno2 <> 0
  BEGIN
    PRINT @sql_command
    IF @errno2 <> 0 SELECT @errno = @errno2
    SELECT @errmsg = 'Removal of ' + @dest_code + ' from commission rate definition failed.',
           @object_name = 'employee_commission_rate_def',
           @operation_name = 'UPDATE'
    GOTO error
  END
  EXEC sp_executesql @sql_command, N'@dest_code nvarchar(20), @quoted_dest_code nvarchar(22), @all nvarchar(3000), @errno int OUT', @dest_code, @quoted_dest_code_comma, @all, @errno OUT   
  SELECT @errno2 = @@error
  IF @errno <> 0 OR @errno2 <> 0
  BEGIN
    PRINT @sql_command
    IF @errno2 <> 0 SELECT @errno = @errno2
    SELECT @errmsg = 'Removal of ' + @dest_code + ' from beginning of commission rate definition failed.',
           @object_name = 'employee_commission_rate_def',
           @operation_name = 'UPDATE'
    GOTO error
  END
  EXEC sp_executesql @sql_command2, N'@dest_code nvarchar(20), @quoted_dest_code nvarchar(22), @errno int OUT', @dest_code, @quoted_dest_code, @errno OUT   
  SELECT @errno2 = @@error
  IF @errno <> 0 OR @errno2 <> 0
  BEGIN
    PRINT @sql_command
    IF @errno2 <> 0 SELECT @errno = @errno2
    SELECT @errmsg = 'Deletion of commission rate definition for ' + @dest_code + ' failed.',
           @object_name = 'employee_commission_rate_def',
           @operation_name = 'DELETE'
    GOTO error
  END

  SELECT @dest_code_list = substring(@dest_code_list, @position + 1, 4000)
  SELECT @position = CHARINDEX(',', @dest_code_list)
END

SELECT @dest_code = (ltrim(rtrim(@dest_code_list)))

SELECT @quoted_dest_code = '''' + @dest_code + ''''
SELECT @comma_quoted_dest_code = ',' + @quoted_dest_code
SELECT @quoted_dest_code_comma = @quoted_dest_code + ','

EXEC sp_executesql @sql_command, N'@dest_code nvarchar(20), @quoted_dest_code nvarchar(22), @all nvarchar(3000), @errno int OUT', @dest_code, @comma_quoted_dest_code, @all, @errno OUT   
SELECT @errno2 = @@error
IF @errno <> 0 OR @errno2 <> 0
BEGIN
  PRINT @sql_command
  IF @errno2 <> 0 SELECT @errno = @errno2
  SELECT @errmsg = 'Removal of last ' + @dest_code + ' from beginning of commission rate definition failed.',
         @object_name = 'employee_commission_rate_def',
         @operation_name = 'UPDATE'
  GOTO error
END
EXEC sp_executesql @sql_command, N'@dest_code nvarchar(20), @quoted_dest_code nvarchar(22), @all nvarchar(3000), @errno int OUT', @dest_code, @quoted_dest_code_comma, @all, @errno OUT   
SELECT @errno2 = @@error
IF @errno <> 0 OR @errno2 <> 0
BEGIN
  PRINT @sql_command
  IF @errno2 <> 0 SELECT @errno = @errno2
  SELECT @errmsg = 'Removal of last ' + @dest_code + ' from beginning of commission rate definition failed.',
         @object_name = 'employee_commission_rate_def',
         @operation_name = 'UPDATE'
  GOTO error
END
EXEC sp_executesql @sql_command2, N'@dest_code nvarchar(20), @quoted_dest_code nvarchar(22), @errno int OUT', @dest_code, @quoted_dest_code, @errno OUT   
SELECT @errno2 = @@error
IF @errno <> 0 OR @errno2 <> 0
BEGIN
  PRINT @sql_command
  IF @errno2 <> 0 SELECT @errno = @errno2
  SELECT @errmsg = 'Deletion of commission rate definition for last' + @dest_code + ' failed.',
         @object_name = 'employee_commission_rate_def',
         @operation_name = 'DELETE'
  GOTO error
END


RETURN

error:

  EXEC common_error_handling_$sp @process_no, @errno, @errmsg, 0, @message_id, @process_name, @object_name, @operation_name, 1, @stream_no

  RETURN
```

