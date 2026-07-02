# Job: zRetired_WEB - DynamicActionOrderHeaderAndLines

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_WEB - DynamicActionOrderHeaderAndLines"]
    JOB --> WebDynamicActionOrderHeaderAndLines_1["Step 1: WebDynamicActionOrderHeaderAndLines [SSIS]"]`n```

## Steps

### Step 1: WebDynamicActionOrderHeaderAndLines
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WEB\WebDynamicActionOrderHeaderAndLines\WebDynamicActionOrderHeaderAndLines.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10141 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


