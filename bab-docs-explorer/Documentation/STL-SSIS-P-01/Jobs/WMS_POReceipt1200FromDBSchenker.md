# Job: WMS_POReceipt1200FromDBSchenker

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_POReceipt1200FromDBSchenker"]
    JOB --> WMS_POReceipt1200FromDBSchenker_1["Step 1: WMS_POReceipt1200FromDBSchenker [SSIS]"]`n```

## Steps

### Step 1: WMS_POReceipt1200FromDBSchenker
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_POReceipt1200FromDBSchenker\WMS_POReceipt1200FromDBSchenker.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10067 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


