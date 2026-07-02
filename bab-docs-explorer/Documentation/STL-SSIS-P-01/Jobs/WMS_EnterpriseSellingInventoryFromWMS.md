# Job: WMS_EnterpriseSellingInventoryFromWMS

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_EnterpriseSellingInventoryFromWMS"]
    JOB --> WMS_EnterpriseSellingInventoryFromWMS_1["Step 1: WMS_EnterpriseSellingInventoryFromWMS [SSIS]"]`n```

## Steps

### Step 1: WMS_EnterpriseSellingInventoryFromWMS
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_EnterpriseSellingInventoryFromWMS\WMS_EnterpriseSellingInventoryFromWMS.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10076 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


