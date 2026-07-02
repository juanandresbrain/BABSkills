# Job: AzurePowerBIDataCheck

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["AzurePowerBIDataCheck"]
    JOB --> AzureDataCheck_1["Step 1: AzureDataCheck [SSIS]"]`n```

## Steps

### Step 1: AzureDataCheck
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\Azure\AzurePowerBIDataCheck\AzurePowerBiDataCheck.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";3 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


