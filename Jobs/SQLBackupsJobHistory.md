# Job: SQLBackupsJobHistory

**Enabled:** Yes  
**Description:** Runs hourly to capture sql agent history logs for sql backups. The reason it runs hourly is because some servers purge the history logs.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["SQLBackupsJobHistory"]
    JOB --> SQLBackupsJobHistory_1["Step 1: SQLBackupsJobHistory [SSIS]"]`n```

## Steps

### Step 1: SQLBackupsJobHistory
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\ADMIN\SQLBackupsJobHistory\SQLBackupsJobHistory.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10097 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


