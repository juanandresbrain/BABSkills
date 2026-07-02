# Job: zRetired_GalaTicketsEmail

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_GalaTicketsEmail"]
    JOB --> Daily_1["Step 1: Daily [SSIS]"]`n```

## Steps

### Step 1: Daily
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WEB\GalaTicketsEmail\GalaTicketsEmail.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


