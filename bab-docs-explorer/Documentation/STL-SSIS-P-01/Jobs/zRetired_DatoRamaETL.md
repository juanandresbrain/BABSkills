# Job: zRetired_DatoRamaETL

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_DatoRamaETL"]
    JOB --> DatoRamaETL_1["Step 1: DatoRamaETL [SSIS]"]`n    JOB --> Job_Completion_Notice_2["Step 2: Job Completion Notice [TSQL]"]`n```

## Steps

### Step 1: DatoRamaETL
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\DatoRamaETL\DatoRamaETL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10100 /Par "\"Azure_Password\"";Omega8 /Par "\"Azure_ServerName\"";"\"asazure://northcentralus.asazure.windows.net/azasp01\"" /Par "\"Azure_UserName\"";"\"sqlservices@buildabear.com\"" /Par "\"DaysToGoBack(Int32)\"";31 /Par "\"DaysToInclude(Int32)\"";30 /Par ExecutionPath;EmailFacts /Par "\"SMTP_SmtpServer\"";"\"exstlhyb.buildabear.com\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: Job Completion Notice
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobCompletion   @ProcessName = 'DatoRamaETL',   @SQLAgent = 'DatoRamaETL',  @Recipients = 'biadmin@buildabear.com'
```


