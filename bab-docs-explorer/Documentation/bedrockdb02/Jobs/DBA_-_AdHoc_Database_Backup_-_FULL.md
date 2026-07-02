# Job: DBA - AdHoc Database Backup - FULL

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Source: https://ola.hallengren.com

## Architecture Diagram

```mermaid
flowchart LR
    JOB["DBA - AdHoc Database Backup - FULL"]
    JOB --> DBA___DatabaseBackup___USER_DATABASES___FULL_1["Step 1: DBA - DatabaseBackup - USER_DATABASES - FULL [CmdExec]"]`n```

## Steps

### Step 1: DBA - DatabaseBackup - USER_DATABASES - FULL
**Subsystem:** CmdExec  

```sql
sqlcmd -E -S $(ESCAPE_SQUOTE(SRVR)) -d DBAUtility -Q "EXECUTE [dbo].[DatabaseBackup] @Databases = 'esell,me_01,ma_01,fn_01', @Directory = N'X:\Live2Test', @BackupType = 'FULL', @Verify = 'Y', @CleanupTime = 336, @CheckSum = 'Y', @LogToTable = 'Y'" -b
```


