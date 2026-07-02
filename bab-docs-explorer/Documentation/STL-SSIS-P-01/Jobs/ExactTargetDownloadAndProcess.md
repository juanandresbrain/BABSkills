# Job: ExactTargetDownloadAndProcess

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["ExactTargetDownloadAndProcess"]
    JOB --> Run_ExactTargetDownloadAndProcess_ETL_1["Step 1: Run ExactTargetDownloadAndProcess ETL [SSIS]"]`n    JOB --> CustomerTransactionETL_2["Step 2: CustomerTransactionETL [CmdExec]"]`n```

## Steps

### Step 1: Run ExactTargetDownloadAndProcess ETL
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\ExactTargetDownloadAndProcessETL\ExactTargetDownloadAndProcess.dtsx\"" /SERVER "\"STL-SSIS-P-01\"" /ENVREFERENCE 10034 /Par "\"ExactTarget_RunDownload(Boolean)\"";True /Par "\"ExactTarget_RunUpload(Boolean)\"";False /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: CustomerTransactionETL
**Subsystem:** CmdExec  

```sql
sqlcmd -E -S stl-ssis-p-01 -Q "EXEC msdb.dbo.sp_start_job @job_name='CustomerTransactionETL'"
```


