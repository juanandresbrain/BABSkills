# dbo.ecp_comms_auto_adj_custom_$sp

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.ecp_comms_auto_adj_custom_$sp"]
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
    employee_comms_auto_adj(["employee_comms_auto_adj"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| common_error_handling_$sp |
| employee_comms_auto_adj |

## Stored Procedure Code

```sql
create proc [dbo].[ecp_comms_auto_adj_custom_$sp]    @pay_period_close_date	datetime,
   @lowest_calendar_level	int,
   @lowest_calendar_level_id	binary(16),
   @ecp_clndr_id	        binary(16),
   @auto_adjustment_description nvarchar(255),
   @auto_commission_adj_id      numeric(5,0),
   @auto_reversal_flag          tinyint
AS
/* 
Proc Name: ecp_comms_auto_adj_custom_$sp
Desc:   Sample ECP custom auto-commission-adjustment proc

HISTORY:  
Date     Name           Def#    Desc
Aug10,15 Vicci     TFS-134960   Correct to determine whether to post to reference amount type or commission adjustment.     
Apr14,11 Paul          126153   Use unicode datatypes
Aug08,08 Vicci         103077   Add additional fields to sample insert.
Apr05,07 Vicci		85597	Author

*/

SET NOCOUNT ON
DECLARE
  @errmsg                       nvarchar(255),
  @errno                        int,
  @errno2                       int,
  @message_id                   int,
  @process_name                 nvarchar(100),
  @process_no                   int,
  @object_name                  nvarchar(255),
  @operation_name               nvarchar(100),
  @rows							int,
  @stream_no                    tinyint,
  @sql_command 					nvarchar(3000),
  @adj_hist_posting_datetime	datetime,
  @adjustment_comment			nvarchar(1000),
  @reference_amount_type		smallint

SELECT @errno = 0,
       @message_id = 201068,
       @operation_name = 'Unknown',
       @process_name = 'ecp_comms_auto_adj_custom_$sp',
       @process_no = 282,
       @stream_no = 1,
	   @adj_hist_posting_datetime = getdate()

SELECT @adjustment_comment = adjustment_comment,
       @reference_amount_type = reference_amount_type
  FROM employee_comms_auto_adj
 WHERE auto_commission_adj_id = @auto_commission_adj_id
SELECT @errno = @@error
IF @errno <> 0
BEGIN
  SELECT @errmsg = 'Failed to determine adjustment type',
         @object_name = 'employee_comms_auto_adj',
         @operation_name = 'SELECT'
  GOTO error
END       

INSERT into #ecp_comms_adj(adj_hist_posting_datetime,
       auto_commission_adj_id,
       employee_no,
       home_store_no,
       primary_position,
       primary_selling_area_no,
       adjustment_description,
       adjustment_comment,
       reference_amount_type,
       auto_rev_flag,
       commission_adj_amount)
VALUES(@adj_hist_posting_datetime,
       @auto_commission_adj_id,
       11, --employee_no,
       2228, --home_store_no,
       '2', --primary_position,
       251, --primary_selling_area_no,
       @auto_adjustment_description,
       @adjustment_comment,
       @reference_amount_type,
       @auto_reversal_flag,
       25)  --commission_adj_amount
SELECT @errno = @@error
IF @errno <> 0
BEGIN
  SELECT @errmsg = 'Failed to log custom auto-commission-adjustment amounts',
         @object_name = '#ecp_comms_adj',
         @operation_name = 'INSERT'
  GOTO error
END
RETURN

error:
  EXEC common_error_handling_$sp @process_no, @errno, @errmsg, 0, @message_id, @process_name, @object_name, @operation_name, 1, @stream_no

  RETURN
```

