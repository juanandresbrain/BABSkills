# Job: zRetired_ResumesETL

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_ResumesETL"]
    JOB --> ResumesETL_1["Step 1: ResumesETL [SSIS]"]`n```

## Steps

### Step 1: ResumesETL
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\Papamart\ResumesETL\ResumesETL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"DaysToGoBack(Int32)\"";3 /Par "\"DaysToInclude(Int32)\"";3 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


