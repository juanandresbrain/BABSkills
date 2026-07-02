# Job: ERP_AmExETL

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["ERP_AmExETL"]
    JOB --> process_1["Step 1: process [SSIS]"]`n```

## Steps

### Step 1: process
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\ERP\ERP_AmExETL\Package.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


