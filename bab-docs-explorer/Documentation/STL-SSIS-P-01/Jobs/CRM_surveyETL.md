# Job: CRM_surveyETL

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["CRM_surveyETL"]
    JOB --> daily_1["Step 1: daily [SSIS]"]`n    JOB --> Start_Job___AzureProcessing_CRMSurvey_2["Step 2: Start Job - AzureProcessing_CRMSurvey [TSQL]"]`n```

## Steps

### Step 1: daily
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\CRM_SurveyETL\CRM_surveyETL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: Start Job - AzureProcessing_CRMSurvey
**Subsystem:** TSQL  

```sql
EXEC [stl-ssis-p-02].msdb.dbo.sp_start_job @job_name='AzureProcessing_CRMSurvey'  
```


