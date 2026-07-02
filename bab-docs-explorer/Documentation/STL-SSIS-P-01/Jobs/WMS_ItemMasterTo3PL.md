# Job: WMS_ItemMasterTo3PL

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_ItemMasterTo3PL"]
    JOB --> WMS_ItemMasterTo3PL_1["Step 1: WMS_ItemMasterTo3PL [SSIS]"]`n```

## Steps

### Step 1: WMS_ItemMasterTo3PL
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_ItemMasterTo3PL\WMS_ItemMasterTo3PL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10111 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


