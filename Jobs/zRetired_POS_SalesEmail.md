# Job: zRetired_POS_SalesEmail

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_POS_SalesEmail"]
    JOB --> POS_SalesEmail_1["Step 1: POS_SalesEmail [SSIS]"]`n```

## Steps

### Step 1: POS_SalesEmail
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\POS\POS_SalesEmail\POS_SalesEmail.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10173 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


