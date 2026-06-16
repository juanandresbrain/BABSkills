# Job: zRetired_GiftCard Process_verify_only

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_GiftCard Process_verify_only"]
    JOB --> one_1["Step 1: one [SSIS]"]`n```

## Steps

### Step 1: one
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\DW\GiftCard_Process\GiftCard_Process.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"SMTP_SmtpServer\"";"\"exstlhyb.buildabear.com\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


