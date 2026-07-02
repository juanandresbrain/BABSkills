# Job: WMS_InventoryAdjustments_3PLtoDynamics

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_InventoryAdjustments_3PLtoDynamics"]
    JOB --> WMS_InventoryAdjustments_3PLtoDynamics_1["Step 1: WMS_InventoryAdjustments_3PLtoDynamics [SSIS]"]`n```

## Steps

### Step 1: WMS_InventoryAdjustments_3PLtoDynamics
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_InventoryAdjustments_3PLtoDynamics\WMS_InventoryAdjustments_3PLtoDynamics.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10153 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


