# Job: zRetired_EmailFactRevCalc

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_EmailFactRevCalc"]
    JOB --> run_1["Step 1: run [SSIS]"]`n```

## Steps

### Step 1: run
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\EmailFactRevCalc\EmailFactRevCalc.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


