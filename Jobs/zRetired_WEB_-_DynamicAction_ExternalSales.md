# Job: zRetired_WEB - DynamicAction_ExternalSales

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_WEB - DynamicAction_ExternalSales"]
    JOB --> DynamicAction_ExternalSales_1["Step 1: DynamicAction_ExternalSales [SSIS]"]`n```

## Steps

### Step 1: DynamicAction_ExternalSales
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WEB\DynamicAction_ExternalSales\DynamicAction_ExternalSales.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10144 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


