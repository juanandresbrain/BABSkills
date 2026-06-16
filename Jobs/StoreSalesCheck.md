# Job: StoreSalesCheck

**Enabled:** Yes  
**Description:** SalesAuditToDW PreStageTrigger runs this SSIS as step 1, then will call this SQL agent to run it again if needed.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["StoreSalesCheck"]
    JOB --> StoreSalesCheck_1["Step 1: StoreSalesCheck [SSIS]"]`n```

## Steps

### Step 1: StoreSalesCheck
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\DW\StoreSalesCheck\StoreSalesCheck.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10099 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


