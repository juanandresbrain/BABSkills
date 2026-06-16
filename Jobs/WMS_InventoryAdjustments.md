# Job: WMS_InventoryAdjustments

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_InventoryAdjustments"]
    JOB --> WMS_InventoryAdjustments_1["Step 1: WMS_InventoryAdjustments [SSIS]"]`n```

## Steps

### Step 1: WMS_InventoryAdjustments
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_InventoryAdjustments\WMS_InventoryAdjustments.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10074 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


