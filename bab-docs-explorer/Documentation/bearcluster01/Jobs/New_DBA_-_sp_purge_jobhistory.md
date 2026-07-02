# Job: New DBA - sp_purge_jobhistory

**Enabled:** Yes  
**Server:** bearcluster01  
**Description:** Source: https://ola.hallengren.com

## Architecture Diagram

```mermaid
flowchart LR
    JOB["New DBA - sp_purge_jobhistory"]
    JOB --> New_DBA___sp_purge_jobhistory_1["Step 1: New DBA - sp_purge_jobhistory [TSQL]"]`n```

## Steps

### Step 1: New DBA - sp_purge_jobhistory
**Subsystem:** TSQL  

```sql
IF sys.fn_hadr_backup_is_preferred_replica('DBAUtility') = 1
BEGIN
     DECLARE @CleanupDate datetime SET @CleanupDate = DATEADD(dd,-30,GETDATE()) EXECUTE msdb.dbo.sp_purge_jobhistory @oldest_date = @CleanupDate
END
```


