# Job: ProcessCubeDimensions

**Enabled:** Yes  
**Description:** No description available. Job is called by DWSales_DimensionImport on  STL-SQL-P-04\SQL2008R2 --LizzyT

## Architecture Diagram

```mermaid
flowchart LR
    JOB["ProcessCubeDimensions"]
    JOB --> ProcessCubeDimensions_1["Step 1: ProcessCubeDimensions [SSIS]"]`n    JOB --> Job_Completion_Notification_2["Step 2: Job Completion Notification [TSQL]"]`n```

## Steps

### Step 1: ProcessCubeDimensions
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\Cube\ProcessCube\ProcessCube.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10116 /Par "\"ProcessCube_DimensionsOrMeasures\"";Dimensions /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";3 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: Job Completion Notification
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobCompletion   @ProcessName = 'Process Cube Dimensions',   @SQLAgent = 'ProcessCubeDimensions',  @Recipients = 'biadmin@buildabear.com'
```


