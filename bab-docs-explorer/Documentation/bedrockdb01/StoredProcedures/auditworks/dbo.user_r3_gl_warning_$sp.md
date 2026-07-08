# dbo.user_r3_gl_warning_$sp

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.user_r3_gl_warning_$sp"]
    auditworks_parameter(["auditworks_parameter"]) --> SP
    auditworks_system_flag(["auditworks_system_flag"]) --> SP
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| auditworks_parameter |
| auditworks_system_flag |
| common_error_handling_$sp |

## Stored Procedure Code

```sql
create proc dbo.user_r3_gl_warning_$sp 
 AS

/* Proc name: user_r3_gl_warning_$sp
** Description: Dummy proc to print warnings to upgrade log that indicate when 
** 		defect fixes are available for customizable base gl export procs.
**		This proc also contains the defect fix logic that would need to be copied to the customized procs.
**		Those base procs are customizable and cannot be overlayed on upgrade.
**		The updates would need to be entered manually onsite after running differences (see comments below).
**

HISTORY:
Date     Name        Def# Desc
Nov12,10 Paul      121833 Add missing gl_posting_datetime setting; remove usage of BETWEEN date range since
                          @last_date_closed should be excluded;  also update dw_subledger on consolidated
Apr20,10 Vicci     117228 Don't set Last Date Closed since this is already done but with correct condition in reset_period_end_$sp.
			  Update status to 500 and set posted to G/L flag based on i_period_ending_date instead of i_period_end_date since for some
			  clients the G/L posting takes place daily, not just at period end and since preliminary period end is available.
Oct18,05 Paul       60970 correctly initialize @current_date

*/

DECLARE
	@current_date 				smalldatetime,
	@errmsg 				varchar(255),
	@errno 					int,
	@instance_id				int,
	@loop_date				smalldatetime,
	@process_log_entry 			bit,
	@process_no 				smallint,
	@process_timestamp 			float,
	@transaction_count 			numeric(12,0),
	@scaleout_flag				int,
	@scaleout_gl_export_on_peri		tinyint,
	@message_id				int,
	@object_name				varchar(255),
	@process_name				varchar(100),
	@operation_name				varchar(100)

SELECT @process_name = 'user_r3_gl_interface_$sp',
	@message_id = 201068,
	@process_no = 205,
	@current_date = getdate()

/* copy the select logic below to the top of the custom proc(s) */

SELECT @process_log_entry = 1,
	@scaleout_flag = 0,
	@scaleout_gl_export_on_peri = 0,
	@instance_id = 0

SELECT @scaleout_flag = flag_numeric_value
  FROM auditworks_system_flag
 WHERE flag_name = 'scaleout_flag'

SELECT @scaleout_gl_export_on_peri = CONVERT(tinyint,par_value)
  FROM auditworks_parameter 
 WHERE par_name = 'scaleout_gl_export_on_peri'

SELECT @instance_id = flag_numeric_value
  FROM auditworks_system_flag
 WHERE flag_name = 'instance_id'


/* the following logic will print warning messages to the upgrade log. 
   Do not copy to the custom procs */

SELECT @errmsg = '*** WARNING *** Defect updates are available for customized G/L export procs.'
PRINT @errmsg
SELECT @errmsg = 'For SA5, defect fixes 121833 and 117228 are available for user_r3_gl_interface_$sp.'
PRINT @errmsg
SELECT @errmsg = 'For SA5, would need to update any customized gl export procs manually.'
PRINT @errmsg

SELECT @errmsg = '121833 Need to update gl_posting_datetime; exclude @last_date_closed from date range; handle scaleout environment.'
PRINT @errmsg

SELECT @errmsg = '117228 Set posted to G/L flag based on @period_ending_date to handle daily preliminary period ends.'
PRINT @errmsg

-- BEGIN TRANSACTION

/********************************************************************************/
/**                                                                            **/
/**                                                                            **/
/**                                                                            **/
/**                          BODY OF CUSTOM CODE HERE                          **/
/**                                                                            **/
/**                                                                            **/
/**           **/
/********************************************************************************/


/* the code below contains the defect changes
  copy this logic to the lower part of the customized proc(s) as needed */

/*
  -- Set subledger posting status to yes

  UPDATE subledger
    SET posting_status = 1,
	gl_posting_datetime = @current_date
   WHERE posting_status = 0
     AND transaction_date > @last_date_closed
     AND transaction_date <= @period_end_date

  SELECT @errno = @@error
  IF @errno <> 0
    BEGIN
     SELECT @errmsg = 'Failed to update subledger with posting_status to 1',
	@object_name = 'subledger',
        @operation_name = 'UPDATE'
     GOTO error
    END

  -- If running export on peripheral, also need to set posted_status in subledger on consolidated
  IF @scaleout_gl_export_on_peri = 1 AND @scaleout_flag = 1 -- THEN 
    BEGIN
    -- Using loop to batch by date and to improve scaleout query plan
    SELECT @loop_date = DATEADD(dd,1,@last_date_closed)

    WHILE @loop_date <= @period_end_date
    BEGIN
	      UPDATE dw_subledger
	         SET posting_status = 1,
	             gl_posting_datetime = @current_date
	       WHERE posting_status = 0
	         AND transaction_date = @loop_date 
	         AND store_no
	             IN (SELECT DISTINCT store_no
	                 FROM subledger
	                 WHERE transaction_date = @loop_date
	                   AND posting_status >= 1)

		  SELECT @errno = @@error
		  IF @errno <> 0
		    BEGIN
		     SELECT @errmsg = 'Failed to update dw_subledger with posting_status to 1',
			@object_name = 'dw_subledger',
			@operation_name = 'UPDATE'
			GOTO error
		    END
	SELECT @loop_date = DATEADD(dd,1,@loop_date)
    END -- While
    END -- If @scaleout_gl_export_on_peri = 1


  UPDATE audit_status
    SET audit_status = 500,
       status_date =  @current_date
   WHERE audit_status = 400
     AND sales_date > @last_date_closed
     AND sales_date <= @period_end_date

  SELECT @errno = @@error
  IF @errno <> 0
    BEGIN
     SELECT @errmsg = 'Failed to update audit_status to 500 from 400',
	@object_name = 'audit_status',
        @operation_name = 'UPDATE'
     GOTO error
    END

  UPDATE store_audit_status
    SET store_audit_status = 500,
        store_status_date = @current_date
   WHERE store_audit_status = 400
     AND sales_date > @last_date_closed
     AND sales_date <= @period_end_date

  SELECT @errno = @@error
  IF @errno <> 0
    BEGIN
     SELECT @errmsg = 'Failed to update store_audit_status to 500 from 400',
	@object_name = 'store_audit_status',
        @operation_name = 'UPDATE'
     GOTO error
    END

  UPDATE dw_store_status
     SET store_status = 3
   WHERE store_status = 2 
     AND subledger_copied_flag = 1
     AND sales_date > @last_date_closed
     AND sales_date <= @period_end_date
     AND instance_id = @instance_id

  SELECT @errno = @@error
  IF @errno <> 0
    BEGIN
	SELECT @errmsg = 'Unable to set store_status to 3 from 2',
	       @object_name = 'dw_store_status',
	       @operation_name = 'UPDATE'
	GOTO error
    END

COMMIT TRAN

*/





RETURN

/* Common error handler */
error:  

	EXEC common_error_handling_$sp @process_no, @errno, @errmsg, 0, @message_id, 
	  @process_name, @object_name, @operation_name, 1, 1, 1, @process_timestamp, @transaction_count

	RETURN
```

