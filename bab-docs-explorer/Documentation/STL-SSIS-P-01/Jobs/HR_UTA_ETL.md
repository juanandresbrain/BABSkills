# Job: HR_UTA_ETL

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** Runs UTA data import, merges labor hours fact and supporting tables, runs babwscore01 job Workbrain HOO Import, which also processes labor cube

## Architecture Diagram

```mermaid
flowchart LR
    JOB["HR_UTA_ETL"]
    JOB --> Get_UK_Clock_Data_from_Labor_Planner___Temporary_until_they_start_using_UltiPro__1["Step 1: Get UK Clock Data from Labor Planner ( Temporary until they start using UltiPro) [TSQL]"]`n    JOB --> HR_UTA_ETL_2["Step 2: HR_UTA_ETL [SSIS]"]`n    JOB --> Process_Cube_Labor_Dimensions_and_Measures_3["Step 3: Process Cube Labor Dimensions and Measures [SSIS]"]`n    JOB --> Job_Completion_Notice_4["Step 4: Job Completion Notice [TSQL]"]`n    JOB --> Run_WorkBrain_HOO_Import_on_Babwscore01_5["Step 5: Run WorkBrain HOO Import on Babwscore01 [CmdExec]"]`n```

## Steps

### Step 1: Get UK Clock Data from Labor Planner ( Temporary until they start using UltiPro)
**Subsystem:** TSQL  

```sql
DECLARE @cmd varchar(8000)  SET @cmd = 'SQLCMD -S BABWSCORE01 -E -Q "EXEC msdb..sp_start_job ''CA/UK Labor Import''"'    EXEC xp_cmdshell @cmd    waitfor delay '00:01:00'
```

### Step 2: HR_UTA_ETL
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\HR\HR_UTA_ETL\HR_UTA_ETL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10039 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: Process Cube Labor Dimensions and Measures
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\Cube\ProcessCube\ProcessCube.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10116 /Par "\"ProcessCube_DimensionsOrMeasures\"";LaborDimensions /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 4: Job Completion Notice
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobCompletion   @ProcessName = 'UltiPro Labor Import + Process Cube Labor',   @SQLAgent = 'HR_UTA_ETL',  @Recipients = 'biadmin@buildabear.com'
```

### Step 5: Run WorkBrain HOO Import on Babwscore01
**Subsystem:** CmdExec  

```sql
sqlcmd -E -S stl-sql-p-04\sql2008r2 -Q "EXEC msdb.dbo.sp_start_job @job_name=' Workbrain HOO Import'"
```


