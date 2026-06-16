# Job: WMS_StoreToStoreTransferExtract

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_StoreToStoreTransferExtract"]
    JOB --> SSIS___WMS_StoreToStoreTransferExtract_1["Step 1: SSIS - WMS_StoreToStoreTransferExtract [SSIS]"]`n```

## Steps

### Step 1: SSIS - WMS_StoreToStoreTransferExtract
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_StoreToStoreTransferExtract\WMS_StoreToStoreTransferExtract.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10171 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


