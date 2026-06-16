# Job: zRetired_DatoRamaETL_MorningLoad

**Enabled:** No  
**Description:** This job creates DatoramaOfflineData.csv only and uploads to FTP destinatino.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_DatoRamaETL_MorningLoad"]
    JOB --> DatoRamaETL_PreFlight_Check_1["Step 1: DatoRamaETL_PreFlight Check [SSIS]"]`n    JOB --> DatoRamaETL_DatoramaOfflineData_2["Step 2: DatoRamaETL_DatoramaOfflineData [SSIS]"]`n    JOB --> Start_Job_DatoRamaKeyStoryETL_3["Step 3: Start Job DatoRamaKeyStoryETL [TSQL]"]`n    JOB --> JobCompletionNotice_4["Step 4: JobCompletionNotice [TSQL]"]`n```

## Steps

### Step 1: DatoRamaETL_PreFlight Check
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\DatoRamaETL_PreFlightCheck\DatoRamaETL_PreFlightCheck.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10125 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: DatoRamaETL_DatoramaOfflineData
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\DatoRamaETL\DatoRamaETL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10100 /Par "\"Azure_Password\"";Omega8 /Par "\"Azure_ServerName\"";"\"asazure://northcentralus.asazure.windows.net/azasp01\"" /Par "\"Azure_UserName\"";"\"sqlservices@buildabear.com\"" /Par "\"DaysToGoBack(Int32)\"";31 /Par "\"DaysToInclude(Int32)\"";30 /Par ExecutionPath;DatoramaOfflineData /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: Start Job DatoRamaKeyStoryETL
**Subsystem:** TSQL  

```sql
EXEC sp_start_job @job_name='DatoRamaKeyStoryETL'
```

### Step 4: JobCompletionNotice
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobCompletion   @ProcessName = 'DatoRamaETL_MorningLoad',   @SQLAgent = 'DatoRamaETL_MorningLoad',  @Recipients = 'biadmin@buildabear.com'
```


