# Job: Import Find-a-Bear IDs from WebOrders

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["Import Find-a-Bear IDs from WebOrders"]
    JOB --> Execute_SSIS_Package_1["Step 1: Execute SSIS Package [SSIS]"]`n```

## Steps

### Step 1: Execute SSIS Package
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\WebOrders\ExtractFindABearOrders.dtsx\"" /SERVER "\"STL-SSIS-P-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


