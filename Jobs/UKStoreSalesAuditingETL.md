# Job: UKStoreSalesAuditingETL

**Enabled:** Yes  
**Description:** Scheduled to run at 3pm, which is 8pm store time during DST.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["UKStoreSalesAuditingETL"]
    JOB --> UKStoreSalesAuditingETL_SSIS_1["Step 1: UKStoreSalesAuditingETL SSIS [SSIS]"]`n```

## Steps

### Step 1: UKStoreSalesAuditingETL SSIS
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\UKStoreSalesAuditingETL\UKStoreSalesAuditingETL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10036 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


