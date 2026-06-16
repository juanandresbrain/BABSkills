# Job: WEB - InventoryDWLoad

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB - InventoryDWLoad"]
    JOB --> WebInventory_1["Step 1: WebInventory [SSIS]"]`n```

## Steps

### Step 1: WebInventory
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WEB\WebInventory\WebInventory.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10089 /Par "\"WebInventory_LoadDestination\"";DW /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


