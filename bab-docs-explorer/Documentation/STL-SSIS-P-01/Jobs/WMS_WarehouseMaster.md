# Job: WMS_WarehouseMaster

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_WarehouseMaster"]
    JOB --> WMS_WarehouseMaster_1["Step 1: WMS_WarehouseMaster [SSIS]"]`n```

## Steps

### Step 1: WMS_WarehouseMaster
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_WarehouseMaster\WMS_WarehouseMaster.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10082 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


