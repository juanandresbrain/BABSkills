# dbo.ecp_commission_rate_lookup_$sp

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.ecp_commission_rate_lookup_$sp"]
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| common_error_handling_$sp |

## Stored Procedure Code

```sql
create proc [dbo].[ecp_commission_rate_lookup_$sp] @employee_commission_code    nvarchar(3000) = null, 
@employee_transaction_role   nvarchar(3000) = null, 
@item_commission_code        nvarchar(3000) = null, 
@store_commission_code       nvarchar(3000) = null, 
@transaction_commission_code nvarchar(3000) = null,
@as_of_and_later_date	     datetime = null,
@summary_flag		     tinyint = 0 --0=detail, 1=summary, 2=tier detail of summary
AS
/* 
Proc Name: ecp_commission_rate_lookup_$sp 
Desc:   Called by UI.
        Returns list of employee_commission_rate_def table entries that control the rate set for a given lookup combination.
        
HISTORY:  
Date     Name           Def#    Desc
Apr14,11 Paul          126153   Use unicode datatypes
Apr09,08 Vicci          98558   Add new @summary_flag as an input parameter and return summary entries instead of details if selected.
Feb22,08 Vicci          98558   Author
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
        @user_name                   nvarchar(30),
        @all			     nvarchar(3000),
        @sql_command                 nvarchar(3000),
        @stream_no                   tinyint

SELECT @errno = 0,
       @message_id = 201068,
       @object_name = 'Unknown',
       @operation_name = 'Unknown',
       @process_name = 'ecp_commission_rate_lookup_$sp',
       @process_no = 0,
       @stream_no = 1,
       @all = '''-1'''

IF @as_of_and_later_date IS NULL
  SELECT @as_of_and_later_date = '01/01/1970'
IF @employee_commission_code IS NULL
  SELECT @employee_commission_code = @all
IF @employee_transaction_role IS NULL
  SELECT @employee_transaction_role = @all
IF @item_commission_code IS NULL
  SELECT @item_commission_code = @all
IF @store_commission_code IS NULL
  SELECT @store_commission_code = @all
IF @transaction_commission_code IS NULL
  SELECT @transaction_commission_code = @all

SELECT @sql_command = '
SELECT employee_commission_code,
       employee_transaction_role,
       item_commission_code,
       store_commission_code,
       transaction_commission_code,
       sequence_no,
       effective_from_date,
       effective_to_date,
       employee_ecp_rate_id,
       tier_accumulation_basis,
       commission_rate,
       commission_amount_per_item
  FROM employee_commission_rate_dtl
 WHERE (@employee_commission_code = @all OR employee_commission_code in (' + @employee_commission_code + '))
   AND (@employee_transaction_role = @all OR employee_transaction_role in (' + @employee_transaction_role + '))
   AND (@item_commission_code = @all OR item_commission_code in (' + @item_commission_code + '))
   AND (@store_commission_code = @all OR store_commission_code in (' + @store_commission_code + '))
   AND (@transaction_commission_code = @all OR transaction_commission_code in (' + @transaction_commission_code + '))
   AND (effective_to_date >= @as_of_and_later_date OR effective_to_date IS NULL)'
SELECT @errno = @@error
IF @errno <> 0
BEGIN
  SELECT @errmsg = 'Failed to create statement required to lookup commission rate definition via dynamic SQL',
         @object_name = '@sql_command',
         @operation_name = 'SELECT'
  GOTO error
END

IF @summary_flag = 1
BEGIN
  SELECT @sql_command = '
         SELECT employee_ecp_rate_id, employee_ecp_rate_descr, employee_ecp_rate_comment, employee_commission_code, employee_transaction_role, item_commission_code, store_commission_code, transaction_commission_code, tier_accumulation_basis, effective_from_date, effective_to_date, commission_rate, commission_amount_per_item, sequence_no, last_modified_datetime 
    FROM employee_commission_rate_def
          WHERE employee_ecp_rate_id IN (SELECT DISTINCT employee_ecp_rate_id FROM (' 
         + @sql_command + ') q )'
END --IF @summary_flag = 1
ELSE
  IF @summary_flag = 2
  BEGIN
  SELECT @sql_command = '
         SELECT employee_ecp_rate_id, tier_id, tier_amount_from, tier_amount_to, commission_rate, commission_amount_per_item  
           FROM employee_commission_rate_tier 
          WHERE employee_ecp_rate_id IN (SELECT DISTINCT employee_ecp_rate_id FROM (' 
         + @sql_command + ') q )'
  END
  ELSE
  BEGIN
    SELECT @sql_command = @sql_command + '
     ORDER BY employee_commission_code,
         employee_transaction_role,
         item_commission_code,
         store_commission_code,
         transaction_commission_code,
         CASE WHEN sign(tier_accumulation_basis) > 0 THEN 1 ELSE 0 END,
         sequence_no,
         effective_from_date,
         effective_to_date' 
  END

SELECT @sql_command = @sql_command + '
       SELECT @errno = @@error'
       
EXEC sp_executesql @sql_command, N'@employee_commission_code nvarchar(3000), 
         @employee_transaction_role nvarchar(3000),
         @item_commission_code nvarchar(3000),
         @store_commission_code nvarchar(3000),
         @transaction_commission_code nvarchar(3000),
         @as_of_and_later_date datetime, 
         @all nvarchar(20),
         @errno int OUT', @employee_commission_code, @employee_transaction_role, @item_commission_code, @store_commission_code, @transaction_commission_code, @as_of_and_later_date, @all, @errno OUT              
SELECT @errno2 = @@error
IF @errno <> 0 OR @errno2 <> 0
BEGIN
  PRINT @sql_command
  IF @errno2 <> 0 SELECT @errno = @errno2
  SELECT @errmsg = 'Failed to lookup commission rate definition via dynamic SQL',
         @object_name = 'employee_commission_rate_dtl',
         @operation_name = 'SELECT'
  GOTO error
END

RETURN

error:

  EXEC common_error_handling_$sp @process_no, @errno, @errmsg, 0, @message_id, @process_name, @object_name, @operation_name, 1, @stream_no

  RETURN
```

