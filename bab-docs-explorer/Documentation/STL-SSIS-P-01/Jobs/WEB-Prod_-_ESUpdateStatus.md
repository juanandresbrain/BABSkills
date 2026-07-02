# Job: WEB-Prod - ESUpdateStatus

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB-Prod - ESUpdateStatus"]
    JOB --> ESUpdateStatus_1["Step 1: ESUpdateStatus [SSIS]"]`n```

## Steps

### Step 1: ESUpdateStatus
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\WebOrderProcessing\ESUpdateOrderStatus.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 6 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


