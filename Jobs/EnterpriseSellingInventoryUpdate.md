# Job: EnterpriseSellingInventoryUpdate

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["EnterpriseSellingInventoryUpdate"]
    JOB --> EnterpriseSellingInventoryUpdate_1["Step 1: EnterpriseSellingInventoryUpdate [SSIS]"]`n```

## Steps

### Step 1: EnterpriseSellingInventoryUpdate
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\EnterpriseSelling\EnterpriseSellingInventoryUpdate\EnterpriseSellingInventoryUpdate.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10057 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


