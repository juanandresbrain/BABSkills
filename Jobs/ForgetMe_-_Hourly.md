# Job: ForgetMe - Hourly

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["ForgetMe - Hourly"]
    JOB --> ForgetMe_Job_Check_1["Step 1: ForgetMe Job Check [TSQL]"]`n    JOB --> Load_Admin_Review_Records_2["Step 2: Load Admin Review Records [SSIS]"]`n    JOB --> LoadPII_3["Step 3: LoadPII [SSIS]"]`n```

## Steps

### Step 1: ForgetMe Job Check
**Subsystem:** TSQL  

```sql
DECLARE @jobCount AS INT, @jobName AS VARCHAR(250), @erroMessage AS VARCHAR(500)  SET @jobName = 'ForgetMe'  SELECT @jobCount =      COUNT(ja.job_id)  FROM msdb.dbo.sysjobactivity ja   LEFT JOIN msdb.dbo.sysjobhistory jh       ON ja.job_history_id = jh.instance_id  JOIN msdb.dbo.sysjobs j   ON ja.job_id = j.job_id  JOIN msdb.dbo.sysjobsteps js      ON ja.job_id = js.job_id      AND ISNULL(ja.last_executed_step_id,0)+1 = js.step_id  WHERE ja.session_id = (SELECT TOP 1 session_id FROM msdb.dbo.syssessions ORDER BY agent_start_date DESC)  AND start_execution_date is not null  AND stop_execution_date is null  AND j.Name = @jobName    IF(@jobCount > 0)  BEGIN   SET @erroMessage = 'Job ' + @jobName + ' is already running!'   RAISERROR(@erroMessage, 11, 1)  END
```

### Step 2: Load Admin Review Records
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\ForgetMe\RetrieveData\LoadAdminReviewRecords.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 22 /Par "\"CRM_ServerName\"";"\"stl-crmdb-p-01\"" /Par "\"DaysToGoBack(Int32)\"";1 /Par "\"DaysToInclude(Int32)\"";1 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: LoadPII
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\ForgetMe\RetrieveData\LoadPIIRecords.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 22 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


