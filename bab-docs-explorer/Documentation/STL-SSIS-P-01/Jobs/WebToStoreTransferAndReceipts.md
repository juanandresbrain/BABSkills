# Job: WebToStoreTransferAndReceipts

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WebToStoreTransferAndReceipts"]
    JOB --> WebToStoreTransferAndReceipts_1["Step 1: WebToStoreTransferAndReceipts [SSIS]"]`n```

## Steps

### Step 1: WebToStoreTransferAndReceipts
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\WebToStoreTransferAndReceipts\WebToStoreTransferAndReceipts.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10027 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


