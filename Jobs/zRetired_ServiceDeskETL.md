# Job: zRetired_ServiceDeskETL

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_ServiceDeskETL"]
    JOB --> ServiceDeskETL_1["Step 1: ServiceDeskETL [SSIS]"]`n```

## Steps

### Step 1: ServiceDeskETL
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\Azure\ServiceDeskETL\ServiceDeskETL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10112 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


