# Job: ProcessCubeCRM

**Enabled:** Yes  
**Description:** --Job is called from CustomerTransactionETL, but only if the cube was already processed today and current time is before 6:30am.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["ProcessCubeCRM"]
    JOB --> ProcessCube_1["Step 1: ProcessCube [SSIS]"]`n    JOB --> Job_Completion_Notification_2["Step 2: Job Completion Notification [TSQL]"]`n```

## Steps

### Step 1: ProcessCube
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\Cube\ProcessCube\ProcessCube.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10116 /Par "\"ProcessCube_DimensionsOrMeasures\"";CRM /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: Job Completion Notification
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobCompletion   @ProcessName = 'Process Cube CRM',   @SQLAgent = 'ProcessCubeCRM',  @Recipients = 'biadmin@buildabear.com'
```


