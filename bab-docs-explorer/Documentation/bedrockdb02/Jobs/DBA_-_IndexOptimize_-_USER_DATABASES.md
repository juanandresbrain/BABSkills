# Job: DBA - IndexOptimize - USER_DATABASES

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Source: https://ola.hallengren.com

## Architecture Diagram

```mermaid
flowchart LR
    JOB["DBA - IndexOptimize - USER_DATABASES"]
    JOB --> New_DBA___IndexOptimize___USER_DATABASES_1["Step 1: New DBA - IndexOptimize - USER_DATABASES [CMDEXEC]"]`n```

## Steps

### Step 1: New DBA - IndexOptimize - USER_DATABASES
**Subsystem:** CMDEXEC  

```sql
sqlcmd -E -S $(ESCAPE_SQUOTE(SRVR)) -d DBAUtility -Q "EXECUTE [dbo].[IndexOptimize] @Databases = 'USER_DATABASES', @FragmentationLow = NULL,@FragmentationMedium = 'INDEX_REORGANIZE,INDEX_REBUILD_ONLINE,INDEX_REBUILD_OFFLINE',@FragmentationHigh = 'INDEX_REBUILD_ONLINE,INDEX_REBUILD_OFFLINE',@FragmentationLevel1 = 5,@FragmentationLevel2 = 30,@UpdateStatistics = 'ALL',@OnlyModifiedStatistics = 'Y',@LogToTable = 'Y'" -b

```


