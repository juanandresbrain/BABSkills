# Job: D365_Avalara

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["D365_Avalara"]
    JOB --> daily_1["Step 1: daily [SSIS]"]`n```

## Steps

### Step 1: daily
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\D365_Avalara\D365_Avalara.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


