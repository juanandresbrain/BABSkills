# Job: SQLServerAccountCleanup

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["SQLServerAccountCleanup"]
    JOB --> Run_SSIS____SQLServerAccountCleanup_1["Step 1: Run SSIS  - SQLServerAccountCleanup [SSIS]"]`n```

## Steps

### Step 1: Run SSIS  - SQLServerAccountCleanup
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\ADMIN\SQLServerAccountCleanup\SQLServerAccountCleanup.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10115 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


