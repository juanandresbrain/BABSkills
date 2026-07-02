# Job: zRetiredEmailFactsETL_reload

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetiredEmailFactsETL_reload"]
    JOB --> run_1["Step 1: run [SSIS]"]`n```

## Steps

### Step 1: run
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\EmailFactsETL_once\EmailFactsETL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"DWStaging_ServerName\"";papamart /Par "\"DW_ServerName\"";papamart /Par "\"DaysToGoBack(Int32)\"";32 /Par "\"DaysToInclude(Int32)\"";7 /Par "\"ESPStaging_ServerName\"";"\"stl-sql-p-04\"" /Par "\"IntegrationStaging_ServerName\"";"\"STL-SSIS-P-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


