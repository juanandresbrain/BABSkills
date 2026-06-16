# Job: zRetired_WMS_CostcoPurchaseOrdersToDynamics

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_WMS_CostcoPurchaseOrdersToDynamics"]
    JOB --> WMS_CostcoPurchaseOrdersToDynamics_1["Step 1: WMS_CostcoPurchaseOrdersToDynamics [SSIS]"]`n```

## Steps

### Step 1: WMS_CostcoPurchaseOrdersToDynamics
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_CostcoPurchaseOrdersToDynamics\WMS_CostcoPurchaseOrdersToDynamics.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10091 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


