# Job: zRetired_Export New Time and Attendance Datafiles

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_Export New Time and Attendance Datafiles"]
    JOB --> Execute_SSIS_Package_1["Step 1: Execute SSIS Package [SSIS]"]`n```

## Steps

### Step 1: Execute SSIS Package
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\GenerateTnAReportsForStores\Package.dtsx\"" /SERVER "\"STL-SSIS-P-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


