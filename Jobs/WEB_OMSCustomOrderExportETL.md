# Job: WEB_OMSCustomOrderExportETL

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB_OMSCustomOrderExportETL"]
    JOB --> WEB_OMSCustomOrderExportETL_1["Step 1: WEB_OMSCustomOrderExportETL [SSIS]"]`n    JOB --> Job_Completion_Notification_2["Step 2: Job Completion Notification [TSQL]"]`n```

## Steps

### Step 1: WEB_OMSCustomOrderExportETL
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WEB\WEB_OMSCustomOrderExportETL\WEB_OMSCustomOrderExportETL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10098 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: Job Completion Notification
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobCompletion   @ProcessName = 'Deck Custom Order Export / Nightly Summary',   @SQLAgent = 'WEB_OMSCustomOrderExportETL',  @Recipients = 'biadmin@buildabear.com'
```


