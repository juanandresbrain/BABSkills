# Job: PCHealthChecks

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["PCHealthChecks"]
    JOB --> Run_SSIS___PCHealthChecks_1["Step 1: Run SSIS - PCHealthChecks [SSIS]"]`n```

## Steps

### Step 1: Run SSIS - PCHealthChecks
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\PCHealthChecks\PCHealthChecks.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10113 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


