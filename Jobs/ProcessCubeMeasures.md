# Job: ProcessCubeMeasures

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["ProcessCubeMeasures"]
    JOB --> Job_Start_Notice_1["Step 1: Job Start Notice [TSQL]"]`n    JOB --> ProcessCubeMeasures_2["Step 2: ProcessCubeMeasures [SSIS]"]`n    JOB --> Job_Completion_Notification_3["Step 3: Job Completion Notification [TSQL]"]`n```

## Steps

### Step 1: Job Start Notice
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobStart   @ProcessName = 'Process Cube Measures',   @SQLAgent = 'ProcessCubeMeasures',  @Recipients = 'biadmin@buildabear.com'
```

### Step 2: ProcessCubeMeasures
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\Cube\ProcessCube\ProcessCube.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10116 /Par "\"ProcessCube_DimensionsOrMeasures\"";Measures /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";3 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: Job Completion Notification
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobCompletion   @ProcessName = 'Process Cube Measures',   @SQLAgent = 'ProcessCubeMeassures',  @Recipients = 'biadmin@buildabear.com'
```


