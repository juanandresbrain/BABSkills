# dbo.ecp_reallocation_request_$sp

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.ecp_reallocation_request_$sp"]
    ADT_TRL_DTL(["ADT_TRL_DTL"]) --> SP
    ADT_TRL_HDR(["ADT_TRL_HDR"]) --> SP
    CLNDR_LVL(["CLNDR_LVL"]) --> SP
    CLNDR_LVL_TYPE(["CLNDR_LVL_TYPE"]) --> SP
    CLNDR_PRD(["CLNDR_PRD"]) --> SP
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
    dbo_convdate(["dbo.convdate"]) --> SP
    ecp_parameter(["ecp_parameter"]) --> SP
    ecp_system_flag(["ecp_system_flag"]) --> SP
    interface_status(["interface_status"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ADT_TRL_DTL |
| ADT_TRL_HDR |
| CLNDR_LVL |
| CLNDR_LVL_TYPE |
| CLNDR_PRD |
| common_error_handling_$sp |
| dbo.convdate |
| ecp_parameter |
| ecp_system_flag |
| interface_status |

## Stored Procedure Code

```sql
CREATE proc  dbo.ecp_reallocation_request_$sp 
@from_reallocation_date datetime, 
@to_reallocation_date datetime,
@allocation_type_list nvarchar(4000) = NULL,
@user_id int = NULL,
@process_id binary(16) = NULL
AS 

/* 
Proc Name: ecp_reallocation_request_$sp 
Desc:   Called by UI to request reperformance of allocations

HISTORY:  
Date     Name           Def#    Desc
Jun30,16 Vicci       DAOM-996   Add audit-trail.  Ensure all request information is logged before the request is visible.
Feb14,08 Vicci          97607   Ensure that ecp_posting_$sp knows it when a request is made while the posting
                                was in the middle of running.
Jul05,07 Vicci          85597   Fix to-date to be a period-end-date
Apr02,07 Vicci		85597	Author
*/

SET NOCOUNT ON
DECLARE
  @errmsg                       nvarchar(255),
  @errno                        int,
  @message_id                   int,
  @object_name                  nvarchar(255),
  @operation_name               nvarchar(100),
  @process_name                 nvarchar(100),
  @process_no                   int,
  @rows				int,
  @stream_no                    tinyint,
  @ecp_clndr_id			binary(16),
  @lowest_calendar_level_id	binary(16),
  @sep 				nchar(1),
  @ENTRY_ID                     binary(16);

SELECT @message_id = 201068,
       @operation_name = 'Unknown',
       @process_name = 'ecp_reallocation_request_$sp',
       @process_no = 282,
       @stream_no = 1,
       @sep = nchar(12),
       @ENTRY_ID = newid();

SELECT @ecp_clndr_id = par_bin_value
  FROM ecp_parameter p
 WHERE par_name = 'ecp_dflt_clndr_id'  
SELECT @errno = @@error
IF @errno <> 0
BEGIN
  SELECT @errmsg = 'Unable to which calendar to use',
         @object_name = 'ecp_parameter',
         @operation_name = 'SELECT'
  GOTO error
END

SELECT @lowest_calendar_level_id = CLNDR_LVL_TYPE_ID
  FROM CLNDR_LVL_TYPE
 WHERE CLNDR_LVL_SEQ = (SELECT MAX(CLNDR_LVL_SEQ)
			  FROM CLNDR_LVL_TYPE
			 WHERE CLNDR_LVL_TYPE_ID
			    IN (SELECT DISTINCT CLNDR_LVL_TYPE_ID
                                  FROM CLNDR_LVL
                                  WHERE CLNDR_ID = @ecp_clndr_id))
   AND CLNDR_LVL_TYPE_ID
    IN (SELECT DISTINCT CLNDR_LVL_TYPE_ID
          FROM CLNDR_LVL
         WHERE CLNDR_ID = @ecp_clndr_id)
SELECT @errno = @@error
IF @errno <> 0
BEGIN
  SELECT @errmsg = 'Unable to determine lowest calendar level',
         @object_name = 'CLNDR_LVL_TYPE',
         @operation_name = 'SELECT'
  GOTO error
END

SELECT @to_reallocation_date = dateadd(ss, -1, min(cp.END_DATE_TIME))
  FROM CLNDR_PRD cp
 WHERE cp.END_DATE_TIME > @to_reallocation_date
   AND @ecp_clndr_id = cp.CLNDR_ID
   AND @lowest_calendar_level_id = cp.CLNDR_LVL_TYPE_ID
SELECT @errno = @@error
IF @errno <> 0
BEGIN
  SELECT @errmsg = 'Unable to determine period-end datetime associate with reallocation to date',
         @object_name = 'CLNDR_PRD',
         @operation_name = 'SELECT'
  GOTO error
END

IF @from_reallocation_date IS NOT NULL AND @to_reallocation_date IS NOT NULL
BEGIN
BEGIN TRANSACTION 
  UPDATE ecp_system_flag
     SET flag_datetime_value = @to_reallocation_date
   WHERE flag_name = 'ecp_reallocation_to_date'  
     AND flag_datetime_value IS NULL
  SELECT @errno = @@error, @rows = @@rowcount
  IF @errno <> 0 OR @rows <> 1
  BEGIN
    IF @rows <> 1 
      SELECT @errno = 201682, @message_id = 201682
    SELECT @errmsg = 'Unable to set reallocation request to date ',
           @object_name = 'ecp_system_flag',
           @operation_name = 'UPDATE'
    GOTO error
  END
  UPDATE ecp_system_flag
     SET flag_datetime_value = @from_reallocation_date
   WHERE flag_name = 'ecp_reallocation_from_date'  
     AND flag_datetime_value IS NULL
  SELECT @errno = @@error, @rows = @@rowcount
  IF @errno <> 0 OR @rows <> 1
  BEGIN
    IF @rows <> 1 
      SELECT @errno = 201682, @message_id = 201682
    SELECT @errmsg = 'Unable to set reallocation request from date ',
           @object_name = 'ecp_system_flag',
           @operation_name = 'UPDATE'
    GOTO error
  END
  IF @allocation_type_list IS NOT NULL
  BEGIN
    UPDATE ecp_system_flag
       SET flag_alpha_value = @allocation_type_list
     WHERE flag_name = 'ecp_reallocation_type_list'  
       AND flag_alpha_value IS NULL
    SELECT @errno = @@error, @rows = @@rowcount
    IF @errno <> 0 OR @rows <> 1
    BEGIN
      IF @rows <> 1 
        SELECT @errno = 201682, @message_id = 201682
      SELECT @errmsg = 'Unable to set reallocation request allocation type list ',
             @object_name = 'ecp_system_flag',
             @operation_name = 'UPDATE'
      GOTO error
    END
  END
 
  INSERT INTO ADT_TRL_HDR (
	 ENTRY_ID,
	 ENTRY_DATE_TIME,
	 USER_ID,
	 APP_ID,
	 ROOT_TBL_NAME,
	 ROOT_TBL_KEY,
	 ROOT_TBL_KEY_RSRC_NAME,
	 ROOT_TBL_KEY_RSRC_PRMS,
	 FNCTN_NUM)
  SELECT @ENTRY_ID,
	 getdate(), 
	 @user_id,
	 300,
	 'MNU_REALLOCATE',
	 'ecp_system_flag.ecp_reallocation_to_date',
	 'TK_EFFE_DATE',
	 dbo.convdate(@to_reallocation_date),
	 282
  SELECT @errno = @@error
  IF @errno <> 0
  BEGIN
    SELECT @errmsg = 'Unable to log ECP reallocation request to audit trail',
           @object_name = 'ADT_TRL_HDR',
           @operation_name = 'INSERT'
    GOTO error
  END

  INSERT into ADT_TRL_DTL(
       ENTRY_ID, 
       TBL_NAME, 
       TBL_KEY, 
       TBL_KEY_RSRC_NAME, 
       TBL_KEY_RSRC_PRMS, 
       ACTN_CODE, 
       CLMN_NAME, 
       NEW_VAL) 
  SELECT @ENTRY_ID,
       'ECP_SYSTEM_FLAG', 
       'flag_name', 
       'TK_AUDI_PRIM', 
       'ecp_reallocation_to_date', 
       'M',
       'TO_TRANSACTION_DATE', 
       dbo.convdate(@to_reallocation_date) 
  SELECT @errno = @@error
  IF @errno <> 0
  BEGIN
    SELECT @errmsg = 'Unable to log ECP reallocation request to-date to audit trail',
           @object_name = 'ADT_TRL_DTL',
           @operation_name = 'INSERT'
    GOTO error
  END

  INSERT into ADT_TRL_DTL(
       ENTRY_ID, 
       TBL_NAME, 
       TBL_KEY, 
       TBL_KEY_RSRC_NAME, 
       TBL_KEY_RSRC_PRMS, 
       ACTN_CODE, 
       CLMN_NAME, 
       NEW_VAL) 
  SELECT @ENTRY_ID,
       'ECP_SYSTEM_FLAG', 
       'flag_name', 
       'TK_AUDI_PRIM', 
       'ecp_reallocation_from_date', 
       'M',
       'COL_FROM_TRANSACTION_DATE', 
       dbo.convdate(@from_reallocation_date) 
  SELECT @errno = @@error
  IF @errno <> 0
  BEGIN
    SELECT @errmsg = 'Unable to log ECP reallocation request from-date to audit trail',
           @object_name = 'ADT_TRL_DTL',
           @operation_name = 'INSERT'
    GOTO error
  END

  INSERT into ADT_TRL_DTL(
       ENTRY_ID, 
       TBL_NAME, 
       TBL_KEY, 
       TBL_KEY_RSRC_NAME, 
       TBL_KEY_RSRC_PRMS, 
       ACTN_CODE, 
       CLMN_NAME, 
       NEW_VAL) 
  SELECT @ENTRY_ID,
       'ECP_SYSTEM_FLAG', 
       'flag_name', 
       'TK_AUDI_PRIM', 
       'ecp_reallocation_type_list', 
       'M',
       'COL_ALLOCATION_TYPES', 
       SUBSTRING(@allocation_type_list, 1, 1500)
  SELECT @errno = @@error
  IF @errno <> 0
  BEGIN
    SELECT @errmsg = 'Unable to log ECP reallocation request allocation type list to audit trail',
           @object_name = 'ADT_TRL_DTL',
           @operation_name = 'INSERT'
    GOTO error
  END

COMMIT TRANSACTION
END

UPDATE interface_status
     SET last_posting_datetime = getdate()
   WHERE interface_id = 44
  SELECT @errno = @@error
IF @errno <> 0
BEGIN
  SELECT @errmsg = 'Unable to indicate new information is available for the ECP posting',
         @object_name = 'interface_status',
         @operation_name = 'UPDATE'
  GOTO error
END

UPDATE interface_status
   SET immediate_posting_requested = 1
 WHERE interface_id = 44
   AND immediate_posting_requested = 0
SELECT @errno = @@error
IF @errno <> 0
BEGIN
  SELECT @errmsg = 'Unable to set ECP posting request',
         @object_name = 'interface_status',
         @operation_name = 'UPDATE'
  GOTO error
END

RETURN

error:
  EXEC common_error_handling_$sp @process_no, @errno, @errmsg, 0, @message_id, @process_name, @object_name, @operation_name, 1, @stream_no
  RETURN
```

