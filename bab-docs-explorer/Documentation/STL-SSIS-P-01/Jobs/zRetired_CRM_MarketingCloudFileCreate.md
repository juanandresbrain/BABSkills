# Job: zRetired_CRM_MarketingCloudFileCreate

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_CRM_MarketingCloudFileCreate"]
    JOB --> daily_delta_1["Step 1: daily delta [SSIS]"]`n```

## Steps

### Step 1: daily delta
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\CRMmarketingCloudFileCreate\CRMmarketingCloudFileCreate.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"SMTP_SmtpServer\"";"\"exstlhyb.buildabear.com\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


