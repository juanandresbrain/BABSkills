# Job: DBA - CommandLog Cleanup

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Source: https://ola.hallengren.com

## Architecture Diagram

```mermaid
flowchart LR
    JOB["DBA - CommandLog Cleanup"]
    JOB --> New_DBA___CommandLog_Cleanup_1["Step 1: New DBA - CommandLog Cleanup [CMDEXEC]"]`n```

## Steps

### Step 1: New DBA - CommandLog Cleanup
**Subsystem:** CMDEXEC  

```sql
sqlcmd -E -S $(ESCAPE_SQUOTE(SRVR)) -d DBAUtility -Q "DELETE FROM [dbo].[CommandLog] WHERE StartTime < DATEADD(dd,-30,GETDATE())" -b
```


