# Job: zRetired_WEB - DynamicAction_ProductAttributes

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_WEB - DynamicAction_ProductAttributes"]
    JOB --> DynamicAction_ProductAttributes_1["Step 1: DynamicAction_ProductAttributes [SSIS]"]`n```

## Steps

### Step 1: DynamicAction_ProductAttributes
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WEB\DynamicAction_ProductAttributes\DynamicAction_ProductAttributes.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10145 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


