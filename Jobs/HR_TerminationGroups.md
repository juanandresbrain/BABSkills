# Job: HR_TerminationGroups

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["HR_TerminationGroups"]
    JOB --> hourly_1["Step 1: hourly [SSIS]"]`n```

## Steps

### Step 1: hourly
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\HR\HR_TerminationGroups\HR_TerminationGroups.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


