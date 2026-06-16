# Job: LoyaltyTransactionETLAv

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["LoyaltyTransactionETLAv"]
    JOB --> once_1["Step 1: once [SSIS]"]`n```

## Steps

### Step 1: once
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\Loyalty\LoyaltyTransactionETLAv\LoyaltyTransactionETLAv.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"Auditworks_ServerName\"";BEDROCKDB01 /Par "\"DWStaging_ServerName\"";papamart /Par "\"DW_ServerName\"";papamart /Par "\"SMTP_SmtpServer\"";"\"exstlhyb.buildabear.com\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


