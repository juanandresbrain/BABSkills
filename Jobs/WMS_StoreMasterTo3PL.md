# Job: WMS_StoreMasterTo3PL

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_StoreMasterTo3PL"]
    JOB --> WMS_StoreMasterTo3PL_1["Step 1: WMS_StoreMasterTo3PL [SSIS]"]`n```

## Steps

### Step 1: WMS_StoreMasterTo3PL
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_StoreMasterTo3PL\WMS_StoreMasterTo3PL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10109 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


