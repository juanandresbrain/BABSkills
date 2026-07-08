# dbo.edit_post_void_$sp_10052010

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.edit_post_void_$sp_10052010"]
    Ex_Queue(["Ex_Queue"]) --> SP
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
    create_if_details_move__sp(["create_if_details_move_$sp"]) --> SP
    edit_store_date_list(["edit_store_date_list"]) --> SP
    if_rejection_reason(["if_rejection_reason"]) --> SP
    if_transaction_header(["if_transaction_header"]) --> SP
    interface_control(["interface_control"]) --> SP
    media_parameter_selection(["media_parameter_selection"]) --> SP
    parameter_general(["parameter_general"]) --> SP
    transaction_header(["transaction_header"]) --> SP
    transaction_line(["transaction_line"]) --> SP
    transl_post_void_detail(["transl_post_void_detail"]) --> SP
    work_if_header(["work_if_header"]) --> SP
    work_pv_media_rec(["work_pv_media_rec"]) --> SP
    work_tran_header_edit(["work_tran_header_edit"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Ex_Queue |
| common_error_handling_$sp |
| create_if_details_move_$sp |
| edit_store_date_list |
| if_rejection_reason |
| if_transaction_header |
| interface_control |
| media_parameter_selection |
| parameter_general |
| transaction_header |
| transaction_line |
| transl_post_void_detail |
| work_if_header |
| work_pv_media_rec |
| work_tran_header_edit |

## Stored Procedure Code

```sql
create proc [dbo].[edit_post_void_$sp_10052010] 
@process_id      binary(16),
@user_id         int,
@errmsg          varchar(255) OUTPUT,
@edit_timestamp  float,
@edit_process_no tinyint = 1

AS

/* Proc name: edit_post_void_$sp
   Desc : flag post voided transactions.
          Called by edit_post_$sp.

 HISTORY :                  
Date     Name		Def# Desc
Dec05,08 Paul          87777 Refix to avoid error, code reviewed
Jul31,08 Paul          87777 uplift 103326 to SA5
Apr05.07 Daphna      DV-1360 uplift 1-3MN9A7	
Dec07,06 Paul        DV-1347 corrected create table, uplift 1-34SQGL to SA5
Oct25,06 Phu           77931 Fix outer join for SQL 2005 Mode 90.
Jul31,06 Tim           69753 Uplift defect 1-3474TN to SA5
Aug25,05 Paul          59056 populate work_pv_media_rec
Jun21,05 Paul        DV-1282 return earlier if no successful post voids exist
Apr29,05 Paul        DV-1234 expand transaction_id to use tran_id_datatype
Dec14,04 Maryam      DV-1191 Improve performance. Removed Eastbourne ELP logic due to interface_id conflict.
Sep23,04 David       DV-1146 uplift 1-1AEKAS to SA5. Removed obsolete code.
May07,04 Maryam      DV-1071 Receive @process_id and @user_name and pass it to the sub procs
Jul31,08 Vicci/Paul   103326 Handle new transaction_void_flag 10 (Post-voiding reversal if original transaction not found else Post-voiding)
Mar23.07 Daphna     1-3MN9A7 Ensure postvoiding txns from other batch match on transaction_series	
Apr24,06 Daphna     1-34SQGL Transactions do not get postvoided if they are after closeout and
                             moved to next business date
Aug15,05 Daphna     1-3474TN reverse media rec effect of post-voided txns
May30,05 David      1-1AEKAS Set effective_date to entry_date_time.
Apr24,03 Paul        1-KO2HY populate till_no
Jul23,02 Paul        1-E7L7M populate key_11 in Ex_Queue with entry_date_time
Nov26,01 Winnie	     1-969YY Add logic for R3 error handling to pass @edit_process_no
Nov01,01 ShuZ	        8900 TRANSL edit changes for Sybase
Jul25,01 David C        8413 Add transaction_id to if_transaction_header
Apr23,01 David M 	7589 Missing transactions by transaction series Version 1.0
Sep15,00 Paul S		6724 Do not check for transaction_series = blank on voided trans
Jul07,00 Louise M       6448 Moved the DELETE of interface_control AFTER the insert into 
                             Ex_Queue which is using that table.
Mar29,00 Paul S		6091 Ignore transaction_series on voiding trans
				when looking for trans to void.
Mar07,00 Paul S		5692 avoid interface rejects on trickle voided transactions
Jan06,00 Paul S		5782 make Eastbourne logic consistent with Oracle
Sep09,99 Daphna 	5280 insert extra line only if interface_id 20 has update timing !=0 	
Sep07,99 Paul S		5279 set source_process_no = 1
Mar15,99 Louise M.	4346 To switch the DELETE interface_control code with the INSERT   
     	                     if_interface_control code towards the end of the procedure.                 
Dec18,98 Paul S.	n/a				                                   
         Paul		author
*/                                   

DECLARE @errno			int,
	@post_void_qty		int,
	@retry			tinyint,
	@rows			int,
	@rows_inserted		int,	
	@rows_deleted		int,	
	@rows_prev_day		int,
	@trickle_polling_flag	tinyint,
	@message_id		int,	
	@object_name		varchar(255),	
	@operation_name		varchar(100),
	@process_name		varchar(100),
	@special_void_rows	int     	

SELECT @retry = 0,
	@process_name = 'edit_post_void_$sp',
	@message_id = 201068,
	@special_void_rows = 0 	

SELECT @post_void_qty = ISNULL(COUNT(store_no),0)
  FROM transl_post_void_detail WITH (NOLOCK)
 WHERE post_void_successful = 1
   AND post_voided_trans_no >= 0

IF @post_void_qty = 0
  RETURN

SELECT @trickle_polling_flag = ISNULL(trickle_polling_flag,0)
  FROM parameter_general

CREATE TABLE #work_voids_edit(
	store_no int not null,
	post_voided_register smallint not null,
	transaction_date smalldatetime not null,
	transaction_series char(1) not null,
	post_voided_trans_no int not null,
	transaction_void_flag smallint null,
	post_voided_transaction_id numeric(14,0) null) -- tran_id_datatype
SELECT @errno = @@error
IF @errno != 0
  BEGIN
   SELECT @errmsg = 'Failed to create table #work_voids_edit',
          @object_name = '#work_voids_edit',
          @operation_name = 'CREATE TABLE'   
   GOTO error
  END

CREATE TABLE #work_tran_void(
       transaction_id numeric(14,0) not null, -- tran_id_datatype
       transaction_void_flag smallint not null,
       entry_date_time datetime not null,
       transaction_date smalldatetime not null,
       sa_rejection_flag tinyint not null)  
SELECT @errno = @@error
IF @errno != 0
  BEGIN
   SELECT @errmsg = 'Failed to create table #work_tran_void',
          @object_name = '#work_tran_void',
          @operation_name = 'CREATE TABLE'   
   GOTO error
  END  

CREATE TABLE #work_special_post_void(
	store_no			int not null,
	post_voided_register		smallint not null,
	transaction_date		smalldatetime not null,
	transaction_series		char(1) not null,
	post_voided_trans_no		int not null,
	transaction_id			numeric(14,0) not null, -- tran_id_datatype
	transaction_void_flag		smallint not null,
	post_voiding_transaction_id	numeric(14,0) null, -- tran_id_datatype
	post_voiding_trans_void_flag	smallint null,
	current_batch_flag		tinyint not null)
SELECT @errno = @@error
IF @errno != 0
  BEGIN
   SELECT @errmsg = 'Failed to create table #work_special_post_void',
          @object_name = '#work_special_post_void',
          @operation_name = 'CREATE TABLE'   
   GOTO error
  END 

CREATE TABLE #transl_post_void_detail(
	store_no			int not null,
	register_no			smallint not null,
	entry_date_time			datetime not null,
	transaction_series		char(1) not null,
	transaction_no			int not null,
	line_id				numeric(5,0) not null,
	post_voided_register		smallint not null,
	post_voided_trans_no		int not null,
	post_void_successful		tinyint not null,
	post_void_reason_code		smallint null,
	row_sequence_no			numeric(12,0) not null,
	transaction_date		smalldatetime null,
	post_voiding_transaction_id	numeric(14,0) null, -- tran_id_datatype
	post_voiding_trans_void_flag	smallint null)
SELECT @errno = @@error
IF @errno != 0
  BEGIN
   SELECT @errmsg = 'Failed to create table #transl_post_void_detail',
          @object_name = '#transl_post_void_detail',
          @operation_name = 'CREATE TABLE'   
   GOTO error
  END

-- get list of all post voiding lines that have a matching header entry

INSERT #transl_post_void_detail(
	store_no,
	register_no,
	entry_date_time,
	transaction_series,
	transaction_no,
	line_id,
	post_voided_register,
	post_voided_trans_no,
	post_void_successful,
	post_void_reason_code,
	row_sequence_no,
	transaction_date,
	post_voiding_transaction_id,
	post_voiding_trans_void_flag)
SELECT pv.store_no,
	pv.register_no,
	pv.entry_date_time,
	pv.transaction_series,
	pv.transaction_no,
	pv.line_id,
	pv.post_voided_register,
	pv.post_voided_trans_no,
	pv.post_void_successful,
	pv.post_void_reason_code,
	pv.row_sequence_no,
	wh.transaction_date,
	wh.transaction_id,
	wh.transaction_void_flag
  FROM transl_post_void_detail pv WITH (NOLOCK)
    JOIN work_tran_header_edit wh WITH (NOLOCK)
      ON pv.store_no = wh.store_no
     AND pv.register_no = wh.register_no
     AND pv.entry_date_time = wh.entry_date_time
     AND pv.transaction_series = wh.transaction_series
     AND pv.transaction_no = wh.transaction_no

SELECT @errno = @@error
IF @errno != 0
BEGIN
  SELECT @errmsg = 'Failed to insert #transl_post_void_detail',
         @object_name = '#transl_post_void_detail',
         @operation_name = 'INSERT'   
  GOTO error
END

-- void matching transactions in the current edit batch

UPDATE  work_tran_header_edit
   SET  transaction_void_flag = 1
  FROM  #transl_post_void_detail pv
  JOIN  work_tran_header_edit wh
    ON  pv.store_no = wh.store_no
   AND  pv.post_voided_register = wh.register_no
   AND  pv.transaction_date =  wh.transaction_date
   AND  pv.post_voided_trans_no = wh.transaction_no
   AND  pv.transaction_series = wh.transaction_series
 WHERE  pv.post_void_successful = 1
   AND  pv.post_voided_trans_no >= 0
   
SELECT @errno = @@error,
	@rows = @@rowcount
IF @errno != 0
  BEGIN
   SELECT @errmsg = 'Failed to update work_tran_header_edit',
          @object_name = 'work_tran_header_edit',
          @operation_name = 'UPDATE'   
   GOTO error
  END

IF @rows != @post_void_qty -- some trans remain to be post voided
  BEGIN

  INSERT #work_special_post_void (
	store_no,
	post_voided_register,
	transaction_date,
	transaction_series,
	post_voided_trans_no,
	transaction_id,
	transaction_void_flag,
	post_voiding_transaction_id, 
        post_voiding_trans_void_flag,
        current_batch_flag)
  SELECT pv.store_no, post_voided_register,
	pv.transaction_date,
	pv.transaction_series,
	pv.post_voided_trans_no,
	wh.transaction_id,
	wh.transaction_void_flag,
	pv.post_voiding_transaction_id,
	CASE WHEN wh.transaction_id IS NULL THEN pv.post_voiding_trans_void_flag ELSE 5 END,
	CASE WHEN wh.transaction_id IS NULL THEN 0 ELSE 1 END
    FROM #transl_post_void_detail pv WITH (NOLOCK)
        LEFT OUTER JOIN work_tran_header_edit wh WITH (NOLOCK)
           ON pv.store_no = wh.store_no
          AND pv.post_voided_register = wh.register_no
          AND pv.transaction_date = wh.transaction_date
          AND pv.post_voided_trans_no = wh.transaction_no
          AND pv.transaction_series = wh.transaction_series
   WHERE pv.post_void_successful = 1
     AND pv.post_voided_trans_no >= 0      
     AND pv.post_voiding_trans_void_flag = 10
  SELECT @errno = @@error, @special_void_rows = @@rowcount
  IF @errno != 0
  BEGIN
    SELECT @errmsg = 'Failed to insert temp table listing special post-void handling requests',
           @object_name = '#work_special_post_void',
           @operation_name = 'INSERT'   
    GOTO error
  END

  IF @special_void_rows > 0
  BEGIN
    UPDATE #work_special_post_void
       SET transaction_id = wh.transaction_id,
           post_voiding_trans_void_flag = 5,
           current_batch_flag = 1
      FROM #work_special_post_void s, work_tran_header_edit wh WITH (NOLOCK)
     WHERE s.transaction_id IS NULL
       AND s.store_no = wh.store_no
       AND s.transaction_date = wh.transaction_date
       AND s.post_voided_trans_no = wh.transaction_no
       AND s.transaction_series = wh.transaction_series

    SELECT @errno = @@error
    IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to mark cross-register post-voids as found',
             @object_name = '#work_special_post_void',
             @operation_name = 'UPDATE'   
      GOTO error
    END

    UPDATE #work_special_post_void
       SET transaction_id = wh.transaction_id,
           post_voiding_trans_void_flag = 5,
           current_batch_flag = 1
      FROM #work_special_post_void s, work_tran_header_edit wh WITH (NOLOCK)
     WHERE s.transaction_id IS NULL
       AND s.store_no = wh.store_no
       AND s.post_voided_trans_no = wh.transaction_no
       AND s.transaction_series = wh.transaction_series

    SELECT @errno = @@error
    IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to mark cross-date post-voids as found',
             @object_name = '#work_special_post_void',
             @operation_name = 'UPDATE'   
      GOTO error
    END

    IF @trickle_polling_flag <> 0
    BEGIN
      UPDATE #work_special_post_void
         SET transaction_id = h.transaction_id,
             post_voiding_trans_void_flag = 5,
             current_batch_flag = 0,
             transaction_void_flag = h.transaction_void_flag 
        FROM #work_special_post_void s, transaction_header h WITH (NOLOCK)
       WHERE s.transaction_id IS NULL
         AND s.transaction_date = h.transaction_date
         AND s.store_no = h.store_no
   AND s.post_voided_register = h.register_no
         AND s.post_voided_trans_no = h.transaction_no
         AND s.transaction_series = h.transaction_series

      SELECT @errno = @@error
      IF @errno != 0
      BEGIN
        SELECT @errmsg = 'Failed to mark outside-of-batch post-voids as found',
               @object_name = '#work_special_post_void',
               @operation_name = 'UPDATE'   
        GOTO error
      END

      UPDATE #work_special_post_void
         SET transaction_id = h.transaction_id,
		post_voiding_trans_void_flag = 5,
		current_batch_flag = 0,
		transaction_void_flag = h.transaction_void_flag 
        FROM #work_special_post_void s, transaction_header h, edit_store_date_list w
       WHERE s.transaction_id IS NULL
         AND s.transaction_date = h.transaction_date
         AND s.store_no = h.store_no
         AND s.post_voided_trans_no = h.transaction_no
         AND s.transaction_series = h.transaction_series
         AND h.store_no = w.store_no
         AND h.transaction_date = w.transaction_date
         AND h.register_no = w.register_no
         AND h.date_reject_id = w.date_reject_id
         AND h.transaction_void_flag IN (0,1)

      SELECT @errno = @@error
      IF @errno != 0
      BEGIN
        SELECT @errmsg = 'Failed to mark outside-of-batch cross-register post-voids as found',
               @object_name = '#work_special_post_void',
               @operation_name = 'UPDATE'   
        GOTO error
      END

      UPDATE #work_special_post_void
         SET transaction_id = h.transaction_id,
             post_voiding_trans_void_flag = 5,
             current_batch_flag = 0,
             transaction_void_flag = h.transaction_void_flag 
        FROM #work_special_post_void s, transaction_header h, edit_store_date_list w
       WHERE s.transaction_id IS NULL
         AND s.store_no = h.store_no
         AND s.post_voided_trans_no = h.transaction_no
         AND s.transaction_series =  h.transaction_series
         AND h.store_no = w.store_no
         AND h.transaction_date = w.transaction_date
         AND h.register_no = w.register_no
         AND h.date_reject_id = w.date_reject_id
         AND h.transaction_void_flag IN (0,1)

      SELECT @errno = @@error
      IF @errno != 0
      BEGIN
        SELECT @errmsg = 'Failed to mark cross-date post-voids as found',
               @object_name = '#work_special_post_void',
               @operation_name = 'UPDATE'   
        GOTO error
      END
    END --IF @trickle_polling_flag <> 0
    
    UPDATE #work_special_post_void
       SET post_voiding_trans_void_flag = 8,
           current_batch_flag = 1
     WHERE transaction_id IS NULL

    SELECT @errno = @@error
    IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to mark post-voiding transaction as a post-voiding reversal instead',
             @object_name = '#work_special_post_void',
             @operation_name = 'UPDATE'   
      GOTO error
    END
  
    UPDATE work_tran_header_edit
       SET transaction_void_flag = 1
      FROM #work_special_post_void s, work_tran_header_edit w
     WHERE s.current_batch_flag = 1
	AND s.transaction_id IS NOT NULL
	AND s.transaction_void_flag IS NULL  --i.e. wasn't already marked as void in the "easy" match.
	AND s.transaction_id = w.transaction_id
	AND w.transaction_void_flag <> 1

    SELECT @errno = @@error
    IF @errno != 0
    BEGIN
	SELECT @errmsg = 'Failed to mark current batch transactions as post-voided',
	       @object_name = 'work_tran_header_edit',
	       @operation_name = 'UPDATE'   
	GOTO error
    END
     
    UPDATE work_tran_header_edit
      SET transaction_void_flag = pv.post_voiding_trans_void_flag
      FROM #work_special_post_void pv, work_tran_header_edit w
     WHERE pv.post_voiding_transaction_id = w.transaction_id

    SELECT @errno = @@error
    IF @errno != 0
    BEGIN
	SELECT @errmsg = 'Failed to mark post-voiding-reversal-if-original-not-found requests as as post-voiding vs post-voiding-reversal',
	      @object_name = 'work_tran_header_edit',
	      @operation_name = 'UPDATE'   
	GOTO error
    END

  END --IF @special_void_rows > 0  --103326

  INSERT INTO #work_voids_edit(
          store_no,
          post_voided_register,
          transaction_date,
          transaction_series,
          post_voided_trans_no,
          transaction_void_flag) 
  SELECT pv.store_no,
          post_voided_register,
          pv.transaction_date,
          pv.transaction_series,
          pv.post_voided_trans_no,
          wh.transaction_void_flag
    FROM  #transl_post_void_detail pv WITH (NOLOCK)
    LEFT OUTER JOIN work_tran_header_edit wh WITH (NOLOCK)
      ON pv.store_no = wh.store_no
     AND pv.post_voided_register = wh.register_no
     AND pv.transaction_date = wh.transaction_date
     AND pv.post_voided_trans_no = wh.transaction_no
     AND pv.transaction_series = wh.transaction_series
   WHERE post_void_successful = 1
     AND post_voided_trans_no >= 0
     AND pv.post_voiding_trans_void_flag <> 10

   SELECT @errno = @@error,
          @rows_inserted = @@rowcount
   IF @errno != 0
     BEGIN
      SELECT @errmsg = 'Failed to insert #work_voids_edit',
             @object_name = '#work_voids_edit',
             @operation_name = 'INSERT'         
      GOTO error
     END

    /* Attempt to match unmatched post voids to previous transaction date (within same batch) */
    /* search previous transaction_date */
   UPDATE work_tran_header_edit
    SET transaction_void_flag = 1
     FROM  #work_voids_edit wv WITH (NOLOCK), work_tran_header_edit wh
     WHERE wv.transaction_void_flag IS NULL /* not matched yet */
       AND wv.store_no = wh.store_no
       AND wv.post_voided_register = wh.register_no
       AND DATEADD(dd, -1, wv.transaction_date)  = wh.transaction_date
       AND wv.post_voided_trans_no = wh.transaction_no
       AND wv.transaction_series = wh.transaction_series
       AND wh.transaction_void_flag != 1

   SELECT @errno = @@error,
	@rows_prev_day = @@rowcount
   IF @errno != 0
     BEGIN
      SELECT @errmsg = 'Failed to update work_tran_header_edit (prev day)',
             @object_name = 'work_tran_header_edit',
             @operation_name = 'UPDATE'           
      GOTO error
     END

   IF @rows_prev_day >= 1
      SELECT @rows = @rows + @rows_prev_day

  IF @special_void_rows > 0
  BEGIN
    INSERT INTO #work_voids_edit(
           store_no, post_voided_register, transaction_date,
           transaction_series, post_voided_trans_no, transaction_void_flag,
           post_voided_transaction_id)
    SELECT store_no, post_voided_register, transaction_date,
           transaction_series, post_voided_trans_no, transaction_void_flag,
           transaction_id
      FROM #work_special_post_void
     WHERE current_batch_flag = 0
       AND transaction_id IS NOT NULL
       AND transaction_void_flag = 0
    SELECT @errno = @@error,
           @rows_inserted = IsNull(@rows_inserted, 0) + @@rowcount
    IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to add special handling post-voids to #work_voids_edit',
             @object_name = '#work_voids_edit',
             @operation_name = 'INSERT'         
      GOTO error
    END
  END --IF @special_void_rows > 0

  END /* If @rows != @post_void_qty */

ELSE    --103326
  BEGIN
  UPDATE work_tran_header_edit
     SET transaction_void_flag = 5
    FROM #transl_post_void_detail pv, work_tran_header_edit w
   WHERE pv.post_voiding_transaction_id = w.transaction_id
     AND pv.post_voiding_trans_void_flag = 10
     AND w.transaction_void_flag = 10
  SELECT @errno = @@error
  IF @errno != 0
  BEGIN
    SELECT @errmsg = 'Failed to post-voiding-reversal if original not found else post-voiding requests as Post Voiding',
           @object_name = 'work_tran_header_edit',
           @operation_name = 'UPDATE'   
    GOTO error
  END 
  END --ELSE of IF @rows != @post_void_qty 

-- drop temp tables to release space

DROP TABLE #transl_post_void_detail
DROP TABLE #work_special_post_void

IF @trickle_polling_flag = 0
  RETURN

IF @rows = @post_void_qty -- return if there are no remaining unmatched voids
  RETURN

/* exclude transactions that were matched to the previous day */

DELETE #work_voids_edit
  FROM #work_voids_edit wv
  JOIN work_tran_header_edit wh WITH (NOLOCK)
    ON wv.store_no = wh.store_no
   AND wv.post_voided_register = wh.register_no
   AND DATEADD(dd,-1,wv.transaction_date) = wh.transaction_date
   AND wv.post_voided_trans_no = wh.transaction_no
   AND wv.transaction_series = wh.transaction_series
   AND wh.transaction_void_flag = 1 /* voids previously matched to prev day */
 WHERE wv.transaction_void_flag IS NULL  

SELECT @errno = @@error,
       @rows_deleted = @@rowcount
IF @errno != 0
  BEGIN
   SELECT @errmsg = 'Failed to DELETE #work_voids_edit (1)',
          @object_name = '#work_voids_edit',
          @operation_name = 'DELETE'                      
   GOTO error
  END

IF @rows_deleted = @rows_inserted -- return if there are no remaining unmatched voids
  RETURN

DELETE work_if_header
  WHERE process_id = @process_id

SELECT @errno = @@error
IF @errno != 0
  BEGIN
   SELECT @errmsg = 'Failed to delete work_if_header',
          @object_name = 'work_if_header',
          @operation_name = 'DELETE'             
   GOTO error
  END

-- Create reversing entries in the interface for any remaining unmatched post voiding trans
-- that can now be matched to tran header, i.e. to previous edit batches

INSERT INTO #work_tran_void(
       transaction_id,
       transaction_void_flag,
       entry_date_time,
       transaction_date,
       sa_rejection_flag)
SELECT th.transaction_id,
       th.transaction_void_flag,
       th.entry_date_time,
       th.transaction_date,
       th.sa_rejection_flag
  FROM #work_voids_edit wv WITH (NOLOCK)
  JOIN transaction_header th WITH (NOLOCK)
     ON wv.store_no = th.store_no
    AND wv.post_voided_register = th.register_no
    AND wv.transaction_date = th.transaction_date
    AND wv.post_voided_trans_no = th.transaction_no
    AND wv.transaction_series = th.transaction_series
  WHERE wv.transaction_void_flag IS NULL /* not matched yet */
    AND wv.post_voided_transaction_id IS NULL  --not special request

SELECT @errno = @@error
IF @errno != 0
  BEGIN
   SELECT @errmsg = 'Failed to insert #work_tran_void',
          @object_name = '#work_tran_void',
          @operation_name = 'INSERT'      
   GOTO error
  END

INSERT INTO #work_tran_void(
       transaction_id,
       transaction_void_flag,
       entry_date_time,
       transaction_date,
       sa_rejection_flag)
SELECT th.transaction_id,
       th.transaction_void_flag,
       th.entry_date_time,
       th.transaction_date,
       th.sa_rejection_flag
  FROM #work_voids_edit wv WITH (NOLOCK)
  JOIN transaction_header th WITH (NOLOCK)
    ON wv.post_voided_transaction_id = th.transaction_id
  WHERE wv.post_voided_transaction_id IS NOT NULL  --special request

SELECT @errno = @@error
IF @errno != 0
BEGIN
  SELECT @errmsg = 'Failed to add special requests to temp table #work_tran_void',
         @object_name = '#work_tran_void',
         @operation_name = 'INSERT'      
  GOTO error
END

INSERT INTO work_pv_media_rec
         (orig_transaction_id, rec_process_id)
SELECT th.transaction_id, 0
    FROM #work_voids_edit wv WITH (NOLOCK)
    JOIN transaction_header th WITH (NOLOCK)
       ON wv.store_no = th.store_no
      AND wv.post_voided_register = th.register_no
      AND wv.transaction_date = th.transaction_date
      AND wv.post_voided_trans_no = th.transaction_no
      AND wv.transaction_series = th.transaction_series
      AND th.date_reject_id = 0 
      AND th.sa_rejection_flag = 0
    JOIN media_parameter_selection mps
   ON th.store_no = mps.store_no 
      AND th.register_no = mps.register_no 
      AND th.transaction_date >= mps.effective_from_date 
      AND (th.transaction_date < mps.effective_until_date OR mps.effective_until_date IS NULL)    
    WHERE wv.transaction_void_flag IS NULL /* not matched yet */

  SELECT @errno = @@error
  IF @errno != 0
  BEGIN
    SELECT @errmsg = 'from #work_voids_edit, header and media_parameter_selection',
           @object_name = 'work_pv_media_rec',
           @operation_name = 'INSERT'             
    GOTO error
  END  

  INSERT work_if_header (
	process_id,
	transaction_id,
	if_entry_no,
	effective_date,
	entry_date_time )
  SELECT DISTINCT
	@process_id,
	wt.transaction_id,
	0,
	wt.transaction_date,
	wt.entry_date_time
   FROM #work_tran_void wt WITH (NOLOCK)
  JOIN interface_control ic WITH (NOLOCK)
    ON wt.transaction_id = ic.transaction_id
    AND interface_status_flag = 1 /* not i/f reject */
  WHERE wt.transaction_void_flag IN (0,8) /* not already voided */
    AND wt.transaction_id >= 1

  SELECT @errno = @@error,
	@rows = @@rowcount
  IF @errno != 0
  BEGIN
   SELECT @errmsg = 'Failed to insert work_if_header',
          @object_name = 'work_if_header',
          @operation_name = 'INSERT'         
   GOTO error
  END


IF @rows >= 1 -- (feed reversals)
  BEGIN /* Create reversing entries in the interfaces */

   INSERT if_transaction_header (
        store_no,
	register_no,
	transaction_date,
	transaction_series,
	transaction_no,
	entry_date_time,
	cashier_no,
	transaction_category,
	tender_total,
	transaction_void_flag,
	customer_info_exists,
	exception_flag,
	deposit_declaration_flag,
	closeout_flag,
	media_count_flag,
	customer_modified_flag,
	tax_override_flag,
	pos_tax_jurisdiction,
	source_process_no,
	edit_timestamp, 
	employee_no,
	transaction_remark,
	last_modified_date_time,
	in_use_timestamp,
	updated_by_user_id,
	transaction_id,
	till_no )
   SELECT 
	store_no,
	register_no,
	transaction_date,
	transaction_series,
	transaction_no,
	th.entry_date_time,
	cashier_no,
	transaction_category,
	tender_total,
	8,              /* post voiding reversal */
	customer_info_exists,
	exception_flag,
	deposit_declaration_flag,
	closeout_flag,
	media_count_flag,
	customer_modified_flag,
	tax_override_flag,
	pos_tax_jurisdiction,
	1,
	@edit_timestamp, 
	employee_no,
	transaction_remark,
	last_modified_date_time,
	in_use_timestamp,
	updated_by_user_id,
	th.transaction_id,
	th.till_no
     FROM  work_if_header wf WITH (NOLOCK)
     JOIN transaction_header th WITH (NOLOCK)
       ON wf.transaction_id = th.transaction_id
    WHERE process_id = @process_id

   SELECT @errno = @@error
   IF @errno != 0
     BEGIN
      SELECT @errmsg = 'Failed to insert if_transaction_header',
             @object_name = 'if_transaction_header',
             @operation_name = 'INSERT'          
      GOTO error
     END

   /* Determine if_entry_no for interface headers just inserted */

   UPDATE work_if_header
     SET if_entry_no = ith.if_entry_no
     FROM work_if_header wf
     JOIN transaction_header th WITH (NOLOCK)
        ON wf.transaction_id = th.transaction_id
     JOIN if_transaction_header ith WITH (NOLOCK)
        ON th.store_no = ith.store_no
       AND th.register_no = ith.register_no
       AND th.transaction_date = ith.transaction_date
       AND th.entry_date_time = ith.entry_date_time
       AND th.transaction_no = ith.transaction_no
       AND th.transaction_series = ith.transaction_series
       AND ith.edit_timestamp = @edit_timestamp
    WHERE process_id = @process_id

   SELECT @errno = @@error
   IF @errno != 0
     BEGIN
      SELECT @errmsg = 'Failed to update work_if_header',
      @object_name = 'work_if_header',
             @operation_name = 'UPDATE'            
      GOTO error
     END

    /* set voiding_reversal_flag = -1 */
EXEC create_if_details_move_$sp @process_id, @user_id, -1, @errmsg OUTPUT

   SELECT @errno = @@error
   IF @errno != 0
     BEGIN
      IF @errmsg IS NULL  
        SELECT @errmsg = 'Failed to execute create_if_details_move',
               @object_name = 'create_if_details_move',
               @operation_name = 'EXEC'                 
      GOTO error
     END

  END /* If @rows >= 1 (feed reversals) */

/* Remove any interface rejects on the voided transactions */

BEGIN TRANSACTION

DELETE if_rejection_reason
  FROM if_rejection_reason ir
  JOIN #work_tran_void wt WITH (NOLOCK)
     ON wt.transaction_id = ir.transaction_id
    AND wt.transaction_id >= 1

SELECT @errno = @@error
IF @errno != 0
  BEGIN
   SELECT @errmsg = 'Failed to delete if_rejection_reason',
          @object_name = 'if_rejection_reason',
          @operation_name = 'DELETE'         
   GOTO error
  END

UPDATE transaction_line
   SET interface_rejection_flag = 0
  FROM transaction_line tl
  JOIN #work_tran_void wt WITH (NOLOCK)
    ON wt.transaction_id = tl.transaction_id
   AND wt.transaction_id >= 1   
 WHERE interface_rejection_flag = 1

SELECT @errno = @@error
IF @errno != 0
  BEGIN
   SELECT @errmsg = 'Failed to update transaction_line (if-rejects)',
          @object_name = 'transaction_line',
          @operation_name = 'UPDATE'         
   GOTO error
  END

UPDATE transaction_header
 SET transaction_void_flag = 1,
     if_rejection_flag = 0
  FROM #work_tran_void wt WITH (NOLOCK), transaction_header th
 WHERE wt.transaction_id = th.transaction_id

SELECT @errno = @@error
IF @errno != 0
  BEGIN
   SELECT @errmsg = 'Failed to update transaction_header (prior transactions)',
          @object_name = 'transaction_header',
          @operation_name = 'UPDATE'          
   GOTO error
  END

DELETE interface_control
  FROM #work_tran_void wt WITH (NOLOCK), interface_control ic
 WHERE wt.sa_rejection_flag = 0
   AND wt.transaction_id = ic.transaction_id

SELECT @errno = @@error
IF @errno != 0
  BEGIN
   SELECT @errmsg = 'Failed to delete interface_control (prior transactions)',
          @object_name = 'interface_control ',
          @operation_name = 'DELETE'                
   GOTO error
  END

IF @rows >= 1
  BEGIN
   INSERT Ex_Queue (
		queue_id, -- interface_id
    		key_1, --if_entry_no
		key_2, --interface_control_flag
		key_9, -- effective_date
		key_10, -- interface_posting_date
		key_11) -- entry_date_time
   SELECT interface_id,
	if_entry_no,
	20,
	wt.effective_date,
	getdate(),
	wt.entry_date_time
    FROM work_if_header wt WITH (NOLOCK)
    JOIN interface_control ic WITH (NOLOCK)
      ON wt.transaction_id = ic.transaction_id
     AND interface_status_flag = 1
     AND wt.transaction_id >= 1  
   WHERE process_id = @process_id

   SELECT @errno = @@error
   IF @errno != 0
     BEGIN
      SELECT @errmsg = 'Failed to insert Ex_Queue',
             @object_name = 'Ex_Queue',
             @operation_name = 'INSERT'             
      GOTO error
     END

  END /* If @rows >= 1 */

COMMIT TRANSACTION

DELETE work_if_header
 WHERE process_id = @process_id

SELECT @errno = @@error
IF @errno != 0
   BEGIN
     SELECT @errmsg = 'Failed to delete work_if_header (2)',
          @object_name = 'work_if_header ',
          @operation_name = 'DELETE'        
     GOTO error
   END

DROP TABLE #work_voids_edit
DROP TABLE #work_tran_void

RETURN

error:
	EXEC common_error_handling_$sp 4, @errno, @errmsg, 0, @message_id, 
	@process_name, @object_name, @operation_name, 1, @edit_process_no,
	0, null, 0, null, null, null, null, null, null, 0, @process_id, @user_id
	
	RETURN


```

