# Job: zRetired_ProcessPowerBI

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_ProcessPowerBI"]
    JOB --> ProcessBAB_DW_1["Step 1: ProcessBAB-DW [SSIS]"]`n```

## Steps

### Step 1: ProcessBAB-DW
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\PowerBIProcessing\FullModelProcess.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10046 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


