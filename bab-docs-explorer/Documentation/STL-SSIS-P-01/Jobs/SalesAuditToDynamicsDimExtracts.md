# Job: SalesAuditToDynamicsDimExtracts

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["SalesAuditToDynamicsDimExtracts"]
    JOB --> SSIS___SalesAuditToDynamicsDimExtracts_1["Step 1: SSIS - SalesAuditToDynamicsDimExtracts [SSIS]"]`n```

## Steps

### Step 1: SSIS - SalesAuditToDynamicsDimExtracts
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\SalesAuditToDynamicsDimExtracts\SalesAuditToDynamicsDimExtracts.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10164 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


