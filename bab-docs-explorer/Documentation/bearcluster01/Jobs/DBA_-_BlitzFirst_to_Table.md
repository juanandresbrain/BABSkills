# Job: DBA - BlitzFirst to Table

**Enabled:** Yes  
**Server:** bearcluster01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["DBA - BlitzFirst to Table"]
    JOB --> Prune_Tables_1["Step 1: Prune Tables [TSQL]"]`n    JOB --> Execute_sp_BlitzFirst_2["Step 2: Execute sp_BlitzFirst [TSQL]"]`n```

## Steps

### Step 1: Prune Tables
**Subsystem:** TSQL  

```sql
DECLARE @DaysToKeep INT
SET @DaysToKeep = 7

delete
from BlitzCache
WHERE CheckDate < DATEADD(day,-(@DaysToKeep),GETDATE())
delete
from [BlitzFirst]
WHERE CheckDate < DATEADD(day,-(@DaysToKeep),GETDATE())
delete
from [BlitzFirst_FileStats]
WHERE CheckDate < DATEADD(day,-(@DaysToKeep),GETDATE())
delete
from [BlitzFirst_PerfmonStats]
WHERE CheckDate < DATEADD(day,-(@DaysToKeep),GETDATE())
delete
from [BlitzFirst_WaitStats]
WHERE CheckDate < DATEADD(day,-(@DaysToKeep),GETDATE())
```

### Step 2: Execute sp_BlitzFirst
**Subsystem:** TSQL  

```sql
IF sys.fn_hadr_backup_is_preferred_replica('DBAUtility') = 1
BEGIN
EXEC DBAUtility.dbo.sp_BlitzFirst 
  @OutputDatabaseName = 'DBAUtility', 
  @OutputSchemaName = 'dbo', 
  @OutputTableName = 'BlitzFirst',
  @OutputTableNameFileStats = 'BlitzFirst_FileStats',
  @OutputTableNamePerfmonStats = 'BlitzFirst_PerfmonStats',
  @OutputTableNameWaitStats = 'BlitzFirst_WaitStats',
  @OutputTableNameBlitzCache = 'BlitzCache';
END
```


