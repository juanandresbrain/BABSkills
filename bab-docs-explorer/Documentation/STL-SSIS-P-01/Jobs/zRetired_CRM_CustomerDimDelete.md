# Job: zRetired_CRM_CustomerDimDelete

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_CRM_CustomerDimDelete"]
    JOB --> step1_1["Step 1: step1 [SSIS]"]`n```

## Steps

### Step 1: step1
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\CRM_CustomerDimDelete\CRM_CustomerDimDelete.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"CRM_AppServerName\"";"\"stl-crmapp-p-01\"" /Par "\"CRM_ServerName\"";"\"STL-CRMDB-P-01\"" /Par "\"DW_ServerName\"";papamart /Par ExactTargetFilePath;"\"\\STL-SQL-P-04\T$\FileRepository\ExactTarget\"" /Par "\"ExactTarget_ServerName\"";"\"stl-sql-p-04\"" /Par "\"IntegrationStaging_ServerName\"";"\"STL-SSIS-P-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


