# Job: zRetired_ExactTarget rerun only

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_ExactTarget rerun only"]
    JOB --> ExactTarget_1["Step 1: ExactTarget [SSIS]"]`n    JOB --> EmailFacts_2["Step 2: EmailFacts [SSIS]"]`n```

## Steps

### Step 1: ExactTarget
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\ExactTargetDownloadAndProcessETL\ExactTargetDownloadAndProcess.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10034 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: EmailFacts
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\EmailFactsETL\EmailFactsETL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10030 /Par "\"DaysToGoBack(Int32)\"";8 /Par "\"DaysToInclude(Int32)\"";8 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


