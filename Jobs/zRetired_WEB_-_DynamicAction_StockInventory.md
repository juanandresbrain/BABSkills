# Job: zRetired_WEB - DynamicAction_StockInventory

**Enabled:** No  
**Description:** Runs:  -InventorySync from Dynamics to IntegrationStaging  -WebInventory - Uses locationID 0 so it will only merge web.InventoryFact, but will not export a file  -DynamicAction_StockInventory - exports US and UK Web and Store Inventory Files to FTP  *Note: The store inventory from Enterprise Selling is running hourly in another job so we are as current as that job

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_WEB - DynamicAction_StockInventory"]
    JOB --> WMS_InventorySync_1["Step 1: WMS_InventorySync [SSIS]"]`n    JOB --> WebInventoryFact_UpdateWebOnly_2["Step 2: WebInventoryFact_UpdateWebOnly [SSIS]"]`n    JOB --> DynamicAction_StockInventory_3["Step 3: DynamicAction_StockInventory [SSIS]"]`n```

## Steps

### Step 1: WMS_InventorySync
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_InventorySync\WMS_InventorySync.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10063 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: WebInventoryFact_UpdateWebOnly
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WEB\WebInventory\WebInventory.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10089 /Par LoadType;FULL /Par "\"LocationID(Int16)\"";0 /Par "\"WebInventory_LoadDestination\"";WEB /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: DynamicAction_StockInventory
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WEB\DynamicAction_StockInventory\DynamicAction_StockInventory.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10146 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


