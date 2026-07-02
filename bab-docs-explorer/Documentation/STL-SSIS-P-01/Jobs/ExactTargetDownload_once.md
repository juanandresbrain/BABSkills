# Job: ExactTargetDownload_once

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["ExactTargetDownload_once"]
    JOB --> 1_1["Step 1: 1 [SSIS]"]`n```

## Steps

### Step 1: 1
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\ExactTargetDownloadAndProcessETL\ExactTargetDownloadAndProcess.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10034 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


