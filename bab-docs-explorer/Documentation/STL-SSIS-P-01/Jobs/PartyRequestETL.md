# Job: PartyRequestETL

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** Replaces Party Request ETL on stl-sql-p-04\sql2008r2

## Architecture Diagram

```mermaid
flowchart LR
    JOB["PartyRequestETL"]
    JOB --> SSIS___PartyRequestETL_1["Step 1: SSIS - PartyRequestETL [SSIS]"]`n```

## Steps

### Step 1: SSIS - PartyRequestETL
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\PartyRequestETL\PartyRequestETl.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10127 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


