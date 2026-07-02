# Job: concurETL

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** After the concurETL_download runs, a scheduled task on stl-ssis-p01 named decrypt needs to run, it is scheduled 7:06am daily and will produce the SAE.txt file which this concurETL will consume.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["concurETL"]
    JOB --> daily_1["Step 1: daily [SSIS]"]`n```

## Steps

### Step 1: daily
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\HR\concurETL\concurETL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10061 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


