# Job: zRetired_CRM_bdayAutomation

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_CRM_bdayAutomation"]
    JOB --> bday_automation_1["Step 1: bday automation [SSIS]"]`n```

## Steps

### Step 1: bday automation
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\CRM_bdayAutomation\Package.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10114 /Par "\"CRM_ServerName\"";"\"stl-crmdb-p-01\"" /Par "\"IntegrationStaging_ServerName\"";"\"STL-SSIS-p-01\"" /Par "\"KodiakBABW_ServerName\"";kodiak /Par "\"SMTP_SmtpServer\"";"\"exstlhyb.buildabear.com\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


