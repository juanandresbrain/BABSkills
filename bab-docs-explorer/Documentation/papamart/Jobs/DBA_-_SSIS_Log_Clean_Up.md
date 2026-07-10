# Job: DBA - SSIS Log Clean Up

**Enabled:** Yes  
**Server:** papamart  
**Description:** Fire Proc to clean up SSIS Logging.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["DBA - SSIS Log Clean Up"]
    JOB --> S1["Step 1: spDBA_SSISLogCleanup [TSQL]"]
```

## Steps

### Step 1: spDBA_SSISLogCleanup
**Subsystem:** TSQL  

```sql
EXEC DBAUtility.dbo.spDBA_SSISLogCleanup
```

