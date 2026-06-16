# Job: WMS_NonWarehouseInventoryShrinkToAptos

**Enabled:** No  
**Description:** Syncs store inventory from Dynamics to Aptos, is triggered by sql agent MERCHANDISING - Process - Nightly Sync All Whse and Web

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_NonWarehouseInventoryShrinkToAptos"]
    JOB --> SSIS__WMS_NonWarehouseInventoryShrinkToAptos_1["Step 1: SSIS- WMS_NonWarehouseInventoryShrinkToAptos [SSIS]"]`n```

## Steps

### Step 1: SSIS- WMS_NonWarehouseInventoryShrinkToAptos
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_NonWarehouseInventoryShrinkToAptos\WMS_NonWarehouseInventoryShrinkToAptos.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10176 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


