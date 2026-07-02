# Job: ActualVsEarned

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["ActualVsEarned"]
    JOB --> ActualVsEarned_SSIS_1["Step 1: ActualVsEarned SSIS [SSIS]"]`n```

## Steps

### Step 1: ActualVsEarned SSIS
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\DW\ActualVsEarned\ActualVsEarned.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10026 /Par "\"DaysToGoBack(Int32)\"";70 /Par "\"DaysToInclude(Int32)\"";70 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


