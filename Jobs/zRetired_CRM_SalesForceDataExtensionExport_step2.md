# Job: zRetired_CRM_SalesForceDataExtensionExport_step2

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_CRM_SalesForceDataExtensionExport_step2"]
    JOB --> master_de_update_and_file_create_only_1["Step 1: master de update and file create only [SSIS]"]`n```

## Steps

### Step 1: master de update and file create only
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\CRMSalesForceDataExtensionFileCreate\CRMSalesForceDataExtensionFileCreate.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


