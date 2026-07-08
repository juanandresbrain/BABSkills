# dbo.create_register_status_$sp

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.create_register_status_$sp"]
    ORG_CHN_WRKSTN(["ORG_CHN_WRKSTN"]) --> SP
    ORG_CHN_WRKSTN_CNFG(["ORG_CHN_WRKSTN_CNFG"]) --> SP
    ORG_CHN_WRKSTN_CNFG_A(["ORG_CHN_WRKSTN_CNFG_A"]) --> SP
    audit_status(["audit_status"]) --> SP
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
    create_store_status__sp(["create_store_status_$sp"]) --> SP
    parameter_general(["parameter_general"]) --> SP
    store_audit_status(["store_audit_status"]) --> SP
    trno(["trno"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ORG_CHN_WRKSTN |
| ORG_CHN_WRKSTN_CNFG |
| ORG_CHN_WRKSTN_CNFG_A |
| audit_status |
| common_error_handling_$sp |
| create_store_status_$sp |
| parameter_general |
| store_audit_status |
| trno |

## Stored Procedure Code

```sql
CREATE proc  dbo.create_register_status_$sp 
@process_id		        binary(16),
@user_id                        int,
@store_no			int,
@register_no			smallint,
@sales_date			smalldatetime,
@current_transaction_no		trno,
@date_reject_id			tinyint OUTPUT,
@status_reject_reason		tinyint OUTPUT,
@errmsg				nvarchar(2000) OUTPUT,
@edit_timestamp			float = 0,		--0=manual functions, 9/109=move, otherwise=Edit
@store_audit_status		smallint = 0,
@valid_qty			smallint = 0,
@sa_reject_qty			smallint = 0,
@if_reject_qty			smallint = 0,
@exception_qty			smallint = 0,
@completion_date_time		datetime = NULL,
@edit_process_no		tinyint = 1

AS

/* Proc Name: create_register_status_$sp

   Description : Look for a status row for a store-reg-date and determine status.
     	If not present, then create it.
   Called by edit_header_$sp, move_register_$sp, move_reg_media_rec_$sp, and Powerbuilder. 

  -- Values for rprt_unsd_wrkstns:
  -- 0: Do not log missing transactions. 
  -- 1: Log server-workstation as missing (if no trnx is polled for that loop), and workstations as unused. 
  -- 2: Log server-workstation and workstations as unused. 
  -- 3: Log server-workstation and workstations as missing.
      
   Unicode version.

HISTORY:
Date     Name		Def# Action
May27,16 Vicci      DAOM-730 Don't change status, verified flags, short in the case of the Edit in a trickle-audit environment since the row
                             is visible to the user (not locked):  wait until counts are changed to and do status and flags at the same time.
May12,16 Vicci      DAOM-730 When try catch was introduced, it broke @errmsg = 'status already exists' causing status_already_existed to always be set
                             to false in edit store date list.  Restore the broken logic.
                             Since register_poll_id is not longer used (was a S/A 4.1 and under concept) appropriate it as an 
                             option 1 (Log parent as missing and child as unused) indicator, specifying the store/parent-reg as the match key.
                             Return register_poll_id to edit.
Apr29,16 Vicci      DAOM-672 If unaccepting a register (allowed when store isn't accepted), still set trickle in progress flag.
May05,15 Vicci    TFS-119660 When a store audit status record is missing, even if in move, in order to avoid integrity which otherwise results silently
                             (namely audit_status record with no corresponding store_audit_status record) allow the proc to error out 
                             so that issue is known and addressed rather than hidden.
Dec04,14 Paul      TFS-94103 use try catch
Jul10,14 Vicci     TFS-37538 Make sure audit status does not get left at 902 when called by archive transaction modify.
Sep09,05 Paul        DV-1312 apply 42694 to SA5, corrected comments
Aug10,05 Paul          57984 log sa reject for invalid date when store and date are both invalid (SA5 business rule)
Feb07,05 Paul        DV-1203 remove reference to sa reject type 10 since it should never happen (store would also be completed)
Nov16,04 Maryam      DV-1167 check for ACTV flag.
Sep28,04 David       DV-1146 Use user_id instead of user_name.
May14,04 Maryam      DV-1071 Hard code register_poll_id as this column does not exist in new ORG_CHN_WRKSTN table,
                             receive @process_id and @user_name and pass it to the sub procs.
Oct18,04 Maryam        42694 Remove @status_reject_reason = 10 and 12
Oct29,02 Winnie	     1-FGESD Add logic for Moved Invalid Register.
May31,02 Winnie      1-DDHQ0 setting the correct value to @store_audit_status when it is null for Sybase 12.5.
Jan30,02 Henry	     AW-7611 Keep original value of media_rec_verified flag in audit_status 
			     if store/reg/date is edited again. 
			     Do NOT reset media_rec_verified = 0 if audit_status entry already exists.
Dec20,01 Phu            8575 Logical trading dates, error handling
Sep19,01 Paul		8753 If date is invalid and reg is invalid, report rejects as invalid date
Jun19,01 ShuZ		8153 Modify error message in order to make difference
May02,01 Sab		7600 Try one more time when we get the duplicate key when insert audit_status
Apr20,01 David M	7587 Missing transactions by transaction Series version 1.0, removing
			     code for last_transaction_no.
Feb15,01 Paul		7091 Correctly check for nonexistent register.	
			     Register could exist but have a null register_poll_id.
Jan30,01 Henry		6765 Commented out redundant code for calculating missing trxns.
Jan09,01 Paul		7153 Do not unaccept register unless store is not yet accepted
Nov14,00 Paul		6948 Ensure that register_poll_id is set
Oct11,00 Paul		6825 Call create_store_status_$sp if store_audit_status does not exist
Oct03,00 Paul		6776 Pass back error message to indicate that status already existed
Feb11,00 Daphna F	5904 Included edit_timestamp = 109 for move
Sep29,99 Paul		5309 Reset verified flags to zero when audit_status already exists.
Jun08,99 Louise M.	4526 Added code to update trickle_in_progres_flag in table audit_status 
			     when trickle edit is used.
Feb15,99 Paul S
Nov07,96 Paul S		n/a  Creation
*/

DECLARE @audit_status			smallint,
	@dayend_in_progress		tinyint,
	@edited_date			smalldatetime,
	@errmsg2		 	nvarchar(2000),
	@errline			int,
	@errno				int,
	@media_short			money,
	@message_id			int,
	@missing_qty			numeric(12,0),
	@object_name			nvarchar(255),
	@operation_name			nvarchar(100),
	@orig_audit_status		smallint,
	@prev_transaction_no		trno,
	@prev_trickle_flag		tinyint,
	@prior_sales_date		smalldatetime,
	@process_name			nvarchar(100),
	@process_no			smallint,
	@register_poll_id		nvarchar(15),
	@rows				int,
	@status_row_exists		int,
	@trickle_in_progress_flag	tinyint,
	@trickle_polling_flag		tinyint,
	@orig_store_audit_status	smallint,
	@status_already_existed 	tinyint,
	@prnt_wrkstn_id                 binary(16),
	@wrkstn_id                      binary(16),
	@edit_trickle_audit		tinyint,  --process is Edit and environment is Trickle Audit
	@rprt_unsd_wrkstns		tinyint;

SELECT 	@process_name = 'create_register_status_$sp',
	@message_id = 201068,
	@edit_trickle_audit = 0;

BEGIN TRY
   SELECT @errmsg = 'Failed to read parameter_general.',
          @object_name = 'parameter_general',
          @operation_name = 'SELECT';	
SELECT @trickle_polling_flag = ISNULL(trickle_polling_flag,0)
  FROM parameter_general;
  

SELECT @errmsg = 'Failed to read audit_status.',
       @object_name = 'audit_status';
SELECT @orig_audit_status = audit_status,
       @media_short = media_short,
       @edited_date = edited_date,
       @prev_trickle_flag = ISNULL(trickle_in_progress_flag,0),
       @register_poll_id = register_poll_id
  FROM audit_status
 WHERE sales_date = @sales_date
   AND store_no = @store_no
   AND register_no = @register_no
   AND date_reject_id = @date_reject_id;
SELECT @status_row_exists = @@rowcount;

--Note : @edit_timestamp is equal to 9 or 109  when coming from the move  
IF @trickle_polling_flag >= 2  AND (@edit_timestamp > 0 AND @edit_timestamp NOT IN (9,109))
 SELECT  @trickle_in_progress_flag = 1,
         @edit_trickle_audit = 1;
ELSE
 SELECT  @trickle_in_progress_flag = 0;

--Keep original trickle flag for manual functions. 
IF @status_row_exists != 0 AND (@edit_timestamp = 0 OR @edit_timestamp IN (9,109) )
 SELECT @trickle_in_progress_flag = @prev_trickle_flag;

IF @edit_trickle_audit = 1 --For trickle audit Edit will only update status when quantities/amounts (valid, reject, short, etc) are updated  DAOM-730
BEGIN  

  IF @status_row_exists = 0  --i.e. if entry doesn't exist and status has not been set to invalid store/reg
    SELECT @audit_status = 900;
  ELSE
    SELECT @audit_status = @orig_audit_status;
END
ELSE --ELSE of IF @edit_trickle_audit = 1
BEGIN
  IF (@status_row_exists = 0 OR @orig_audit_status IN (5, 200, 900, 901, 902, 903, 904, 905, 906))
    SELECT @audit_status = 100;
  ELSE
    SELECT @audit_status = @orig_audit_status;
END --ELSE of IF @edit_trickle_audit = 1

SELECT @orig_store_audit_status = NULL,
       @errmsg = 'Failed to select from store_audit_status (1).',
       @object_name = 'store_audit_status',
       @operation_name = 'SELECT';
SELECT @orig_store_audit_status = store_audit_status
  FROM store_audit_status
 WHERE @store_no = store_no
   AND @sales_date = sales_date
   AND @date_reject_id = date_reject_id;

IF COALESCE(@store_audit_status, 0) = 0
  SELECT @store_audit_status = @orig_store_audit_status;

/* safety check: if null it means there is a bug in the calling procedure, but
   compensate by creating store_audit_status. */

IF @orig_store_audit_status IS NULL /* then */
BEGIN
       SELECT @object_name = 'create_store_status_$sp',
              @operation_name = 'EXECUTE',
              @errmsg = 'Failed to exec create_store_status_$sp.';
    EXEC create_store_status_$sp @process_id, @user_id, @store_no, @sales_date,
      @date_reject_id OUTPUT, @status_reject_reason OUTPUT,
      @errmsg OUTPUT, @edit_timestamp;

      SELECT @errmsg = 'Failed to select from store_audit_status (2).',
             @object_name = 'store_audit_status',
             @operation_name = 'SELECT';
    SELECT @orig_store_audit_status = store_audit_status
      FROM store_audit_status
     WHERE @store_no = store_no
       AND @sales_date = sales_date
       AND @date_reject_id = date_reject_id;
       
    IF @orig_store_audit_status IS NULL
    BEGIN
      SELECT @errmsg = 'Failed to create missing store_audit_status record.';
      GOTO business_error;
    END;
    ELSE
      SELECT @store_audit_status = @orig_store_audit_status;
END;

IF @store_audit_status != 7
BEGIN /* check whether store/reg is valid */
  IF @audit_status = 7 --store/date now corrected --Should never happen since create store status should leave it invalid if it started off that way until fix-invalid moves it.
    SELECT @audit_status = 100;

  SELECT @object_name = 'ORG_CHN_WRKSTN',
         @operation_name = 'SELECT',
         @errmsg = 'Failed to determine parent workstation.  ';
  SELECT @prnt_wrkstn_id = COALESCE(PRNT_WRKSTN_ID, WRKSTN_ID),
         @wrkstn_id = WRKSTN_ID
    FROM ORG_CHN_WRKSTN 
   WHERE ORG_CHN_NUM = @store_no
     AND WRKSTN_NUM = @register_no
     AND ACTV = 1;
     
  IF @prnt_wrkstn_id IS NULL  
  BEGIN -- register does not exist
     IF @status_reject_reason = 0 -- not invalid date
       SELECT @status_reject_reason = 1;

     IF @edit_timestamp = 0 -- manual add
       BEGIN
        SELECT @status_reject_reason = 1;
        RETURN;
       END;

     SELECT @audit_status = 8,
            @errmsg = 'Failed to update store_audit_status.',
            @object_name = 'store_audit_status',
            @operation_name = 'UPDATE';

     UPDATE store_audit_status
       SET store_audit_status = 8, -- invalid register
           trickle_in_progress_flag = @trickle_in_progress_flag
      WHERE store_no = @store_no
        AND sales_date = @sales_date
        AND date_reject_id = @date_reject_id
        AND store_audit_status <> 5;  --missing
  END; --IF @prnt_wrkstn_id IS NULL, i.e. register does not exist
END; --IF @store_audit_status != 7
ELSE  --ELSE of IF @store_audit_status != 7, i.e. store does not exit
BEGIN 
   SELECT @audit_status = @store_audit_status;
   IF @status_reject_reason = 0 -- set to invalid store if not also an invalid date
     SELECT @status_reject_reason = 7;
END;  --ELSE of IF @store_audit_status != 7, i.e. store does not exit

IF (@edit_timestamp = 0 AND @status_reject_reason != 0)
  RETURN;

IF (@edit_timestamp IN (9,109) AND @status_reject_reason NOT IN (0, 99))
  RETURN;

IF @status_row_exists = 0  --Note:  should already be there (except for bad dates) because edit_missing_reg_$sp runs first.
BEGIN

  IF @prnt_wrkstn_id IS NOT NULL
  BEGIN

    SELECT @errmsg = 'Failed to determine loop name for case when option to log parent as missing and child as unused is selected.  ',
           @object_name = 'ORG_CHN_WRKSTN_CNFG',
           @operation_name = 'SELECT'
    SELECT @register_poll_id = MAX(RIGHT ('0000000000' + CONVERT(nvarchar, rg.ORG_CHN_NUM),10) + RIGHT ('00000' + CONVERT(nvarchar, rg.WRKSTN_NUM),5)),
           @rprt_unsd_wrkstns = MIN(COALESCE(c.RPRT_UNSD_WRKSTNS, 1))
      FROM ORG_CHN_WRKSTN rg WITH (NOLOCK)
           INNER JOIN ORG_CHN_WRKSTN_CNFG_A ca WITH (NOLOCK)
              ON @prnt_wrkstn_id = ca.WRKSTN_ID	   
	     AND @sales_date >= ca.EFCTV_DATE
	     AND (@sales_date < ca.EXPRTN_DATE OR ca.EXPRTN_DATE IS NULL)
	   INNER JOIN ORG_CHN_WRKSTN_CNFG c WITH (NOLOCK)
  	      ON ca.WRKSTN_CNFG_CODE = c.WRKSTN_CNFG_CODE
  	     AND COALESCE(c.RPRT_UNSD_WRKSTNS, 1) IN (1, 3)
     WHERE rg.WRKSTN_ID = @prnt_wrkstn_id;
     
    IF @rprt_unsd_wrkstns <> 1 --1: Log server-workstation as missing (if no trnx is polled for that loop), and workstations as unused. 
      SELECT @register_poll_id = NULL; 

  END;  --IF @prnt_wrkstn_id IS NOT NULL

  IF @edit_trickle_audit = 1 AND @audit_status = 900
  BEGIN
    IF @date_reject_id = 0
    BEGIN
      IF @rprt_unsd_wrkstns = 3
        SELECT @audit_status = 5;
      ELSE  --ELSE of IF @rprt_unsd_wrkstns = 3
      BEGIN
        IF @rprt_unsd_wrkstns = 1 AND @wrkstn_id = @prnt_wrkstn_id
        BEGIN
          SELECT @errmsg = 'Failed to determine if other registers on same loop exist with data for case when option to log parent as missing and child as unused is selected.  ',
                 @object_name = 'audit_status',
                 @operation_name = 'SELECT';
          IF NOT EXISTS (SELECT 1 
                           FROM audit_status 
                          WHERE store_no = @store_no 
                            AND sales_date = @sales_date 
                            AND date_reject_id = @date_reject_id 
                            AND register_poll_id = @register_poll_id
                            AND (valid_qty > 0 OR sa_reject_qty > 0))
            SELECT @audit_status = 5;
          
          IF @audit_status = 5
          BEGIN
            SELECT @errmsg = 'Failed to set store status to missing. ',
                   @object_name = 'store_audit_status',
                   @operation_name = 'UPDATE';
            UPDATE store_audit_status
               SET store_audit_status = 5,
                   store_status_date = getdate()
             WHERE store_no = @store_no 
               AND sales_date = @sales_date 
               AND date_reject_id = @date_reject_id
               AND store_audit_status IN (100, 200, 300, 901);
          END;  --IF @audit_status = 5
        END;  --IF @rprt_unsd_wrkstns = 1 AND @wrkstn_id = @prnt_wrkstn_id                                   
      END;  --ELSE of IF @rprt_unsd_wrkstns = 3
    END;  --IF @date_reject_id = 0
    ELSE  --ELSE of IF @date_reject_id = 0
    BEGIN
      SELECT @audit_status = 100;
    END;  --ELSE of IF @date_reject_id = 0
  END;  --IF @edit_trickle_audit = 1 AND i_audit_status = 900

  IF @edit_timestamp > 109
    SELECT @edited_date = getdate();
  ELSE
    SELECT @edited_date = NULL;

  SELECT @errmsg = 'Failed to insert audit_status (1).',
         @object_name = 'audit_status',
         @operation_name = 'INSERT',
         @errno = 0;
   BEGIN TRY
    INSERT audit_status (
	store_no,
	register_no,
	sales_date,
	date_reject_id,
	audit_status,
	status_date,
	status_set_by_user_id,
	valid_qty,
	sa_reject_qty,
	if_reject_qty,
	exception_qty,
	media_short,
	register_poll_id,
	edited_date,
	trickle_in_progress_flag,
	completion_date_time )
     VALUES (
	@store_no,
	@register_no,
	@sales_date,
	@date_reject_id,
	@audit_status,
	getdate(),
	NULL,
	@valid_qty,
	@sa_reject_qty,
	@if_reject_qty,
	@exception_qty,
	0,
	@register_poll_id,  --if using option 1 (log parent as missing child as unused) should begin store/parent-reg, otherwise should be null
	@edited_date,
	@trickle_in_progress_flag,
	@completion_date_time );
   END TRY
   BEGIN CATCH;
     SELECT @errno = ERROR_NUMBER(),
            @errline = ERROR_LINE();

     SELECT @errmsg = CONVERT(nvarchar, @errno) + ':' + @process_name + ':' + CONVERT(nvarchar, @errline) + ':'
               + 'Failed to insert audit_status (1).' + ':' + ERROR_MESSAGE();
   END CATCH;
   IF @errno NOT IN (0, 2601) -- skip possible duplicate error caused by multistream timing
      GOTO business_error;

   IF @edit_timestamp > 0
   BEGIN
     IF LEN(@register_poll_id) = 15 SELECT @errmsg = 'register_poll_id=' + @register_poll_id
     
     RETURN;
   END;

   SELECT @status_reject_reason = 99; /* indicates that row was created */
   RETURN;
  END; /* @status_row_exists = 0 */

ELSE /* Audit_status already exists */
  BEGIN
   SELECT @status_already_existed = 1
   
   IF @audit_status = 8
     BEGIN
      SELECT @status_reject_reason = 1;

      IF @edit_timestamp = 0
      BEGIN
        IF @status_already_existed = 1 SELECT @errmsg = 'status already exists';
        RETURN;
      END
     END;

   IF (@audit_status = 100 AND @edit_timestamp > 0)
     IF @edited_date IS NULL OR DATEADD(dd, 1, @edited_date) < getdate() /* orig edited_date is old */
        SELECT @edited_date = getdate();

   IF (@audit_status < 300 OR @audit_status >= 900) AND @edit_timestamp > 0  --Edit or Move
   BEGIN
     IF @edit_trickle_audit = 0
     BEGIN
       SELECT @errmsg = 'Failed to update audit_status. ',
              @object_name = 'audit_status',
              @operation_name = 'UPDATE';
       UPDATE audit_status
          SET audit_status = @audit_status,
              media_short = ISNULL(@media_short, 0),
              status_date = getdate(),
              edited_date = @edited_date,
              trickle_in_progress_flag = @trickle_in_progress_flag,
              exceptions_verified = 0,	-- Dev AW-7611. Removed media_rec_verified = 0.
              duplicate_verified = 0,
              translate_error_verified = 0,
              missing_verified = 0,
              register_poll_id = COALESCE(@register_poll_id, register_poll_id),
              completion_date_time = ISNULL(@completion_date_time, completion_date_time)
        WHERE @sales_date = sales_date
          AND @store_no = store_no
          AND @register_no = register_no
          AND @date_reject_id = date_reject_id;
     END  --IF @edit_trickle_audit = 0
     ELSE
     BEGIN  --ELSE of IF @edit_trickle_audit = 0
       --Don't change verified flags / short for trickle audit Edit:  they will be set if/when counts are changed.
       SELECT @errmsg = 'Failed to update audit_status (Edit in trickle audit environment). ',
              @object_name = 'audit_status',
              @operation_name = 'UPDATE';
       UPDATE audit_status
          SET audit_status = @audit_status,
	      status_date = getdate(),
	      edited_date = @edited_date,
	      trickle_in_progress_flag = @trickle_in_progress_flag,
	      register_poll_id = COALESCE(@register_poll_id, register_poll_id),
	      completion_date_time = COALESCE(@completion_date_time, completion_date_time)
        WHERE sales_date = @sales_date
          AND store_no = @store_no
          AND register_no = @register_no
          AND date_reject_id = @date_reject_id;
     END;  --ELSE of IF @edit_trickle_audit = 0
        
     IF @status_already_existed = 1 
     BEGIN
       SELECT @errmsg = 'status already exists';
       IF LEN(@register_poll_id) = 15 
         SELECT @errmsg = @errmsg + ' register_poll_id=' + @register_poll_id;
     END;
     ELSE
     BEGIN
       IF LEN(@register_poll_id) = 15 
         SELECT @errmsg = 'register_poll_id=' + @register_poll_id;
     END;

    RETURN;
   END; -- If @audit_status < 300 OR @audit_status >= 900 ...

   IF (@audit_status < 300 OR @audit_status >= 900)
      AND @edit_timestamp = 0
   BEGIN
       SELECT @errmsg = 'Failed to update audit_status for manual functions other than move.  ',
              @object_name = 'audit_status',
              @operation_name = 'UPDATE';
     UPDATE audit_status
        SET audit_status = @audit_status,
            status_date = getdate(),
            exceptions_verified = 0 	-- Dev AW-7611. Removed media_rec_verified = 0.
      WHERE @sales_date = sales_date
        AND @store_no = store_no
        AND @register_no = register_no
        AND @date_reject_id = date_reject_id;  
        
     IF @status_already_existed = 1 SELECT @errmsg = 'status already exists';
     
     RETURN;
   END; -- If @audit_status < 300 OR @audit_status >= 900 ...

  END; -- Else (status exists)


IF @audit_status >= 300  /* register already accepted/completed */
  BEGIN
       SELECT @errmsg = 'Failed to select store_audit_status (3)',
              @object_name = 'store_audit_status',
              @operation_name = 'SELECT';
   SELECT @orig_audit_status = store_audit_status
     FROM store_audit_status 
    WHERE store_no = @store_no
      AND sales_date = @sales_date 
      AND date_reject_id = 0;

   IF @orig_audit_status >= 300 AND @orig_audit_status <= 899 AND @date_reject_id > 0
   BEGIN
     IF @status_already_existed = 1 
     BEGIN
       SELECT @errmsg = 'status already exists';
       IF LEN(@register_poll_id) = 15 
         SELECT @errmsg = @errmsg + ' register_poll_id=' + @register_poll_id;
     END;
     ELSE
     BEGIN
       IF LEN(@register_poll_id) = 15 
         SELECT @errmsg = 'register_poll_id=' + @register_poll_id;
     END;

     RETURN; -- date_reject_id was already bumped by create_store_status_$sp
   END;
   
   /* Allow edit to unaccept reg as long as the store has not yet been accepted/completed */
   IF @audit_status = 300 AND @edit_timestamp > 200 AND @date_reject_id = 0
      AND (@orig_audit_status < 300 OR @orig_audit_status >= 900)
   BEGIN  -- register already accepted but store is not
     SELECT @errmsg = 'Failed to update audit_status (2)',
            @object_name = 'audit_status',
            @operation_name = 'UPDATE';
     UPDATE audit_status
        SET audit_status = CASE WHEN @edit_trickle_audit = 0 THEN 100 ELSE 200 END,
            trickle_in_progress_flag = @trickle_in_progress_flag,
	    completion_date_time = ISNULL(@completion_date_time, completion_date_time)
      WHERE sales_date = @sales_date 
        AND store_no = @store_no 
        AND register_no = @register_no 
        AND date_reject_id = @date_reject_id;
      
     IF @status_already_existed = 1 
     BEGIN
       SELECT @errmsg = 'status already exists';
       IF LEN(@register_poll_id) = 15 
         SELECT @errmsg = @errmsg + ' register_poll_id=' + @register_poll_id;
     END;
     ELSE
     BEGIN
       IF LEN(@register_poll_id) = 15 
         SELECT @errmsg = 'register_poll_id=' + @register_poll_id;
     END;
      
     RETURN;
   END;

   IF @edit_timestamp = 0  
   BEGIN
     IF @status_already_existed = 1 SELECT @errmsg = 'status already exists';
     RETURN;
   END;

    /* Edit: create new rows in store_audit_status and audit_status
       when store is already accepted/completed */
       SELECT @errmsg = 'Failed to read store_audit_status (4)',
              @object_name = 'store_audit_status',
              @operation_name = 'SELECT';
    SELECT @date_reject_id = ISNULL(MAX(date_reject_id),0)
      FROM store_audit_status
     WHERE sales_date = @sales_date
       AND store_no = @store_no;

    IF @date_reject_id < 255
      SELECT @date_reject_id = @date_reject_id + 1;

       SELECT @object_name = 'create_store_status_$sp',
              @operation_name = 'EXECUTE',
              @errmsg = 'Failed to exec create_store_status_$sp.';
    EXEC create_store_status_$sp @process_id, @user_id, @store_no, @sales_date,
      @date_reject_id OUTPUT, @status_reject_reason OUTPUT,
      @errmsg OUTPUT, @edit_timestamp;

       SELECT @errmsg = 'Failed to insert audit_status (2).',
              @object_name = 'audit_status',
              @operation_name = 'INSERT',
              @errno = 0;
    BEGIN TRY
    INSERT audit_status (
	store_no,
	register_no,
	sales_date,
	date_reject_id,
	audit_status,
	status_date,
	status_set_by_user_id,
	media_short,
	register_poll_id,
	trickle_in_progress_flag,
	completion_date_time )
    VALUES (
	@store_no,
	@register_no,
	@sales_date,
	@date_reject_id,  --bad date
	100,
	getdate(),
	NULL,
	0,
	@register_poll_id,
	@trickle_in_progress_flag,
	@completion_date_time);
    END TRY
    BEGIN CATCH
     SELECT @errno = ERROR_NUMBER(),
            @errline = ERROR_LINE();

     SELECT @errmsg = CONVERT(nvarchar, @errno) + ':' + @process_name + ':' + CONVERT(nvarchar, @errline) + ':'
               + 'Failed to insert audit_status (2).' + ':' + ERROR_MESSAGE();
    END CATCH;
    IF @errno NOT IN (0, 2601) -- skip possible duplicate error caused by multistream timing
      GOTO business_error;

  END; /* If @audit_status >= 300 */

  IF @status_already_existed = 1 
  BEGIN
    SELECT @errmsg = 'status already exists';
    IF LEN(@register_poll_id) = 15 
      SELECT @errmsg = @errmsg + ' register_poll_id=' + @register_poll_id;
  END;
  ELSE
  BEGIN
    IF LEN(@register_poll_id) = 15 
      SELECT @errmsg = 'register_poll_id=' + @register_poll_id;
  END;

RETURN;


business_error:   /* Business Rule handler. */

	SELECT @errmsg2 = @errmsg;

	/* Could include similar cleanup code to system error trap when needed (example is from move_store_$sp).
	   However, could also exclude the cleanup code here since the outer system error catch should fire again after the exec below. */

	EXEC common_error_handling_$sp 4, @errno, @errmsg, 0, @message_id, 
	@process_name, @object_name, @operation_name, 1, @edit_process_no,
	0, null, 0, null, null, null, null, null, null, 0, @process_id, @user_id;
	  /* Note: when the exec above raises an error, that action also fires the system error trap (below) */
	RETURN;
END TRY

BEGIN CATCH; -- trap system errors
    /* common error handling. Appending proc name here because a rollback could occur if called within a transaction. */

        SELECT @errno = ERROR_NUMBER(),
		@errline = ERROR_LINE();

        SELECT @errmsg = CONVERT(nvarchar, @errno) + ':' + @process_name + ':' + CONVERT(nvarchar, @errline) + ':'
               + COALESCE(@errmsg, ' ') + ':' + ERROR_MESSAGE();

	 /* this condition will only be true when raise error in traps above fire this general catch */
	IF @errmsg2 IS NOT NULL
	  SELECT @errmsg = @errmsg2;
	  
	EXEC common_error_handling_$sp 4, @errno, @errmsg, 0, @message_id, 
	@process_name, @object_name, @operation_name, 1, @edit_process_no,
	0, null, 0, null, null, null, null, null, null, 0, @process_id, @user_id;

	RETURN;
END CATCH;
```

