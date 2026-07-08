# dbo.edit_verify_registers_$sp

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.edit_verify_registers_$sp"]
    ORG_CHN(["ORG_CHN"]) --> SP
    ORG_CHN_WRKSTN(["ORG_CHN_WRKSTN"]) --> SP
    ORG_CHN_WRKSTN_CNFG(["ORG_CHN_WRKSTN_CNFG"]) --> SP
    ORG_CHN_WRKSTN_CNFG_A(["ORG_CHN_WRKSTN_CNFG_A"]) --> SP
    audit_status(["audit_status"]) --> SP
    auditworks_parameter(["auditworks_parameter"]) --> SP
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
    duplicate_transaction(["duplicate_transaction"]) --> SP
    edit_store_date_list(["edit_store_date_list"]) --> SP
    end_process_log__sp(["end_process_log_$sp"]) --> SP
    exception_reason(["exception_reason"]) --> SP
    media_reconciliation_status(["media_reconciliation_status"]) --> SP
    media_unreconciliation(["media_unreconciliation"]) --> SP
    parameter_general(["parameter_general"]) --> SP
    process_error_log(["process_error_log"]) --> SP
    start_process_log__sp(["start_process_log_$sp"]) --> SP
    store_audit_status(["store_audit_status"]) --> SP
    transaction_header(["transaction_header"]) --> SP
    transaction_missing(["transaction_missing"]) --> SP
    translate_error(["translate_error"]) --> SP
    verify_store_status__sp(["verify_store_status_$sp"]) --> SP
    work_edit_batch_list(["work_edit_batch_list"]) --> SP
    work_rec_incomplete(["work_rec_incomplete"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ORG_CHN |
| ORG_CHN_WRKSTN |
| ORG_CHN_WRKSTN_CNFG |
| ORG_CHN_WRKSTN_CNFG_A |
| audit_status |
| auditworks_parameter |
| common_error_handling_$sp |
| duplicate_transaction |
| edit_store_date_list |
| end_process_log_$sp |
| exception_reason |
| media_reconciliation_status |
| media_unreconciliation |
| parameter_general |
| process_error_log |
| start_process_log_$sp |
| store_audit_status |
| transaction_header |
| transaction_missing |
| translate_error |
| verify_store_status_$sp |
| work_edit_batch_list |
| work_rec_incomplete |

## Stored Procedure Code

```sql
CREATE proc  dbo.edit_verify_registers_$sp 
 @process_id            binary(16),
 @user_id		int,
 @process_timestamp     float,
 @errmsg                nvarchar(2000) OUTPUT,
 @trickle_finished_flag tinyint /* always 1 */

AS

  /* 
  
    Proc name : edit_verify_registers_$sp
         Desc : Verify all edited store_reg_dates (status = 100).
                Set status to 200 (verified) for all that meet verification criteria.
                If autaccept_flag is on for a verified store then set status = 300 (accepted).
                Uses cursor to minimize locking.
                Called by edit_phase2_$sp.
    Unicode version.
    
HISTORY

Date     Name           Def#  Desc
Aug19,16 Vicci     DAOM-1293  Take store closeout (store completion date/time) into account in auto-accept when logical trading date handling is active too.
May27,16 Vicci      DAOM-730  Pass correct date_reject_id to verify_store_status_$sp;
                              Don't unconditionally unlock store/date:  this is properly in phase2 later on.
May20,16 Vicci      DAOM-730  Handle possibility of status 100, 200, 300 with no transactions needing fixing.
                              Call verify_store_status_$sp with edit flag 5 to indicate phase 2.
May18,16 Vicci      DAOM-682  Refix to handle duplicate_qty and unreconciled_media_present when skipping downgrade status to 100 for when no auditing concerns existed.
Apr29,16 Vicci      DAOM-682  Use try catch since edit_phase2_$sp uses try catch.
                              Don't downgrade status to 100 and report erroneous "Edit_verify_registers_$sp has autocorrected an incorrect audit_status." warnings
                              when the status was correct to begin with and no auditing concerns existed.
Dec02,14 Vicci     TFS-94637  Ensure store_audit_status is updated even when the batch did not contain any "audit-concern-free" store/dates.
                              Otherwise store_audit_status is left at Edited instead of Invalid Store and/or Invalid Register, for example.
Jan27,14 Vicci        141621  Leave status at Edited if unreconciled media beyond tolerance already exists.
Oct21,10 Vicci        121948  Since unreconciled FLOAT rec-type amounts are now considered activity too, ensure they
                              only prevent auto-accept if the drawer fund has changed.
Apr05,10 Vicci        115666  When re-evaluating a status > 100 that has audit-concerns, downgrade the status to 100
			      if the status is 200 (not only if it is 300).
Nov20,09 Vicci        113373  For the purpose of the Auto-Accept, ignore closeouts which do not fall within the defined 
			      pre/post midnight times when logical trading date handling is in use.
Apr25,08 Paul          98023  Uplift 1-3WGK0B to SA5
Apr05.07 Daphna      DV-1360  uplift 84045  update other registers in verify_store_status for all stores
Feb05,07 Paul        DV-1355  port 1-39RAI3 to SA5
Apr18,05 Paul        DV-1218  pass 1 in @verify_store_status when calling verify_store_status_$sp
Dec15,04 Maryam      DV-1191  Improve performance.
Oct12,04 Maryam      DV-1146  Modify the call to verify_store_status_$sp to pass 1 for @called_by_edit.
May18,04 David       DV-1071  Use ORG_CHN table instead of store_salesaudit, receive @process_id, @user_id
Apr17,08 Paul       1-3WGK0B  prevent auto-verification of store-dates that are being processed on another stream
Mar12.07 Daphna        84045  update other registers in verify_store_status for all stores
Mar20,06 Daphna     1-39RAI3  Pass new flag in call to verify_store_status
                     / 69360
Dec29,03 Paul        DV-1007  do not autoverify store-dates for which media rec posting failed, remove select into
Jul10,03 Maryam      1-KL08H  Support new auto-accept flag of 3 and 4. Modified options 1
                              and 2 to additionally verify that no reconciliations are 
                              missing for the store/date.
Jan02,03 Paul        1-HNQKP  re-evaluate translate_error_verified flag
Nov27,01 Ian K       1-97UU6  Edit Phase 2 batching for R3
Oct03,00 Paul           6776  Reevaluate exceptions_verified flag 
Jun05,00 Maryam         6244  Closeout flag of 2 is acceptable for auto-accept method 1
Mar01,00 Phu            5900  Change @@fetch_status > 0 to @@fetch_status <> 0 for MS SQL compatibility
Sep18,98 Paul
Apr21,98 Paul                 Author

  */

DECLARE

  @audit_status                 smallint,
  @autoaccept_flag              tinyint,
  @current_date                 smalldatetime,
  @closeout_exists              tinyint,
  @closeout_flag                tinyint,
  @current_day_autoaccept_time  smallint,
  @cursor_open                  tinyint,
  @date_reject_id		tinyint,
  @errno                        int,
  @errmsg2			nvarchar(2000),
  @errline			int,
  @exceptions_verified          tinyint,
  @latest_date_to_accept        smalldatetime,
  @media_rec_verified           tinyint,
  @opening_drawer_discrepancy   tinyint,
  @prev_sales_date              smalldatetime,
  @prev_store_no                int,
  @process_log_entry            tinyint,
  @process_no                   smallint,
  @register_no                  smallint,
  @sales_date                   smalldatetime,
  @short_by_tender_over_limit   tinyint,
  @store_audit_status           smallint,
  @store_no               	int,
  @transaction_count            numeric(12,0),
  @translate_error_verified	tinyint,
  @unreconciled_media_present	tinyint,
  @update_in_progress           smallint,
  @valid_qty                    smallint,
  @object_name                  nvarchar(255),
  @process_name                 nvarchar(100),
  @operation_name               nvarchar(100),
  @message_id	                int,
  @exception_qty		smallint,
  @translate_error_qty		smallint,
  @default_post_midnight_time	int,
  @default_pre_midnight_time	int,
  @completion_date_time		datetime,
  @store_completion_date_time	datetime,
  @issue_flag			int,
  @missing_qty			int,
  @missing_verified		int,
  @duplicate_qty		int,
  @duplicate_verified		int,
  @sa_reject_qty		int,
  @corrections			int,
  @register_poll_id		nvarchar(15),
  @new_status			smallint
  
  SELECT @process_name     = 'edit_verify_registers_$sp',
         @message_id       = 201068

  SELECT @current_date      = getdate(),
         @errmsg            = NULL,
         @process_log_entry = 0,
         @process_no        = 84,
         @transaction_count = 0

BEGIN TRY
  SELECT @errmsg       = 'Unable to execute start_process_log_$sp',
         @object_name    = 'execute start_process_log_$sp',
         @operation_name = 'EXECUTE'
  EXEC start_process_log_$sp @process_no, @process_timestamp OUTPUT, @errmsg OUTPUT;

  SELECT @errmsg = 'Failed to select default_pre_midnight_time from auditworks_parameter',
         @object_name = 'auditworks_parameter',
         @operation_name = 'SELECT';
  SELECT @default_pre_midnight_time = CONVERT(int, par_value)
    FROM auditworks_parameter
   WHERE par_name = 'default_pre_midnight_time';


  SELECT @errmsg = 'Failed to select default_post_midnight_time from auditworks_parameter'
  SELECT @default_post_midnight_time = CONVERT(int, par_value)
    FROM auditworks_parameter
   WHERE par_name = 'default_post_midnight_time';

  SELECT @errmsg = 'Failed to set @current_day_autoaccept_time',
         @object_name = 'parameter_general';
  SELECT @current_day_autoaccept_time = ISNULL(current_day_autoaccept_time, 2100)
    FROM parameter_general;

  SELECT @errmsg = 'Failed to set @latest_date_to_accept. ',
         @object_name = NULL;
  SELECT @process_log_entry = 1,
         @latest_date_to_accept = CONVERT(smalldatetime, CONVERT(nchar(6),@current_date,12));
  -- If current time < @current_day_autoaccept_time then don't allow autoaccepting sales
  -- with the same sales_date as the current system date. Prevents manual polls from
  -- autoaccepting sales for the current date.

  IF DATEPART(hh, @current_date) * 100
    + DATEPART(mi, @current_date) < @current_day_autoaccept_time
    SELECT @latest_date_to_accept = DATEADD(dd, -1, @latest_date_to_accept)

  -- Re-evaluate whether exceptions have been verified for audit_status rows
  -- which existed before the edit was run.
  -- Also correct any possible integrities related to multistream

  SELECT @errmsg = 'Failed to handle reevaluate_crsr',
         @object_name = 'reevaluate_crsr',
         @operation_name = 'DECLARE';
  DECLARE reevaluate_crsr CURSOR FAST_FORWARD
    FOR
    SELECT e.store_no,
           e.transaction_date,
           e.register_no,
           e.date_reject_id,
           a.audit_status,
           a.exception_qty,
           a.translate_error_qty,
           a.missing_qty,
           a.duplicate_qty,
           a.unreconciled_media_present,
           a.valid_qty,
           a.sa_reject_qty,
           a.register_poll_id,
           CASE WHEN    (  a.audit_status > 100 
                         AND (a.sa_reject_qty > 0 OR a.if_reject_qty > 0 OR (a.short_by_tender_over_limit > 0 AND a.media_rec_verified = 0) OR a.opening_drawer_discrepancy > 0)
                        )
                     OR (a.audit_status >= 900 AND a.valid_qty > 0)
                THEN 1 ELSE 0 END issue_flag
     FROM  work_edit_batch_list e WITH (NOLOCK), 
           audit_status a WITH (NOLOCK)
     WHERE a.store_no             = e.store_no
       AND a.register_no          = e.register_no
       AND a.sales_date           = e.transaction_date
       AND a.date_reject_id       = e.date_reject_id
       AND (a.audit_status <= 300 OR a.audit_status >= 900) -- safety check
       AND (   (status_already_existed = 1 AND (a.exception_qty > 0 OR a.translate_error_qty > 0 OR a.duplicate_qty > 0 OR a.missing_qty > 0))
            OR (    a.audit_status > 100 
                AND (a.exception_qty > 0 OR a.translate_error_qty > 0 OR a.missing_qty > 0 OR a.duplicate_qty > 0 OR a.sa_reject_qty > 0 OR a.if_reject_qty > 0 OR a.short_by_tender_over_limit > 0 OR a.opening_drawer_discrepancy > 0 OR a.unreconciled_media_present > 0)
               )
            OR ((a.audit_status >= 900 OR a.audit_status = 5) AND a.valid_qty > 0)
            OR (a.audit_status IN (100, 200, 300) AND a.valid_qty = 0 AND a.sa_reject_qty = 0)
           );

  SELECT @operation_name = 'OPEN';
  OPEN reevaluate_crsr;


  SELECT @cursor_open = 1

  WHILE 0=0
  BEGIN

  SELECT @operation_name = 'FETCH';
    FETCH reevaluate_crsr 
     INTO @store_no,
          @sales_date,
          @register_no,
          @date_reject_id,
          @audit_status,
          @exception_qty,
          @translate_error_qty,
          @missing_qty,
          @duplicate_qty,
          @unreconciled_media_present,
          @valid_qty,
          @sa_reject_qty,
          @register_poll_id,
          @issue_flag;

    IF @@fetch_status <> 0
      BREAK;
      
    SELECT @corrections = 0;
    
    SELECT @errmsg = 'Failed to determine verification status.  ',
           @operation_name = 'SELECT';
    
    IF @missing_qty > 0
    BEGIN
      SELECT @object_name = 'exception_reason';
      SELECT @missing_verified = MIN(verified)
        FROM transaction_missing th WITH (NOLOCK)
       WHERE th.sales_date  = @sales_date
         AND th.store_no    = @store_no
         AND th.register_no = @register_no;
    END;  --IF @missing_qty > 0

    IF @exception_qty > 0
    BEGIN
      SELECT @object_name = 'exception_reason';
      SELECT @exceptions_verified = MIN(verified)
        FROM transaction_header th WITH (NOLOCK),  
             exception_reason er WITH (NOLOCK)
       WHERE th.transaction_date = @sales_date
         AND th.store_no         = @store_no
         AND th.register_no      = @register_no
         AND th.date_reject_id   = @date_reject_id
         AND th.transaction_id   = er.transaction_id;
    END;  --IF @exception_qty > 0
 	  
    IF @translate_error_qty > 0
    BEGIN
SELECT @object_name = 'translate_error';
      SELECT @translate_error_verified = MIN(verified)
        FROM translate_error WITH (NOLOCK)
       WHERE transaction_date = @sales_date
         AND store_no         = @store_no
         AND register_no      = @register_no;
    END;  --IF @translate_error_qty > 0	

    IF @duplicate_qty > 0
    BEGIN
      SELECT @object_name = 'translate_error';
      SELECT @duplicate_verified = MIN(verified)
        FROM duplicate_transaction WITH (NOLOCK)
       WHERE transaction_date = @sales_date
         AND store_no         = @store_no
         AND register_no      = @register_no
         AND date_reject_id   = @date_reject_id;    
    END;
    
    IF (@translate_error_qty > 0 OR @exception_qty > 0 OR @missing_qty > 0 OR @duplicate_qty > 0)
    BEGIN
      SELECT @errmsg         = 'Failed to update audit_status (exceptions_verified).  ',
             @object_name    = 'audit_status',
             @operation_name = 'UPDATE';
      UPDATE audit_status
         SET exceptions_verified = ISNULL(@exceptions_verified,0),
             translate_error_verified = ISNULL(@translate_error_verified,0),
             missing_verified = ISNULL(@missing_verified,0),
             duplicate_verified = ISNULL(@duplicate_verified, 0)
       WHERE sales_date     = @sales_date
         AND store_no       = @store_no
         AND register_no    = @register_no
         AND date_reject_id = @date_reject_id
         AND (   exceptions_verified <> ISNULL(@exceptions_verified,0)
	      OR translate_error_verified <> ISNULL(@translate_error_verified,0)
	      OR missing_verified <> ISNULL(@missing_verified,0)
	      OR duplicate_verified <> ISNULL(@duplicate_verified, 0) );
    END; --IF (@translate_error_qty > 0 OR @exception_qty > 0 OR @missing_qty > 0 OR @duplicate_qty > 0)

    /* If audit concerns exist and if the audit_status is incorrect, or valid transactions exist but the status is unused/deleted/moved then fix it.
       This could occur due to multistream timing issues. */
    IF     @issue_flag = 0 
       AND (   (ISNULL(@exceptions_verified,0) = 0 AND @exception_qty > 0)
            OR (ISNULL(@translate_error_verified,0) = 0 AND @translate_error_qty > 0)
            OR (ISNULL(@missing_verified,0) = 0 AND @missing_qty > 0)
            OR (ISNULL(@duplicate_verified,0) = 0 AND @duplicate_qty > 0)  )
    BEGIN
      SELECT @issue_flag = 1;
    END;
    
    IF @issue_flag = 0 AND @unreconciled_media_present = 1 AND @audit_status IN (200, 300)  --if not already marked as an issue for another reason but might be an issue for unrec media reasons and status might require downgrading
    BEGIN
      IF EXISTS (SELECT 1
                   FROM media_unreconciliation mu WITH (NOLOCK)
                        INNER JOIN media_reconciliation_status ms WITH (NOLOCK)
                           ON ms.balancing_entity_id = mu.balancing_entity_id
                          AND ms.first_unreconciled_date_time is not null AND ms.unreconciled_activity_amount <> 0 
                          AND (   ABS(ms.unreconciled_activity_amount) > ms.unrec_tolerance_amount 
                               OR DATEDIFF(dd, ms.first_unreconciled_date_time, getdate()) > ms.unrec_tolerance_days) 
                  WHERE mu.store_no = @store_no
                    AND mu.register_no = @register_no
                    AND mu.transaction_date = @sales_date
                    AND mu.unrec_activity_flag > 0
                    AND (   DATEDIFF(dd, mu.transaction_date, getdate()) > ms.unrec_tolerance_days --If the unreconciled amount for the balancing entity is NOT beyond tolerance we want the store/reg/dates that are beyond tolerance days.
                         OR ABS(ms.unreconciled_activity_amount) > ms.unrec_tolerance_amount) --If the unreconciled amount for the balancing entity is beyond tolerance we want all store/reg/dates that contributed not just those that are beyond tolerance themselves  
                )
      BEGIN
        SELECT @issue_flag = 2;  --to avoid warning in process error log about downgrade when only for this reason (since this is not evaluated by trickle audit until now)
      END;
    END;

    IF (   (@audit_status >= 200 AND @issue_flag >= 1)
        OR ( (@audit_status >= 900 OR @audit_status = 5) AND (@valid_qty > 0 OR @sa_reject_qty > 0) )
       )
    -- fix integrity if audit concerns exist
    BEGIN
      SELECT @errmsg         = 'Failed to update audit_status (status fix).  ',
             @object_name    = 'audit_status',
	     @operation_name = 'UPDATE';
      UPDATE audit_status
	 SET audit_status = 100  --for missing/unused going to edited, might later move to 200
       WHERE sales_date     = @sales_date
	 AND store_no       = @store_no
	 AND register_no    = @register_no
	 AND date_reject_id = @date_reject_id;

      SELECT @corrections = 1;
    END;
    ELSE  --ELSE of IF (@audit_status >= 200 AND @issue_flag = 1) OR ( (@audit_status >= 900 OR @audit_status = 5) AND (@valid_qty > 0 OR @sa_reject_qty > 0) )
    BEGIN
      IF @audit_status IN (100, 200, 300) AND @valid_qty = 0 AND @sa_reject_qty = 0 
         AND (@audit_status <> 100 OR @issue_flag = 0)
      BEGIN
        -- Values for rprt_unsd_wrkstns:
        -- 0: Do not log missing transactions. 
        -- 1: Log server-workstation as missing (if no trnx is polled for that loop), and workstations as unused. 
        -- 2: Log server-workstation and workstations as unused. 
        -- 3: Log server-workstation and workstations as missing.
        SELECT @errmsg         = 'Failed to determine if missing registers are to be identified. ',
               @object_name    = 'ORG_CHN_WRKSTN_CNFG',
  	       @operation_name = 'SELECT';
  	IF EXISTS (
               SELECT 1
                FROM ORG_CHN_WRKSTN rg
               INNER JOIN ORG_CHN_WRKSTN_CNFG_A ca
                  ON COALESCE(rg.PRNT_WRKSTN_ID, rg.WRKSTN_ID) = ca.WRKSTN_ID	   
	         AND @sales_date >= ca.EFCTV_DATE
	         AND (@sales_date < ca.EXPRTN_DATE OR ca.EXPRTN_DATE IS NULL)
	       INNER JOIN ORG_CHN_WRKSTN_CNFG c
  	          ON ca.WRKSTN_CNFG_CODE = c.WRKSTN_CNFG_CODE
  	         AND COALESCE(c.RPRT_UNSD_WRKSTNS, 1) IN (1, 3)
               WHERE rg.ORG_CHN_NUM = @store_no
                 AND rg.WRKSTN_NUM = @register_no
                 AND (   COALESCE(c.RPRT_UNSD_WRKSTNS, 1) = 3
                      OR COALESCE(rg.PRNT_WRKSTN_ID, rg.WRKSTN_ID) = rg.WRKSTN_ID)
                     )
          SELECT @new_status = 5; 
        ELSE
          SELECT @new_status = 900; 
        
        IF @new_status = 5 AND @register_poll_id IS NOT NULL
        BEGIN
          SELECT @errmsg         = 'Failed to determine if any other registers on same loop exist. ',
                 @object_name    = 'audit_status',
  	         @operation_name = 'SELECT';
          IF EXISTS (SELECT 1 
                       FROM audit_status
                      WHERE sales_date = @sales_date
                        AND store_no       = @store_no
                        AND date_reject_id = @date_reject_id
                        AND register_no <> @register_no
                        AND (valid_qty > 0 OR sa_reject_qty > 0))
          SELECT @new_status = 900;
        END --IF @new_status = 5 AND @register_poll_id IS NOT NULL
  
        SELECT @errmsg         = 'Failed to downgrade audit_status to missing/unused.  ',
               @object_name    = 'audit_status',
	       @operation_name = 'UPDATE';
        UPDATE audit_status
	   SET audit_status = @new_status
         WHERE sales_date     = @sales_date
	   AND store_no       = @store_no
	   AND register_no    = @register_no
	   AND date_reject_id = @date_reject_id;

  SELECT @corrections = 1;
      END;  --IF @audit_status IN (100, 200, 300) AND @valid_qty = 0 AND @sa_reject_qty = 0 AND (@audit_status <> 100 OR @issue_flag = 0)
    END;  --ELSE of IF (@audit_status >= 200 AND @issue_flag = 1) OR ( (@audit_status >= 900 OR @audit_status = 5) AND (@valid_qty > 0 OR @sa_reject_qty > 0) )

    IF @issue_flag <> 2 AND @corrections = 1
    BEGIN
      SELECT @errmsg         = 'Failed to log warning that integrities in audit_status have been repaired.  ',
             @object_name    = 'audit_status',
	     @operation_name = 'process_error_log';
      INSERT INTO process_error_log (
             process_no,
             error_code,
             error_timestamp,
             process_id,
             verified,
             error_msg,
             user_id,
             memo1,
             memo2,
             memo3,
             memo_date )
      VALUES(1,
             201612,
             getdate(),
             1, -- batch_process_no
             1, -- nsb purposes
             'Edit_verify_registers_$sp has autocorrected an incorrect audit_status. ',
             null,
             CONVERT(nvarchar,@audit_status),
             CONVERT(nvarchar,@store_no),
             CONVERT(nvarchar,@register_no),
             @sales_date);
    END  --IF @issue_flag <> 2
  END -- End of re-evaluation cursor

  SELECT @errmsg = 'Failed to handle reevaluate_crsr',
         @object_name = 'reevaluate_crsr',
         @operation_name = 'CLOSE';
  CLOSE reevaluate_crsr
  SELECT @operation_name = 'DEALLOCATE';
  DEALLOCATE reevaluate_crsr

  SELECT @cursor_open = 0

  SELECT @errmsg         = 'Unable to create temp table #audit_status.  ',
         @object_name    = '#audit_status',
         @operation_name = 'CREATE';
  CREATE TABLE #audit_status (
         store_no			int           not null,
         register_no			smallint      not null,
         sales_date			smalldatetime not null,
         date_reject_id			tinyint	      not null,
         audit_status           	smallint      not null,
         valid_qty			smallint      not null,
         unreconciled_media_present	tinyint       null,
         completion_date_time		datetime      null );

  SELECT @errmsg         = 'Unable to insert #audit_status.  ',
         @object_name    = '#audit_status',
         @operation_name = 'INSERT';
  INSERT #audit_status (
         store_no,
         register_no,
         sales_date,
         date_reject_id,
         audit_status,
         valid_qty,
         unreconciled_media_present,
         completion_date_time)  
  SELECT a.store_no,
         a.register_no,
         a.sales_date,
         a.date_reject_id,
         a.audit_status,
         a.valid_qty,
         a.unreconciled_media_present,
         a.completion_date_time
    FROM work_edit_batch_list e WITH (NOLOCK), audit_status a 
   WHERE (a.audit_status = 100 OR 
          a.audit_status = 200)
     AND a.date_reject_id = 0
     AND e.date_reject_id = 0
     AND a.store_no       = e.store_no
     AND a.register_no    = e.register_no
     AND a.sales_date     = e.transaction_date
     AND a.date_reject_id = e.date_reject_id
     AND sa_reject_qty = 0
     AND if_reject_qty = 0
     AND (missing_qty                = 0 OR 
          missing_verified           = 1)
     AND (exception_qty              = 0 OR 
          exceptions_verified        = 1)
     AND (duplicate_qty              = 0 OR 
          duplicate_verified         = 1)
     AND (short_by_tender_over_limit = 0 OR 
          media_rec_verified         = 1)
     AND (opening_drawer_discrepancy = 0 OR
          media_rec_verified         = 1)
     AND (translate_error_qty        = 0 OR 
          translate_error_verified   = 1);
  SELECT @transaction_count = @@rowcount;

IF @transaction_count > 0  --i.e. if there were some audit-concern-free store/dates in the batch
BEGIN
  SELECT @errmsg = 'Unable to delete #audit_status',
         @object_name    = '#audit_status',
         @operation_name = 'DELETE';
  DELETE #audit_status -- exclude failed media rec
 FROM #audit_status st, work_rec_incomplete wr WITH (NOLOCK)
   WHERE wr.store_no = st.store_no
     AND wr.transaction_date = st.sales_date
     AND st.date_reject_id = 0;

  -- update audit_status to 200 or 300 for store-reg-dates with no audit concerns
  SELECT @errmsg         = 'Failed to handle audit_crsr',
         @object_name    = 'audit_crsr',
         @operation_name = 'DECLARE';
  DECLARE audit_crsr CURSOR FAST_FORWARD
    FOR
    SELECT store_no,
           sales_date,
           register_no,
           audit_status,
           valid_qty,
           ISNULL(unreconciled_media_present,0),
           completion_date_time
      FROM #audit_status WITH (NOLOCK)
     WHERE date_reject_id = 0
     ORDER BY store_no, sales_date, register_no;
     
  SELECT @operation_name = 'OPEN';
  OPEN audit_crsr;

  SELECT @cursor_open   = 2,
         @prev_store_no = -1;

  WHILE 1=1
  BEGIN
    SELECT @errmsg         = 'Failed to handle audit_crsr',
           @object_name    = 'audit_crsr',
           @operation_name = 'FETCH';
    FETCH audit_crsr 
     INTO @store_no,
          @sales_date,
          @register_no,
          @audit_status,
          @valid_qty,
          @unreconciled_media_present,
          @completion_date_time;

    IF @@fetch_status <> 0
      BREAK;

    SELECT @errmsg         = 'Failed to determine if store/reg/dates with unrec media beyond tolerance exist.  ',
           @object_name    = 'media_unreconciliation',
           @operation_name = 'SELECT';
    --141621
    IF @unreconciled_media_present = 1
     AND EXISTS (SELECT 1
                   FROM media_unreconciliation mu WITH (NOLOCK)
                        INNER JOIN media_reconciliation_status ms WITH (NOLOCK)
                           ON ms.balancing_entity_id = mu.balancing_entity_id
                          AND ms.first_unreconciled_date_time is not null AND ms.unreconciled_activity_amount <> 0 
                          AND (   ABS(ms.unreconciled_activity_amount) > ms.unrec_tolerance_amount 
                               OR DATEDIFF(dd, ms.first_unreconciled_date_time, getdate()) > ms.unrec_tolerance_days) 
                  WHERE mu.store_no = @store_no
                    AND mu.register_no = @register_no
                    AND mu.transaction_date = @sales_date
                    AND mu.unrec_activity_flag > 0
                    AND (   DATEDIFF(dd, mu.transaction_date, getdate()) > ms.unrec_tolerance_days --If the unreconciled amount for the balancing entity is NOT beyond tolerance we want the store/reg/dates that are beyond tolerance days.
                         OR ABS(ms.unreconciled_activity_amount) > ms.unrec_tolerance_amount) --If the unreconciled amount for the balancing entity is beyond tolerance we want all store/reg/dates that contributed not just those that are beyond tolerance themselves  
                )
    BEGIN
      CONTINUE; -- skip store/reg/date if unreconciled media is beyond tolerance.
    END;

    -- Change of store or date    
    IF ( @store_no != @prev_store_no OR @sales_date != @prev_sales_date )
    BEGIN 
      SELECT @errmsg         = 'Failed to determine if store/date media rec information.  ',
             @object_name    = 'store_audit_status',
             @operation_name = 'SELECT';	       
      SELECT @update_in_progress         = update_in_progress,
             @short_by_tender_over_limit = short_by_tender_over_limit,
             @opening_drawer_discrepancy = opening_drawer_discrepancy,
             @media_rec_verified         = media_rec_verified,
             @store_completion_date_time = completion_date_time
        FROM store_audit_status  WITH (NOLOCK)
       WHERE store_no       = @store_no
         AND sales_date     = @sales_date
         AND date_reject_id = 0;

      IF @store_no != @prev_store_no
      BEGIN
        SELECT @errmsg         = 'Failed to determine auto accept method.  ',
      @object_name    = 'ORG_CHN',
               @operation_name = 'SELECT';	       
        SELECT @autoaccept_flag = AUTO_ACPT
          FROM ORG_CHN WITH (NOLOCK)
         WHERE ORG_CHN_NUM = @store_no;

        SELECT @prev_store_no = @store_no;
  
      END;
      
      SELECT @prev_sales_date = @sales_date;

    END; -- End of Change of store

    IF @update_in_progress > 1
      CONTINUE; -- skip store if locked by a manual function

    SELECT @audit_status = 200;

    IF ( @autoaccept_flag        >= 1     AND 
         @trickle_finished_flag   = 1                      AND 
         @sales_date             <= @latest_date_to_accept AND 
         @valid_qty            >= 1 )
    BEGIN

      SELECT @closeout_exists = 0,
             @closeout_flag   = 0 
    
      IF @autoaccept_flag in (1, 2) AND @unreconciled_media_present > 0
      BEGIN
        SELECT @errmsg         = 'Failed to determine if unreconciled media is present.  ',
               @object_name    = 'media_reconciliation_status',
               @operation_name = 'SELECT';	       
        IF EXISTS (SELECT 1 FROM media_reconciliation_status m WHERE m.store_no = @store_no AND (m.register_no = @register_no OR m.register_no = 0) AND m.rec_type = 3)
           AND NOT EXISTS (SELECT 1 FROM media_reconciliation_status m, media_unreconciliation u
                            WHERE m.store_no = @store_no
     			      AND (m.register_no = @register_no OR m.register_no = 0)
     			      AND m.first_unreconciled_date_time < dateadd(hh, 6, dateadd(dd, 1, @sales_date))  --include contribution to expected of counts entered between midnight and 6AM
     			      AND (m.rec_type <> 3 OR m.unreconciled_activity_amount <> 0)
     			      AND @store_no = u.store_no 
     			      AND @register_no = u.register_no 
     			      AND @sales_date = u.transaction_date
     			      AND u.unrec_activity_flag > 0)
          SELECT @unreconciled_media_present = 0;
      END;  --in the case of FLOAT rec, check if unreconciled activity is <> 0
      
      IF ((@autoaccept_flag = 1 AND @unreconciled_media_present = 0)
           OR @autoaccept_flag = 3)
      BEGIN
        IF @default_pre_midnight_time <> 2359 OR @default_post_midnight_time <> 0
        BEGIN
          IF COALESCE(@completion_date_time, @store_completion_date_time) IS NOT NULL
            SELECT @closeout_exists = 1, @closeout_flag = 1
        END
        ELSE  --ELSE of IF i_default_pre_midnight_time <> 2359 OR i_default_post_midnight_time <> 0
	BEGIN
          SELECT @errmsg         = 'Failed to determine if closeout trans exists.  ',
                 @object_name    = 'transaction_header',
                 @operation_name = 'SELECT';	       
          IF EXISTS (SELECT 1   --- look for any closeout flag on @register
                       FROM transaction_header WITH (NOLOCK)
                      WHERE transaction_date = @sales_date
                        AND store_no = @store_no
                        AND date_reject_id = 0
                        AND register_no = @register_no
                        AND closeout_flag >= 1)
            SELECT @closeout_exists = 1, @closeout_flag   = 1;

          IF @closeout_flag = 0
          BEGIN
            IF EXISTS (SELECT 1  -- look for store closeout flag on other reg
                         FROM transaction_header WITH (NOLOCK)
                        WHERE transaction_date = @sales_date
                          AND store_no = @store_no
                          AND date_reject_id = 0
                          AND closeout_flag = 2)
              SELECT @closeout_exists = 1;
          END;
        END; --ELSE of IF @default_pre_midnight_time <> 2359 OR @default_post_midnight_time <> 0   
      END; -- @autoaccept_flag = 1 or 3
      ELSE
 BEGIN
        IF((@autoaccept_flag = 2 AND @unreconciled_media_present = 0)
           OR @autoaccept_flag = 4)
        BEGIN
          IF @default_pre_midnight_time <> 2359 OR @default_post_midnight_time <> 0
          BEGIN
            IF @store_completion_date_time IS NOT NULL
              SELECT @closeout_exists = 1
          END
          ELSE  --ELSE of IF @default_pre_midnight_time <> 2359 OR @default_post_midnight_time <> 0
          BEGIN
            SELECT @errmsg         = 'Failed to determine if store closeout trans exists.  ',
                   @object_name    = 'transaction_header',
                   @operation_name = 'SELECT';	       
            IF EXISTS (SELECT 1
                         FROM transaction_header WITH (NOLOCK)
                        WHERE transaction_date = @sales_date
                          AND store_no = @store_no
                          AND date_reject_id = 0
                          AND closeout_flag = 2 )
              SELECT @closeout_exists = 1;
          END; --ELSE of IF @default_pre_midnight_time <> 2359 OR @default_post_midnight_time <> 0
        END; -- If @autoaccept_flag = 2 or 4
      END; -- Else
                  	    
      IF @closeout_exists = 1
        SELECT @audit_status = 300;
	      
    END; -- If @autoaccept_flag >= 1 and trickle finished

    -- check that another edit stream has not started processing the store-reg-date since phase2 started
    -- Set status for all other registers done in verify_store_status
    SELECT @errmsg    = 'Failed to update audit_status',
           @object_name    = 'audit_status',
           @operation_name = 'UPDATE';
    UPDATE audit_status
       SET audit_status  = @audit_status,
           status_date   = @current_date,
           status_set_by_user_id = NULL --
      FROM audit_status a
     WHERE a.date_reject_id = 0
       AND a.audit_status <= 300 -- safety check for multistream
       AND a.store_no       = @store_no
       AND a.register_no    = @register_no
       AND a.sales_date     = @sales_date
       AND EXISTS( SELECT *
            FROM edit_store_date_list dl
            WHERE dl.store_no       = a.store_no
              AND dl.register_no    = a.register_no
              AND dl.transaction_date = a.sales_date
              AND dl.posted_flag > 0); -- not currently in progress by phase1 on another stream
  END; -- End of audit cursor

  SELECT @errmsg    = 'Failed to handle audit_crsr.  ',
         @object_name    = 'audit_crsr',
         @operation_name = 'CLOSE';
  CLOSE audit_crsr;
  SELECT @operation_name = 'DEALLOCATE';
  DEALLOCATE audit_crsr;
  SELECT @cursor_open = 0;

  SELECT @errmsg    = 'Failed to delete #audit_status.  ',
         @object_name    = '#audit_status',
         @operation_name = 'DELETE';
  DELETE #audit_status;

END --IF @transaction_count > 0  --i.e. if there were some audit-concern-free store/dates in the batch
  
  SELECT @errmsg    = 'Failed to INSERT INTO #audit_status for all store-dates in batch',
         @object_name    = '#audit_status',
         @operation_name = 'INSERT';
  INSERT INTO #audit_status 
         (store_no, register_no, sales_date, date_reject_id, audit_status, valid_qty, unreconciled_media_present)
  SELECT DISTINCT store_no, 0, transaction_date, date_reject_id, 0, 0, 0
  FROM work_edit_batch_list;
     
  -- exclude failed media rec
  SELECT @errmsg    = 'Failed to DELETE #audit_status where media rec incomplete.  ',
         @object_name    = '#audit_status',
         @operation_name = 'DELETE';  
  DELETE #audit_status
  FROM #audit_status st, work_rec_incomplete wr WITH (NOLOCK)
  WHERE st.store_no = wr.store_no
  AND wr.transaction_date = st.sales_date
  AND st.date_reject_id = 0;

  -- Set store_audit_status to match audit_status

  SELECT @errmsg    = 'Failed to handle store_crsr cursor.  ',
         @object_name    = 'store_crsr',
         @operation_name = 'DECLARE';  
  DECLARE store_crsr CURSOR FAST_FORWARD
  FOR
  SELECT store_no, sales_date, date_reject_id
  FROM #audit_status WITH (NOLOCK)
  ORDER BY store_no, sales_date, date_reject_id;
  
  SELECT @operation_name = 'OPEN';  
  OPEN store_crsr;
    
  SELECT @cursor_open = 3;
  
  WHILE 3=3
  BEGIN
    SELECT @errmsg    = 'Failed to handle store_crsr cursor.  ',
           @object_name    = 'store_crsr',
           @operation_name = 'FETCH';  
    FETCH store_crsr
     INTO @store_no, @sales_date, @date_reject_id;
    
    IF @@fetch_status <> 0
      BREAK;
      
    SELECT @errmsg    = 'Failed to execute stored proc verify_store_status_$sp.  ',
           @object_name    = 'verify_store_status_$sp',
           @operation_name = 'EXEC';  
    EXEC verify_store_status_$sp @process_id, null, @store_no, @sales_date, @date_reject_id, @errmsg OUTPUT, 1, 5

  END; -- While 3=3
  
  SELECT @errmsg    = 'Failed to handle store_crsr cursor.  ',
         @object_name    = 'store_crsr',
         @operation_name = 'CLOSE';  
  CLOSE store_crsr;
  SELECT @operation_name = 'DEALLOCATE';  
  DEALLOCATE store_crsr;
  
  SELECT @cursor_open =0;
  
  SELECT @errmsg    = 'Failed to mark process log entry as complete.  ',
         @object_name    = 'end_process_log_$sp',
         @operation_name = 'EXEC';  
  EXEC end_process_log_$sp @process_no, @process_timestamp, @transaction_count;
 
RETURN;

business_error:   /* Business Rule handler. */

  SELECT @errmsg2 = @errmsg;

  EXEC common_error_handling_$sp @process_no, @errno, @errmsg, 0, @message_id, @process_name,
   @object_name, @operation_name, 1, 1, 0, null, 0, null, null, null, null, null, null,
       0, @process_id, @user_id;
  --Note: when the exec above raises an error, that action also fires the system error trap (below)
   RETURN;
END TRY

BEGIN CATCH; -- trap system errors
  --common error handling. Appending proc name here because a rollback could occur if called within a transaction.

  SELECT @errno = ERROR_NUMBER(),
	 @errline = ERROR_LINE();

  SELECT @errmsg = CONVERT(nvarchar, @errno) + ':' + @process_name + ':' + CONVERT(nvarchar, @errline) + ':'
               + COALESCE(@errmsg, ' ') + ':' + ERROR_MESSAGE();

  --this condition will only be true when raise error in traps above fire this general catch
  IF @errmsg2 IS NOT NULL
     SELECT @errmsg = @errmsg2;

  IF @cursor_open = 1
  BEGIN
    CLOSE reevaluate_crsr
    DEALLOCATE reevaluate_crsr
  END

  IF @cursor_open = 2
  BEGIN
    CLOSE audit_crsr
    DEALLOCATE audit_crsr
  END
  
  
  IF @cursor_open = 3
  BEGIN
    CLOSE store_crsr
    DEALLOCATE store_crsr
  END

  EXEC common_error_handling_$sp @process_no, @errno, @errmsg, 0, @message_id, @process_name,
       @object_name, @operation_name, 1, 1, 0, null, 0, null, null, null, null, null, null,
       0, @process_id, @user_id;

  RETURN;
END CATCH;
```

