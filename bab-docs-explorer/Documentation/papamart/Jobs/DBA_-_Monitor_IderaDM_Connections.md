# Job: DBA - Monitor IderaDM Connections

**Enabled:** Yes  
**Server:** papamart  
**Description:** Send Databears email if IderaDM has more than x spids on a server.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["DBA - Monitor IderaDM Connections"]
    JOB --> S1["Step 1: Check Counts [TSQL]"]
```

## Steps

### Step 1: Check Counts
**Subsystem:** TSQL  

```sql
IF (select COUNT(*) from master.dbo.sysprocesses
where RTRIM(program_name) = 'SQL diagnostic manager Collection Service' ) > 6
BEGIN
DECLARE @sbj VARCHAR(100)
SELECT @sbj = 'ERROR: IderaDM CMDShell issue on ' + @@servername

exec msdb.dbo.sp_send_dbmail @recipients = 'databears@buildabear.com', @subject = @sbj, 
@body = 'The IderaDM monitoring service is not working correctly. please check to see how many open sessions Idera is using.',
@query = 'select * from master.dbo.sysprocesses where RTRIM(program_name) = ''SQL diagnostic manager Collection Service''',
@attach_query_result_as_file = 1
END
```

