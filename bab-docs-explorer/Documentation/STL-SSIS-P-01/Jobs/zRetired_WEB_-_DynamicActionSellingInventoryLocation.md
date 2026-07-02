# Job: zRetired_WEB - DynamicActionSellingInventoryLocation

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_WEB - DynamicActionSellingInventoryLocation"]
    JOB --> WebDynamicActionSellingInventoryLocation_1["Step 1: WebDynamicActionSellingInventoryLocation [SSIS]"]`n```

## Steps

### Step 1: WebDynamicActionSellingInventoryLocation
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WEB\WebDynamicActionSellingInventoryLocation\WebDynamicActionSellingInventoryLocation.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10143 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


