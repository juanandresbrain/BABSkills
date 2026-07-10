# Job: DBA - BlitzFirst to Table

**Enabled:** Yes  
**Server:** papamart  
**Description:** No description available.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["DBA - BlitzFirst to Table"]
    JOB --> S1["Step 1: Prune Tables [TSQL]"]
    S1 --> S2["Step 2: Execute sp_BlitzFirst [TSQL]"]
```

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
EXEC sp_BlitzFirst 
  @OutputDatabaseName = 'DBAUtility', 
  @OutputSchemaName = 'dbo', 
  @OutputTableName = 'BlitzFirst',
  @OutputTableNameFileStats = 'BlitzFirst_FileStats',
  @OutputTableNamePerfmonStats = 'BlitzFirst_PerfmonStats',
  @OutputTableNameWaitStats = 'BlitzFirst_WaitStats',
  @OutputTableNameBlitzCache = 'BlitzCache';
```

