# Job: New DBA - CommandLog Cleanup

**Enabled:** Yes  
**Server:** bearcluster01  
**Description:** Source: https://ola.hallengren.com

## Architecture Diagram

```mermaid
flowchart LR
    JOB["New DBA - CommandLog Cleanup"]
    JOB --> New_DBA___CommandLog_Cleanup_1["Step 1: New DBA - CommandLog Cleanup [TSQL]"]`n```

## Steps

### Step 1: New DBA - CommandLog Cleanup
**Subsystem:** TSQL  

```sql
IF sys.fn_hadr_backup_is_preferred_replica('DBAUtility') = 1
BEGIN
     DELETE FROM [dbo].[CommandLog] WHERE StartTime < DATEADD(dd,-30,GETDATE())
END
```


