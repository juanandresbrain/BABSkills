# Job: ZRetired_WEB_StoreInventoryToDeckOMS

**Enabled:** No  
**Description:** Store Inventory to Deck is now part of Web - InventoryAndLocationsExports

## Architecture Diagram

```mermaid
flowchart LR
    JOB["ZRetired_WEB_StoreInventoryToDeckOMS"]
    JOB --> WEB_StoreInventoryBuffers_1["Step 1: WEB_StoreInventoryBuffers [SSIS]"]`n    JOB --> WEB_StoreInventoryToDeck_2["Step 2: WEB_StoreInventoryToDeck [SSIS]"]`n    JOB --> WEB_EnterpriseSellingStoreInventoryToOMS_3["Step 3: WEB_EnterpriseSellingStoreInventoryToOMS [SSIS]"]`n```

## Steps

### Step 1: WEB_StoreInventoryBuffers
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WEB\WEB_StoreInventoryBuffers\WEB_StoreInventoryBuffers.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10086 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: WEB_StoreInventoryToDeck
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WEB\Web_StoreInventoryToDeck\Web_StoreInventoryToDeck.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10175 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: WEB_EnterpriseSellingStoreInventoryToOMS
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WEB\WEB_EnterpriseSellingStoreInventoryToOMS\WEB_EnterpriseSellingStoreInventoryToOMS.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10088 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


