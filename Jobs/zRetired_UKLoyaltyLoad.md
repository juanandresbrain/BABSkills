# Job: zRetired_UKLoyaltyLoad

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_UKLoyaltyLoad"]
    JOB --> LoadDataForUKLoyalty_1["Step 1: LoadDataForUKLoyalty [SSIS]"]`n```

## Steps

### Step 1: LoadDataForUKLoyalty
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\PowerBILoad\UKLoyaltyLoad.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10040 /Par "\"$Project::CM.SMTP Connection Manager.SmtpServer\"";"\"exstlhyb.buildabear.com\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


