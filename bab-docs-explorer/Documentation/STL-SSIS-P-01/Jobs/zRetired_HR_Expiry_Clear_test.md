# Job: zRetired_HR_Expiry_Clear_test

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_HR_Expiry_Clear_test"]
    JOB --> test_run_1["Step 1: test run [SSIS]"]`n```

## Steps

### Step 1: test run
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\HR\HR_expiryClear_test\HR_expiryClear_test.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


