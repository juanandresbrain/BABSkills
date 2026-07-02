# Job: EmailFactsETL

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["EmailFactsETL"]
    JOB --> EmailFactsETL_1["Step 1: EmailFactsETL [SSIS]"]`n```

## Steps

### Step 1: EmailFactsETL
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\EmailFactsETL\EmailFactsETL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10030 /Par "\"DaysToGoBack(Int32)\"";68 /Par "\"DaysToInclude(Int32)\"";68 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


