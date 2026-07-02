# Job: DBA - DatabaseIntegrityCheck - USER_DATABASES

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Source: https://ola.hallengren.com

## Architecture Diagram

```mermaid
flowchart LR
    JOB["DBA - DatabaseIntegrityCheck - USER_DATABASES"]
    JOB --> New_DBA___DatabaseIntegrityCheck___USER_DATABASES_1["Step 1: New DBA - DatabaseIntegrityCheck - USER_DATABASES [CMDEXEC]"]`n```

## Steps

### Step 1: New DBA - DatabaseIntegrityCheck - USER_DATABASES
**Subsystem:** CMDEXEC  

```sql
sqlcmd -E -S $(ESCAPE_SQUOTE(SRVR)) -d DBAUtility -Q "EXECUTE [dbo].[DatabaseIntegrityCheck] @Databases = 'USER_DATABASES', @LogToTable = 'Y'" -b
DBA - Inclusive Log Cleanup Job	Yes	This backup job cleans different logs.
SET @Revision = '12/30/2013'	1	dbo.sp_delete_backuphistory	TSQL	DECLARE @CleanupDate datetime 
SET @CleanupDate = DATEADD(dd,-30,GETDATE()) 
EXECUTE dbo.sp_delete_backuphistory @oldest_date = @CleanupDate
DBA - Inclusive Log Cleanup Job	Yes	This backup job cleans different logs.
SET @Revision = '12/30/2013'	2	dbo.sp_purge_jobhistory	TSQL	EXEC DBAUtility.dbo.[spDBA_Delete_JobHistory]
DBA - Inclusive Log Cleanup Job	Yes	This backup job cleans different logs.
SET @Revision = '12/30/2013'	3	Process SQL Server Error Logs and Agent Logs	TSQL	EXEC dbo.spDBA_ReadErrorLog @ResultsToTable = 'Y'  
DBA - Inclusive Log Cleanup Job	Yes	This backup job cleans different logs.
SET @Revision = '12/30/2013'	4	Clean Up sysmail	TSQL	DECLARE @CleanupDate datetime 
SET @CleanupDate = DATEADD(dd,-30,GETDATE()) 

EXEC msdb.dbo.sysmail_delete_mailitems_sp @sent_before = @CleanupDate
EXEC msdb.dbo.sysmail_delete_log_sp @logged_before = @CleanupDate

DBA - Inclusive Log Cleanup Job	Yes	This backup job cleans different logs.
SET @Revision = '12/30/2013'	5	dbo.spDBA_Diskspace	TSQL	EXECUTE spDBA_Diskspace
DBA - Inclusive Log Cleanup Job	Yes	This backup job cleans different logs.
SET @Revision = '12/30/2013'	6	dbo.spDBA_JobStatusCheck	TSQL	EXEC spDBA_JobStatusCheck @DaysBack = 7 , @SQLVersion = 'SQL2005', @ResultsToTable = 'Y'

DBA - Inclusive Log Cleanup Job	Yes	This backup job cleans different logs.
SET @Revision = '12/30/2013'	7	Error Email	TSQL	DECLARE @sbj VARCHAR(100)
SET @sbj = 'ERROR: Job failure of [DBA - Inclusive Log Cleanup Job] on ' + @@SERVERNAME
exec DBAUtility.dbo.spDBA_SendEmail @recipients = 'Databears@buildabear.com', @subject = @sbj, @MessageTxt = 'The SQL job [DBA - Inclusive Log Cleanup Job] had an error.  Check the job history for more information'
```


