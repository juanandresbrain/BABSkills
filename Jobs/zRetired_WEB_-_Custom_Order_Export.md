# Job: zRetired__WEB - Custom Order Export

**Enabled:** No  
**Description:** See new job WEB_OMSCustomOrderExportETL

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired__WEB - Custom Order Export"]
    JOB --> Custom_Order_Export_Import_1["Step 1: Custom Order Export Import [SSIS]"]`n```

## Steps

### Step 1: Custom Order Export Import
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\WebOrderProcessing\OMSCustomOrderExportImport.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 6 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


