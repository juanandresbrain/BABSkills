# Job: DBA - IndexOptimize - USER_DATABASES

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["DBA - IndexOptimize - USER_DATABASES"]
    JOB --> IndexOptimize_1["Step 1: IndexOptimize [CmdExec]"]`n```

## Steps

### Step 1: IndexOptimize
**Subsystem:** CmdExec  

```sql
sqlcmd -E -S $(ESCAPE_SQUOTE(SRVR)) -d DBAUtility -Q "EXECUTE [dbo].[IndexOptimize] @Databases = 'USER_DATABASES', @FragmentationLow = NULL,@FragmentationMedium = 'INDEX_REORGANIZE,INDEX_REBUILD_ONLINE,INDEX_REBUILD_OFFLINE',@FragmentationHigh = 'INDEX_REBUILD_ONLINE,INDEX_REBUILD_OFFLINE',@FragmentationLevel1 = 5,@FragmentationLevel2 = 30,@UpdateStatistics = 'ALL',@OnlyModifiedStatistics = 'Y',@LogToTable = 'Y'" -b
```


