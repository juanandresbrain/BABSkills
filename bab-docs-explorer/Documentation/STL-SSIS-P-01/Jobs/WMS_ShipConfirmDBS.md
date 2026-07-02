# Job: WMS_ShipConfirmDBS

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_ShipConfirmDBS"]
    JOB --> WMS_ShipConfirmDBS_1["Step 1: WMS_ShipConfirmDBS [SSIS]"]`n```

## Steps

### Step 1: WMS_ShipConfirmDBS
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_ShipConfirmDBS\WMS_ShipConfirmDBS.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10070 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


