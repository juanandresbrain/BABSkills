# Job: SQLServerServiceCheck

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["SQLServerServiceCheck"]
    JOB --> SQLServerServiceCheck_1["Step 1: SQLServerServiceCheck [SSIS]"]`n```

## Steps

### Step 1: SQLServerServiceCheck
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\ADMIN\SQLServerServiceCheck\SQLServerServiceCheck.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10147 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


