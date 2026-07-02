# Job: CRM_voucherXML_ETL

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** this is initiated by agent job CRM_voucherValidation when vouchers processed in sales audit are validated

## Architecture Diagram

```mermaid
flowchart LR
    JOB["CRM_voucherXML_ETL"]
    JOB --> daily_1["Step 1: daily [SSIS]"]`n```

## Steps

### Step 1: daily
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\CRM_voucherXML_ETL\CRM_voucherXML_ETL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10156 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


