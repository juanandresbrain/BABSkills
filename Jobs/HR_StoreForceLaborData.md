# Job: HR_StoreForceLaborData

**Enabled:** Yes  
**Description:** Runs Labor Data (payroll) export and uploads to StoreForce sftp. Every other Tuesday after pay period ends.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["HR_StoreForceLaborData"]
    JOB --> HR_StoreforceLaborData_1["Step 1: HR_StoreforceLaborData [SSIS]"]`n```

## Steps

### Step 1: HR_StoreforceLaborData
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\HR\StoreForceLabor\Package.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"Auditworks_ServerName\"";bedrockdb01 /Par "\"CRM_ServerName\"";"\"stl-crmdb-p-01\"" /Par "\"DWStaging_ServerName\"";papamart /Par "\"DW_ServerName\"";papamart /Par "\"DaysToGoBack(Int32)\"";26 /Par "\"DaysToInclude(Int32)\"";13 /Par "\"IntegrationStaging_ServerName\"";"\"STL-SSIS-p-01\"" /Par "\"ME_01_ServerName\"";bedrockdb02 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


