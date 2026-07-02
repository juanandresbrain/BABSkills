# Job: Web_OrderIntegrationDataMonitor

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["Web_OrderIntegrationDataMonitor"]
    JOB --> Web_OrderIntegrationDataMonitor_1["Step 1: Web_OrderIntegrationDataMonitor [SSIS]"]`n    JOB --> Job_Completion_Notice_2["Step 2: Job Completion Notice [TSQL]"]`n```

## Steps

### Step 1: Web_OrderIntegrationDataMonitor
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\Azure\Web_OrderIntegrationDataMonitor\Web_OrderIntegrationDataMonitor.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10095 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: Job Completion Notice
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobCompletion   @ProcessName = 'Power BI Daily Web Order Integration Tracking',   @SQLAgent = 'Web_OrderIntegrationDataMonitor',  @Recipients = 'biadmin@buildabear.com'
```


