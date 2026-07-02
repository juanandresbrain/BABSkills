# Job: WMS_PurchaseOrderToDynamics

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_PurchaseOrderToDynamics"]
    JOB --> Reset_Failed_POs_1["Step 1: Reset Failed POs [TSQL]"]`n    JOB --> WMS_PurchaseOrderToDynamics_2["Step 2: WMS_PurchaseOrderToDynamics [SSIS]"]`n```

## Steps

### Step 1: Reset Failed POs
**Subsystem:** TSQL  

```sql
exec wms.AptosToDynamicsResetForAPI
```

### Step 2: WMS_PurchaseOrderToDynamics
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_PurchaseOrderToDynamics\WMS_PurchaseOrderToDynamics.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10064 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


