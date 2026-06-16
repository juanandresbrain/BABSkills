# Job: zRetired_SalesAuditToDW Delete Trigger

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_SalesAuditToDW Delete Trigger"]
    JOB --> SSIS___AuditworksToDWTriggerFile___Delete_Trigger_1["Step 1: SSIS - AuditworksToDWTriggerFile - Delete Trigger [SSIS]"]`n```

## Steps

### Step 1: SSIS - AuditworksToDWTriggerFile - Delete Trigger
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\DW\AuditworksToDWTriggerFile\AuditworksToDWTriggerFile.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10120 /Par WatchOrDelete;Delete /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


