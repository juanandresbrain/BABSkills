# Job: HR_temp

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["HR_temp"]
    JOB --> temp_1["Step 1: temp [SSIS]"]`n```

## Steps

### Step 1: temp
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\HR\HR_ADEmployeeExtract\HR_ADEmployeeExtract.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10052 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


