# Job: DW_FlashGaapSalesForAccounting

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["DW_FlashGaapSalesForAccounting"]
    JOB --> DW_FlashGaapSalesForAccounting_1["Step 1: DW_FlashGaapSalesForAccounting [SSIS]"]`n    JOB --> Job_Completion_Notification_2["Step 2: Job Completion Notification [TSQL]"]`n```

## Steps

### Step 1: DW_FlashGaapSalesForAccounting
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\DW\DW_FlashGaapSalesForAccounting\DW_FlashGaapSalesForAccounting.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10094 /Par "\"DaysToGoBack(Int32)\"";45 /Par "\"DaysToInclude(Int32)\"";45 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: Job Completion Notification
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobCompletion   @ProcessName = 'DW_FlashGaapSalesForAccounting',   @SQLAgent = 'DW_FlashGaapSalesForAccounting',  @Recipients = 'biadmin@buildabear.com'
```


