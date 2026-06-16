# Job: WEB - InventoryAndLocationsExports

**Enabled:** Yes  
**Description:** Job takes around 30 minutes to complete and we want it to run twice per hour, so I have it scheduled to run every minute

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB - InventoryAndLocationsExports"]
    JOB --> SSIS___UKWebInventory_1["Step 1: SSIS - UKWebInventory [SSIS]"]`n    JOB --> SSIS___WebInventory_2["Step 2: SSIS - WebInventory [SSIS]"]`n    JOB --> WEB_StoreInventoryBuffers_3["Step 3: WEB_StoreInventoryBuffers [SSIS]"]`n    JOB --> WEB_StoreInventoryToDeck_4["Step 4: WEB_StoreInventoryToDeck [SSIS]"]`n    JOB --> SSIS___Locations_5["Step 5: SSIS - Locations [SSIS]"]`n    JOB --> JobCompletionNotice_6["Step 6: JobCompletionNotice [TSQL]"]`n```

## Steps

### Step 1: SSIS - UKWebInventory
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WEB\UKWebInventory\UKWebInventory.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10102 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";3 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: SSIS - WebInventory
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WEB\WebInventory\WebInventory.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10089 /Par "\"LocationID(Int16)\"";0 /Par "\"WebInventory_LoadDestination\"";WEB /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";3 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: WEB_StoreInventoryBuffers
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WEB\WEB_StoreInventoryBuffers\WEB_StoreInventoryBuffers.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10086 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";3 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 4: WEB_StoreInventoryToDeck
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WEB\Web_StoreInventoryToDeck\Web_StoreInventoryToDeck.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10175 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 5: SSIS - Locations
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WEB\WebLocations\WebLocations.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10087 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 6: JobCompletionNotice
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobCompletion   @ProcessName = 'Web Locations and Inventory Exports (Web and Stores)',   @SQLAgent = 'WEB - InventoryAndLocationsExports',  @Recipients = 'biadmin@buildabear.com'
```


