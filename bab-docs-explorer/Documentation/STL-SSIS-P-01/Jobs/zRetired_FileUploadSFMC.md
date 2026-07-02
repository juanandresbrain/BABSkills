# Job: zRetired_FileUploadSFMC

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** Upload Files from DM folder path to SFMC sftp

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_FileUploadSFMC"]
    JOB --> Run_FileUploadSFMC_ETL_1["Step 1: Run FileUploadSFMC ETL [SSIS]"]`n```

## Steps

### Step 1: Run FileUploadSFMC ETL
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\FileUploadSFMC\Package.dtsx\"" /SERVER "\"STL-SSIS-P-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


