# Job: WMS_InventorySync

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** Job takes around 30 minutes to complete and we want it to run twice per hour, so I have it scheduled to run every minute

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_InventorySync"]
    JOB --> WMS_InventorySync_1["Step 1: WMS_InventorySync [SSIS]"]`n```

## Steps

### Step 1: WMS_InventorySync
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_InventorySync\WMS_InventorySync.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10063 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


