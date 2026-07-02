# Job: HR_Store_AD

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["HR_Store_AD"]
    JOB --> recurring_1["Step 1: recurring [SSIS]"]`n```

## Steps

### Step 1: recurring
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\HR\HR_Store_AD\HR_Store_AD.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


