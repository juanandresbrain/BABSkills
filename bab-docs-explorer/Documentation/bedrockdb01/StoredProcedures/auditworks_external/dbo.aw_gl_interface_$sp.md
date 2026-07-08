# dbo.aw_gl_interface_$sp

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.aw_gl_interface_$sp"]
    CLNDR_PRD(["CLNDR_PRD"]) --> SP
    CRDM_PRMTRS(["CRDM_PRMTRS"]) --> SP
    audit_status(["audit_status"]) --> SP
    auditworks_parameter(["auditworks_parameter"]) --> SP
    auditworks_system_flag(["auditworks_system_flag"]) --> SP
    aw_gl_interface(["aw_gl_interface"]) --> SP
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
    dw_store_status(["dw_store_status"]) --> SP
    dw_subledger(["dw_subledger"]) --> SP
    end_process_log__sp(["end_process_log_$sp"]) --> SP
    gl_account_cross_reference(["gl_account_cross_reference"]) --> SP
    start_process_log__sp(["start_process_log_$sp"]) --> SP
    store_audit_status(["store_audit_status"]) --> SP
    subledger(["subledger"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| CLNDR_PRD |
| CRDM_PRMTRS |
| audit_status |
| auditworks_parameter |
| auditworks_system_flag |
| aw_gl_interface |
| common_error_handling_$sp |
| dw_store_status |
| dw_subledger |
| end_process_log_$sp |
| gl_account_cross_reference |
| start_process_log_$sp |
| store_audit_status |
| subledger |

## Stored Procedure Code

```sql
create proc dbo.aw_gl_interface_$sp @period_ending_date		smalldatetime,
@journal_entry_description 	nchar(29),
@last_date_closed		smalldatetime,
@period_end_date		smalldatetime

AS

/*
** NAME: aw_gl_interface_$sp
** DESC: Build aw_gl_interface table from subledger table
**       It is preferred to use user_r3_gl_interface_$sp for new installs.
** 	 Called from period_end_$sp

HISTORY:
Date     Name        Def# Desc
Sep09,14 Vicci  TFS-83789 Support subledger amounts up to +/-999,999,999,999.99.
Jun04,12 Vicci     134811 Explicitly insert aw_gl_interface table columns whose defaults have disappeared.
May11,11 Vicci     126975 Store/Dates with a dw_store_status.store_status of 3 should not be excluded from the export since the store/date
                          may have been rebuilt following an over/short adjustment, tax rate adjustment impacting tax-stripping, etc.
                          The subledger.posting_status is what indicates whether or not an entry has been interfaced to G/L, not the date status.
Nov12,10 Paul      121833 Add missing gl_posting_datetime setting; also update dw_subledger on consolidated
Nov06,06 Paul       74790 read CRDM_PRMTRS to get CLNDR_ID
Oct25,06 Phu        77931 Fix outer join for SQL 2005 Mode 90.
Oct03,05 Paul       60471 apply 60634 to SA5
May04,05 Sab      DV-1254 Update dw_store_status set store_status = 3;join dw_store_status instead of store_audit_status
Dec15,04 David    DV-1191 Improve performance by adding hints.
May11,04 David    DV-1071 Use new Calendar table.
Sep19,05 Daphna     60634 set subledger.gl_posting_datetime when posting_status set = 1
Oct11,02 Winnie   1-D048L Expand the gl_company_no up to 10 digits.
Nov30,01 Phu         8931 Progress monitor and error handling
Jul05,01 Winnie      8169 Remove the date format of status_date
Mar23,01 Winnie      7450 Check gl_interface_timing for daily GL, move out all the recurring logic of all the GL interface and put it in period end. 
Jul05,00 Maryam      5696 Prevent duplicate error 2601 when inserting in batch header/trailer
May25,00 John G      5864 Change '= NULL' to 'IS NULL' where applicable to mirror Oracle.
Mar01,00 Phu         5900 Change @@fetch_status > 0 to @@fetch_status <> 0 for MS SQL compatibility
Jan14,00 Phu         5831 Fix batch debits <> detail debits
Jan13,00 Vicci       5835 Use auditworks_parameter gl_interface_timing instead of smartload_var ascii_update_timin 
Dec15,99 Henry       5781 Support creation of ascii subledger export when preliminary period end
Sep20,99 Vicci       5455 Support daily (instead of period-end) building of ascii file
Aug16,99 Phu         5233 Expand GL account number up to 160 characters in length
*/

DECLARE
	@calendar_date 				smalldatetime,
	@current_date 				smalldatetime,
	@cursor_open 				tinyint,
	@errmsg 				nvarchar(255),
	@errno 					int,
	@gl_account_id 				int,
	@instance_id				int,
	@gl_account_no 				nvarchar(160),
	@message_id				int,
	@object_name				nvarchar(255),
	@operation_name				nvarchar(100),
	@process_name				nvarchar(100),
	@pd_end_julian_date 			nchar(5),
	@period_ending_date2 			smalldatetime,
	@process_log_entry 			tinyint,
	@process_no 				smallint,
	@process_timestamp 			float,
	@rows					int,
	@scaleout_flag				int,
	@scaleout_gl_export_on_peri		tinyint,
	@transaction_count 			numeric(12,0),
	@transaction_date 			smalldatetime,
	@zero_filler				nchar(10),
	@zero_filler_2				nchar(2),
	@zero_filler_3				nchar(3),
	@mask					nvarchar(10),
	@gl_company_no_length			tinyint,
	@clndr_id				binary(16),
	@lvl_month				binary(16),
	@month_end_date				smalldatetime


SELECT 	@current_date = getdate(),
	@cursor_open = 0,
	@errmsg = NULL,
	@process_log_entry = 0,
	@process_no = 205,
	@process_timestamp = 0,
	@transaction_count = 0,
	@zero_filler_2 = '00',	
	@zero_filler_3 = '000',
	@message_id = 201068,
	@process_name = 'aw_gl_interface_$sp',
	@zero_filler = '0000000000'

CREATE TABLE #cal_date (
	calendar_date 		smalldatetime 	not null,
	pd_end_date		smalldatetime 	null,
	pd_end_julian_date	nchar(5) null )

SELECT @errno = @@error
IF @errno <> 0
  BEGIN
	SELECT @errmsg = 'Unable to create table #cal_date',
	       @object_name = '#cal_date',
	       @operation_name = 'CREATE TABLE'
	GOTO error
  END

create table #gl_int_temp (
   gl_company_no  nvarchar(10) not null,
   gl_period_no  nchar(2) not null,
   period_ending_date  nchar(5) not null,
   gl_account_no  nvarchar(160) not null,
   amount  money not null )

SELECT @errno = @@error
IF @errno <> 0
  BEGIN
	SELECT @errmsg = 'Unable to create table #gl_int_temp',
	       @object_name = '#gl_int_temp',
	       @operation_name = 'CREATE TABLE'
	GOTO error
  END

EXEC start_process_log_$sp @process_no, @process_timestamp OUTPUT, @errmsg OUTPUT

SELECT @errno = @@error
IF @errno <> 0
  BEGIN
	SELECT @object_name = 'start_process_log_$sp',
	     @operation_name = 'EXECUTE'
	IF @errmsg IS NULL -- 
	  SELECT @errmsg = 'Unable to execute start_process_log_$sp'
	GOTO error
  END
SELECT @process_log_entry = 1

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

SELECT @gl_company_no_length = ISNULL(CONVERT(TINYINT,par_value),2)
 FROM auditworks_parameter
 WHERE par_name = 'gl_company_no_length'

SELECT @errno = @@error
IF @errno <> 0
  BEGIN
	SELECT @errmsg = 'Unable to select gl_company_no_length from auditworks_parameter',
	  @object_name = 'auditworks_parameter',
	       @operation_name = 'SELECT'
	GOTO error
  END

SELECT @clndr_id = PRMTR_VAL_BIN
  FROM CRDM_PRMTRS
 WHERE PRMTR_NAME = 'GL_PSTNG_CLNDR_ID'

SELECT @errno = @@error, @rows = @@rowcount
IF @rows = 0 AND @errno = 0
  SELECT @errno = 201612
IF @errno <> 0
  BEGIN
	SELECT @errmsg = 'Unable to select calendar id',
	       @object_name = 'CRDM_PRMTRS',
	       @operation_name = 'SELECT'
	GOTO error
  END

SELECT @lvl_month = par_bin_value
  FROM auditworks_parameter
 WHERE par_name = 'clndr_lvl_month'

SELECT @errno = @@error
IF @errno <> 0
  BEGIN
	SELECT @errmsg = 'Unable to select month level id',
	       @object_name = 'auditworks_parameter',
	       @operation_name = 'SELECT'
	GOTO error
  END

DECLARE clndr_crsr CURSOR FAST_FORWARD
    FOR
 SELECT DATEADD( dd, -1, CONVERT(SMALLDATETIME, CONVERT(nvarchar, END_DATE_TIME, 101)) )
   FROM CLNDR_PRD
  WHERE CLNDR_ID          = @clndr_id
    AND CLNDR_LVL_TYPE_ID = @lvl_month
    AND END_DATE_TIME     > DATEADD(dd,1,@last_date_closed)
    AND STRT_DATE_TIME   <= @period_ending_date
  ORDER BY END_DATE_TIME   

OPEN clndr_crsr
SELECT @cursor_open = 2,
       @calendar_date = @last_date_closed

WHILE 1 = 1
BEGIN
  FETCH clndr_crsr 
   INTO @month_end_date 
   
  IF @@fetch_status <> 0
  BREAK

  SELECT @pd_end_julian_date = SUBSTRING( STR( datepart(yy, @month_end_date), 4), 3, 2 ) +
                               RIGHT (@zero_filler_3 + LTRIM( STR( DATEPART(dy,@month_end_date), 3) ), 3)

  WHILE @calendar_date < @month_end_date AND @calendar_date < @period_ending_date
  BEGIN
    SELECT @calendar_date = DATEADD(dd,1,@calendar_date)
  
    INSERT #cal_date (
	calendar_date,
	pd_end_date,
	pd_end_julian_date )
    VALUES (
	@calendar_date,
	@month_end_date,
	@pd_end_julian_date)

	SELECT @errno = @@error
	IF @errno <> 0
	BEGIN
	  SELECT @errmsg = 'Unable to insert #gl_int_temp',
	         @object_name = '#gl_int_temp',
	         @operation_name = 'INSERT'
	  GOTO error
	END	
  END -- WHILE @calendar_date <= @month_end_date AND @calendar_date <= @period_ending_date

END -- WHILE 1=1

CLOSE clndr_crsr
DEALLOCATE clndr_crsr
SELECT @cursor_open = 0

INSERT #gl_int_temp (
	gl_company_no,
	gl_period_no,
	period_ending_date,
	gl_account_no,
	amount )
  SELECT
	RIGHT (@zero_filler + LTRIM (STR (s.gl_company, @gl_company_no_length)), @gl_company_no_length),
	RIGHT (@zero_filler_2 + LTRIM (STR (s.period, 2)), 2),
	c.pd_end_julian_date,
	ISNULL (LTRIM (RTRIM (g.gl_account_no)), '0'),
	SUM(s.amount)
  FROM subledger s WITH (NOLOCK)
       INNER JOIN #cal_date c WITH (NOLOCK) ON (s.transaction_date = c.calendar_date)
       LEFT JOIN gl_account_cross_reference g ON (s.gl_account_id = g.gl_account_id)
  WHERE (s.transaction_date >= @last_date_closed OR @last_date_closed IS NULL)
    AND s.posting_status = 0
  GROUP BY
	RIGHT (@zero_filler + LTRIM (STR (s.gl_company, @gl_company_no_length)), @gl_company_no_length),
	RIGHT (@zero_filler_2 + LTRIM (STR (s.period, 2)), 2),
	c.pd_end_julian_date,
	ISNULL (LTRIM (RTRIM (g.gl_account_no)), '0')

  SELECT @errno = @@error
  IF @errno <> 0
    BEGIN
	SELECT @errmsg = 'Unable to insert #gl_int_temp',
	       @object_name = '#gl_int_temp',
	       @operation_name = 'INSERT'
	GOTO error
    END

BEGIN TRAN

  /* Create batch header */

  INSERT aw_gl_interface (
	gl_company_no,
	gl_period_no,
	period_ending_date,
	record_type,
	gl_account_no,			--134811
	journal_entry_description,	--134811
	detail_type_indicator,		--134811
	amount )
  SELECT
	gl_company_no,
	gl_period_no,
	period_ending_date,
	'BH',
	'                            ', 
	' ',
	' ',
	CONVERT (NUMERIC(14,0), ROUND (SUM (amount), 0))
  FROM #gl_int_temp WITH (NOLOCK)
  WHERE amount > 0
  GROUP BY
	gl_company_no,
	gl_period_no,
	period_ending_date

  SELECT @errno = @@error,
	 @transaction_count = @@rowcount

  IF @errno <> 0
    BEGIN
	SELECT @errmsg = 'Unable to create aw_gl_interface for batch header',
	       @object_name = 'aw_gl_interface',
	       @operation_name = 'INSERT'
	GOTO error
    END

  /* Create batch trailer */

  INSERT aw_gl_interface (
	gl_company_no,
	gl_period_no,
	period_ending_date,
	record_type,
	gl_account_no,			--134811
	journal_entry_description,	--134811
	detail_type_indicator,		--134811
	amount )
  SELECT
	gl_company_no,
	gl_period_no,
	period_ending_date,
	'TH',
	'                            ', 
	' ',
	' ',
	CONVERT (NUMERIC(14,0), ROUND (SUM (amount), 0))
  FROM #gl_int_temp WITH (NOLOCK)
  WHERE amount < 0
  GROUP BY
	gl_company_no,
	gl_period_no,
	period_ending_date

  SELECT @errno = @@error,
	 @transaction_count = @transaction_count + @@rowcount

  IF @errno <> 0
    BEGIN
	SELECT @errmsg = 'Unable to create aw_gl_interface for trailer',
	       @object_name = 'aw_gl_interface',
	       @operation_name = 'INSERT'
	GOTO error
    END

  /* Create gl details */

  INSERT aw_gl_interface (
	gl_company_no,
	gl_period_no,
	period_ending_date,
	record_type,
	gl_account_no,
	journal_entry_description,
	detail_type_indicator,
	amount )
  SELECT
	gl_company_no,
	gl_period_no,
	period_ending_date,
	'DT',
	gl_account_no,
	@journal_entry_description,
	' ',
	CONVERT (NUMERIC(14,0), ROUND (amount * 100, 0))
  FROM #gl_int_temp WITH (NOLOCK)

  SELECT @errno = @@error,
	@transaction_count = @transaction_count + @@rowcount

  IF @errno <> 0
    BEGIN
	SELECT @errmsg = 'Unable to create aw_gl_interface for details',
	       @object_name = 'aw_gl_interface',
	       @operation_name = 'INSERT'
	GOTO error
    END

DECLARE cal_date_crsr CURSOR FAST_FORWARD
    FOR
 SELECT calendar_date
   FROM #cal_date WITH (NOLOCK)

SELECT @errno = @@error
IF @errno <> 0
  BEGIN
   SELECT @errmsg = 'Unable to declare cursor cal_date_crsr',
	  @object_name = 'cal_date_crsr',
	  @operation_name = 'DECLARE CURSOR'
   GOTO error
  END

OPEN cal_date_crsr
SELECT @cursor_open = 1

WHILE 2 = 2
  BEGIN
	FETCH cal_date_crsr INTO
		@calendar_date

	IF @@fetch_status <> 0
		BREAK

	-- Set subledger posting status to yes --

	UPDATE subledger
	SET posting_status = 1,
	    gl_posting_datetime = @current_date
	WHERE transaction_date = @calendar_date
	AND posting_status = 0

	SELECT @errno = @@error
	IF @errno <> 0
	 BEGIN
		SELECT @errmsg = 'Unable to update subledger with posting_status to 1',
		       @object_name = 'subledger',
		       @operation_name = 'UPDATE'
		GOTO error
	  END

	  /* If running export on peripheral, also need to set posted_status in subledger on consolidated */
	  IF @scaleout_gl_export_on_peri = 1 AND @scaleout_flag = 1 -- THEN 
	    BEGIN

	      UPDATE dw_subledger
	         SET posting_status = 1,
	             gl_posting_datetime = @current_date
	       WHERE posting_status = 0
	         AND transaction_date = @calendar_date
	         AND store_no
	             IN (SELECT DISTINCT store_no
	                 FROM subledger
	                 WHERE transaction_date = @calendar_date
	                   AND posting_status >= 1)

		  SELECT @errno = @@error
		  IF @errno <> 0
		    BEGIN
		     SELECT @errmsg = 'Failed to update dw_subledger with posting_status to 1',
			@object_name = 'dw_subledger',
			@operation_name = 'UPDATE'
			GOTO error
		    END
	    END -- If @scaleout_gl_export_on_peri = 1

  END -- While 2 = 2 --

CLOSE cal_date_crsr
DEALLOCATE cal_date_crsr
SELECT @cursor_open = 0

  UPDATE audit_status
     SET audit_status = 500,
	 status_date = @current_date
  WHERE audit_status = 400
  AND sales_date > @last_date_closed
  AND sales_date <= @period_ending_date

  SELECT @errno = @@error
  IF @errno <> 0
    BEGIN
	SELECT @errmsg = 'Unable to set audit_status to 500 from 400',
	       @object_name = 'audit_status',
	       @operation_name = 'UPDATE'
	GOTO error
    END

  UPDATE store_audit_status
  SET store_audit_status = 500,
	store_status_date = @current_date
  WHERE store_audit_status = 400
  AND sales_date > @last_date_closed 
  AND sales_date <= @period_ending_date

  SELECT @errno = @@error
  IF @errno <> 0
    BEGIN
	SELECT @errmsg = 'Unable to set store_audit_status to 500 from 400',
	       @object_name = 'store_audit_status',
	       @operation_name = 'UPDATE'
	GOTO error
    END

  UPDATE dw_store_status
     SET store_status = 3
   WHERE store_status = 2
     AND sales_date > @last_date_closed 
     AND sales_date <= @period_ending_date
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

-- NOTE:
--	Moved the UPDATE of parameter_general, for the
--	RESET of the last_date_closed = period_end_date, and the
--	RESET of the preliminary_period_end_date = NULL,
--	to the proc reset_period_end_$sp

IF @process_log_entry = 1
	EXEC end_process_log_$sp @process_no, @process_timestamp, @transaction_count

DROP TABLE #cal_date
DROP TABLE #gl_int_temp

RETURN


error:
	IF @cursor_open = 1
	  BEGIN
		CLOSE cal_date_crsr
		DEALLOCATE cal_date_crsr
		SELECT @cursor_open = 0
	  END

	IF @cursor_open = 2
	BEGIN
		CLOSE clndr_crsr
		DEALLOCATE clndr_crsr
	END

	EXEC common_error_handling_$sp @process_no, @errno, @errmsg, 0, @message_id, 
	@process_name, @object_name, @operation_name, 1
	RETURN
```

