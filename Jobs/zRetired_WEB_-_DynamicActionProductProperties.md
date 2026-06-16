# Job: zRetired_WEB - DynamicActionProductProperties

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_WEB - DynamicActionProductProperties"]
    JOB --> WebDynamicActionProductProperties_1["Step 1: WebDynamicActionProductProperties [SSIS]"]`n    JOB --> SQL_Agent_Call___WEB___DynamicActionSellingInventoryLocation_2["Step 2: SQL Agent Call - WEB - DynamicActionSellingInventoryLocation [TSQL]"]`n    JOB --> SQL_Agent_Call___WEB___DynamicActionOrderHeaderAndLines_3["Step 3: SQL Agent Call - WEB - DynamicActionOrderHeaderAndLines [TSQL]"]`n```

## Steps

### Step 1: WebDynamicActionProductProperties
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WEB\WebDynamicActionProductProperties\WebDynamicActionProductProperties.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10142 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: SQL Agent Call - WEB - DynamicActionSellingInventoryLocation
**Subsystem:** TSQL  

```sql
EXEC [STL-SSIS-P-01].msdb.dbo.sp_start_job @job_name='WEB - DynamicActionSellingInventoryLocation'
```

### Step 3: SQL Agent Call - WEB - DynamicActionOrderHeaderAndLines
**Subsystem:** TSQL  

```sql
EXEC [STL-SSIS-P-01].msdb.dbo.sp_start_job @job_name='WEB - DynamicActionOrderHeaderAndLines'
```


