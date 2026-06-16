# Job: zRetired_CRM_voucherXMLcancelled_ETL

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_CRM_voucherXMLcancelled_ETL"]
    JOB --> daily_1["Step 1: daily [SSIS]"]`n```

## Steps

### Step 1: daily
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\CRM_voucherXMLcancel_ETL\CRM_voucherXMLcancel_ETL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10158 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


