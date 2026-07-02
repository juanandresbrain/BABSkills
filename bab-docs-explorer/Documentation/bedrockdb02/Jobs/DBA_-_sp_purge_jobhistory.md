# Job: DBA - sp_purge_jobhistory

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Source: https://ola.hallengren.com

## Architecture Diagram

```mermaid
flowchart LR
    JOB["DBA - sp_purge_jobhistory"]
    JOB --> New_DBA___sp_purge_jobhistory_1["Step 1: New DBA - sp_purge_jobhistory [CMDEXEC]"]`n```

## Steps

### Step 1: New DBA - sp_purge_jobhistory
**Subsystem:** CMDEXEC  

```sql
sqlcmd -E -S $(ESCAPE_SQUOTE(SRVR)) -d msdb -Q "DECLARE @CleanupDate datetime SET @CleanupDate = DATEADD(dd,-30,GETDATE()) EXECUTE dbo.sp_purge_jobhistory @oldest_date = @CleanupDate" -b
DBA - syspolicy_purge_history	Yes	SQL 2008 and above ONLY.
SET @Revision = '05/29/2012'	1	Verify that automation is enabled.	TSQL	IF (msdb.dbo.fn_syspolicy_is_automation_enabled() != 1)
        BEGIN
            RAISERROR(34022, 16, 1)
        END
DBA - syspolicy_purge_history	Yes	SQL 2008 and above ONLY.
SET @Revision = '05/29/2012'	2	Purge history.	TSQL	EXEC msdb.dbo.sp_syspolicy_purge_history
DBA - syspolicy_purge_history	Yes	SQL 2008 and above ONLY.
SET @Revision = '05/29/2012'	3	Erase Phantom System Health Records.	PowerShell	if ('$(ESCAPE_SQUOTE(INST))' -eq 'MSSQLSERVER') {$a = '\DEFAULT'} ELSE {$a = ''};
(Get-Item SQLSERVER:\SQLPolicy\$(ESCAPE_NONE(SRVR))$a).EraseSystemHealthPhantomRecords()
```


