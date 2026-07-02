# Job: WEB - DATA WAREHOUSE LOAD

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB - DATA WAREHOUSE LOAD"]
    JOB --> WebOrdersDataWarehouse_1["Step 1: WebOrdersDataWarehouse [SSIS]"]`n```

## Steps

### Step 1: WebOrdersDataWarehouse
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\WebOrdersDataWarehouse\WebOrdersDataWarehouse.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"DaysToPull(Int32)\"";30 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


