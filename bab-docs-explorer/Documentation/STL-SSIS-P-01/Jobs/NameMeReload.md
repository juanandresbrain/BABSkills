# Job: NameMeReload

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["NameMeReload"]
    JOB --> once_1["Step 1: once [SSIS]"]`n```

## Steps

### Step 1: once
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\CustomerTransactionETL_\CustomerTransactionETL_.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"Auditworks_ServerName\"";BEDROCKDB01 /Par CRMFileDirectory;"\"\\stl-crmapp-p-01\import\\"" /Par "\"CRM_ServerName\"";"\"STL-CRMDB-P-01\"" /Par "\"ControlFlag_RunFileCheck(Int32)\"";1 /Par "\"DWStaging_ServerName\"";papamart /Par "\"DW_ServerName\"";papamart /Par "\"KodiakBABW_ServerName\"";KODIAK /Par "\"MA_01_ServerName\"";bedrockdb02 /Par "\"SMTP_SmtpServer\"";"\"exstlhyb.buildabear.com\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


