# dbo.check_dayend_running_$sp

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.check_dayend_running_$sp"]
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| common_error_handling_$sp |

## Stored Procedure Code

```sql
create proc [dbo].[check_dayend_running_$sp] 

 @process_id            binary(16),
 @current_stream_no	int, -- dayend process id, 1= main SA db/single stream
 @action		int, -- 0 = called by check_dayend_periodend_$sp
 @status 		int OUTPUT -- @current_stream_running or @other_streams_running

AS

DECLARE

@db_id			int,
@errno			int,
@rdbms_process_id	int, -- spid that is running this proc
@stream_running		int,
@stream_name		nvarchar(25),
@current_db_name	nvarchar(25),
@other_db_name		nvarchar(25)

/* 
Name: check_dayend_running_$sp
Description:	This procedure will be used to check if the dayend is currently running.
		Called from day_end_posting_$sp, dayend_housekeeping_$sp, period_end_$sp, check_dayend_periodend_$sp.
		Used with multi-stream dayend to allow waiting for other streams to complete processing.

@action		Description									Returns
   0		Check to see if dayend is running on any stream for the current instance	  1 or 2
   1		Check to see if dayend is running on @current_stream_no		 		  1
   2		Check to see if dayend is running on any streams besides @current_stream_no.	  2

HISTORY
Date		 Name	Def#	Desc
Jan31,07         Paul     82449 check all streams when @action = 0
Nov18,05         Paul   DV-1323 allow n-tier to also call this proc by passing in @action = 0
Oct07,04        David   DV-1146 Pass null to user_id in common_error_handling_$sp.
                         /42301 Check context_info instead of login-name since users assigned to run  
                                smartload processes are user-defined in Smartload Var table maintenance.
May05,04       Maryam   DV-1071 Receive @process_id and user_name and pass it to common_error_handling_$sp
May03,02          Ian   1-CD0IX Add R3 Error Handling
Jul20,01	Henry	8286	Author. Replaces Defects 7493 and 8285 in Oracle.

*/

DECLARE	-- error handling
	@process_name		nvarchar(100),
	@process_no		smallint,
	@operation_name		nvarchar(100),
	@object_name		nvarchar(255),
	@message_id		int,
	@log_flag		tinyint,
	@rows                   numeric(12,0),
	@errmsg                 nvarchar(255),
	@function_name	        varbinary(128)

SELECT	@process_name = 'check_dayend_running_$sp',
	@message_id = 201068,
	@log_flag = 0,
	@process_no = 18,
	@function_name = convert(varbinary(128), 'auditworks_dayend' + convert(nvarchar, IsNull(@current_stream_no, 1)))

IF @action != 0 -- when called from dayend procs, set info to identify spid as a dayend process
  SET CONTEXT_INFO @function_name

SELECT	@status = 0,
	@stream_running = 0,
	@current_db_name = db_name(),
	@rdbms_process_id = @@spid

SELECT	@db_id = dbid -- dbid of current db
  FROM	master..sysprocesses
 WHERE	spid = @rdbms_process_id

SELECT @errno = @@error
IF @errno !=0
BEGIN
  SELECT @errmsg         = 'Failed to select from master..sysprocesses',
         @object_name    = 'master..sysprocesses',
         @operation_name = 'SELECT'
  GOTO error
END

SELECT @other_db_name = @current_db_name + '%'

IF @action IN (0,1)

-- Check to see if any other dayend processes are running for that same stream,
-- and in the same database.
  BEGIN

    IF EXISTS (SELECT 1
		 FROM master..sysprocesses
		WHERE context_info = @function_name
		  AND spid <> @rdbms_process_id
		  AND dbid = @db_id
		  AND db_name(dbid) = @current_db_name)
	SELECT @stream_running = 1

    SELECT @errno = @@error
    IF @errno != 0
	SELECT @stream_running = 99

  END -- IF @action in (0,1)

IF @action IN (0,2)
-- Check to see if any other dayend processes are running for any other streams,
-- (other streams are setup to run only in other databases with similar database name).
  BEGIN

    SELECT @stream_name = 'auditworks_dayend%'

    -- other streams in other databases
    IF EXISTS (SELECT 1
		 FROM master..sysprocesses
		WHERE context_info != @function_name
		  AND convert(nvarchar, context_info) LIKE @stream_name
		  AND spid <> @rdbms_process_id
		  AND db_name(dbid) != @current_db_name
		  AND db_name(dbid) LIKE @other_db_name)
	SELECT @stream_running = 2

    SELECT @errno = @@error
    IF @errno != 0
	SELECT @stream_running = 99

  END -- IF @action in (0,2)

SELECT @status = @stream_running

RETURN

error:

	EXEC common_error_handling_$sp @process_no, @errno, @errmsg, 0, @message_id,
	     @process_name, @object_name, @operation_name, @log_flag, 1, 0, null, 0,
	     null, null, null, null, null, null, 0, @process_id, null --
	     
	RETURN
```

