# Job: WMS_CartonsCancelledToHA

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_CartonsCancelledToHA"]
    JOB --> WMS_CartonsCancelledToHA_1["Step 1: WMS_CartonsCancelledToHA [SSIS]"]`n```

## Steps

### Step 1: WMS_CartonsCancelledToHA
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_CartonsCancelledToHA\WMS_CartonsCancelledToHA.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10073 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


