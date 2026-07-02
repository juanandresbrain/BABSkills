# Job: ZRetired_CRM_UKcompareValidation

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["ZRetired_CRM_UKcompareValidation"]
    JOB --> daily_1["Step 1: daily [SSIS]"]`n```

## Steps

### Step 1: daily
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\CRM_UKcompareValidation\CRM_UKcompareValidation.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"CRM_AppServerName\"";"\"stl-crmapp-p-01\"" /Par "\"CRM_ServerName\"";"\"STL-CRMDB-P-01\"" /Par "\"DW_ServerName\"";papamart /Par ExactTargetFilePath;"\"\\STL-SQL-P-04\T$\FileRepository\ExactTarget\"" /Par "\"ExactTarget_ServerName\"";"\"stl-sql-p-04\"" /Par "\"IntegrationStaging_ServerName\"";"\"STL-SSIS-P-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


