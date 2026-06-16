# Job: WMS_InventorySync_3PLToDynamics

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_InventorySync_3PLToDynamics"]
    JOB --> WMS_InventorySync_3PLToDynamics_1["Step 1: WMS_InventorySync_3PLToDynamics [SSIS]"]`n```

## Steps

### Step 1: WMS_InventorySync_3PLToDynamics
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_InventorySync_3PLtoDynamics\WMS_InventorySync_3PLtoDynamics.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10154 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


