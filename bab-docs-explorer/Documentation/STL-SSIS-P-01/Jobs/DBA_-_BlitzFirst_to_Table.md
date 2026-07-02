# Job: DBA - BlitzFirst to Table

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["DBA - BlitzFirst to Table"]
    JOB --> Execute_sp_BlitzFirst_1["Step 1: Execute sp_BlitzFirst [TSQL]"]`n```

## Steps

### Step 1: Execute sp_BlitzFirst
**Subsystem:** TSQL  

```sql
EXEC sp_BlitzFirst     @OutputDatabaseName = 'DBAUtility',     @OutputSchemaName = 'dbo',     @OutputTableName = 'BlitzFirst',    @OutputTableNameFileStats = 'BlitzFirst_FileStats',    @OutputTableNamePerfmonStats = 'BlitzFirst_PerfmonStats',    @OutputTableNameWaitStats = 'BlitzFirst_WaitStats',    @OutputTableNameBlitzCache = 'BlitzCache';
```


