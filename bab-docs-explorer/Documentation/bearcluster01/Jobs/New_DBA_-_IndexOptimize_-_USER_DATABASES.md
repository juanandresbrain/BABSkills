# Job: New DBA - IndexOptimize - USER_DATABASES

**Enabled:** Yes  
**Server:** bearcluster01  
**Description:** Source: https://ola.hallengren.com

## Architecture Diagram

```mermaid
flowchart LR
    JOB["New DBA - IndexOptimize - USER_DATABASES"]
    JOB --> New_DBA___IndexOptimize___USER_DATABASES_1["Step 1: New DBA - IndexOptimize - USER_DATABASES [TSQL]"]`n```

## Steps

### Step 1: New DBA - IndexOptimize - USER_DATABASES
**Subsystem:** TSQL  

```sql
IF sys.fn_hadr_backup_is_preferred_replica('DBAUtility') = 1
BEGIN
     EXECUTE [dbo].[IndexOptimize] @Databases = 'USER_DATABASES', @LogToTable = 'Y',@FragmentationLow = NULL,@FragmentationMedium = 'INDEX_REORGANIZE,INDEX_REBUILD_ONLINE,INDEX_REBUILD_OFFLINE',@FragmentationHigh = 'INDEX_REBUILD_ONLINE,INDEX_REBUILD_OFFLINE',@FragmentationLevel1 = 5,@FragmentationLevel2 = 30,@UpdateStatistics = 'ALL',@OnlyModifiedStatistics = 'Y'
END
```


