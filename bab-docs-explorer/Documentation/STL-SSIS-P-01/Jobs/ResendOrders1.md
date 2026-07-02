# Job: ResendOrders1

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["ResendOrders1"]
    JOB --> SendWavedOrders_1["Step 1: SendWavedOrders [SSIS]"]`n```

## Steps

### Step 1: SendWavedOrders
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\WebOrderProcessing\ResendStatusUpdates.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


