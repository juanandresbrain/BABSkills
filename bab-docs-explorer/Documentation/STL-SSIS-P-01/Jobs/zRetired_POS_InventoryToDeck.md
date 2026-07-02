# Job: zRetired_POS_InventoryToDeck

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** this is still work in progress.. just building the agent...

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_POS_InventoryToDeck"]
    JOB --> StoreInventoryBuffers_1["Step 1: StoreInventoryBuffers [SSIS]"]`n```

## Steps

### Step 1: StoreInventoryBuffers
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WEB\WEB_StoreInventoryBuffers\WEB_StoreInventoryBuffers.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10086 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


