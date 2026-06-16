# Job: ZRetiredExactTargetUploadAndProcess

**Enabled:** No  
**Description:** Disabled - Called from job EXEC sp_start_job @job_name='ExactTargetUploadAndProcess', which is called from CustomerTransactionETL

## Architecture Diagram

```mermaid
flowchart LR
    JOB["ZRetiredExactTargetUploadAndProcess"]
    JOB --> Run_ExactTargetDownloadAndProcess_ETL_1["Step 1: Run ExactTargetDownloadAndProcess ETL [SSIS]"]`n    JOB --> Job_Completion_Email_2["Step 2: Job Completion Email [TSQL]"]`n```

## Steps

### Step 1: Run ExactTargetDownloadAndProcess ETL
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\ExactTargetDownloadAndProcessETL\ExactTargetDownloadAndProcess.dtsx\"" /SERVER "\"STL-SSIS-P-01\"" /ENVREFERENCE 10034 /Par "\"ExactTarget_RunDownload(Boolean)\"";False /Par "\"ExactTarget_RunUpload(Boolean)\"";True /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: Job Completion Email
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobCompletion   @ProcessName = 'ExactTarget Upload from CRM',   @SQLAgent = 'ExactTargetUploadAndProcess',  @Recipients = 'biadmin@buildabear.com'
```


