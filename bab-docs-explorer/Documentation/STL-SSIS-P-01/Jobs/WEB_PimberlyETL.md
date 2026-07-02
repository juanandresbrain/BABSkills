# Job: WEB_PimberlyETL

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB_PimberlyETL"]
    JOB --> one_1["Step 1: one [SSIS]"]`n    JOB --> notification_2["Step 2: notification [TSQL]"]`n```

## Steps

### Step 1: one
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WEB\WEB_PimberlyETL\WEB_PimberlyETL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10157 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: notification
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobCompletion  @ProcessName = 'PIM Catalog Stage',  @SQLAgent = 'WEB_PimberlyETL',  @Recipients = 'BIAdmin@buildabear.com'    
```


