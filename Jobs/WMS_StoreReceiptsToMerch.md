# Job: WMS_StoreReceiptsToMerch

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_StoreReceiptsToMerch"]
    JOB --> SSIS___WMS_StoreReceiptsToMerch_1["Step 1: SSIS - WMS_StoreReceiptsToMerch [SSIS]"]`n```

## Steps

### Step 1: SSIS - WMS_StoreReceiptsToMerch
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_StoreReceiptsToMerch\WMS_StoreReceiptsToMerch.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10165 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


