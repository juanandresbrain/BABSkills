# Job: HR_ADemployeeExtract

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["HR_ADemployeeExtract"]
    JOB --> 1_1["Step 1: 1 [SSIS]"]`n```

## Steps

### Step 1: 1
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\HR\HR_ADEmployeeExtract\HR_ADEmployeeExtract.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


