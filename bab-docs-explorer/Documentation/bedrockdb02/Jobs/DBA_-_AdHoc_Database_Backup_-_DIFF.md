# Job: DBA - AdHoc Database Backup - DIFF

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Source: https://ola.hallengren.com

## Architecture Diagram

```mermaid
flowchart LR
    JOB["DBA - AdHoc Database Backup - DIFF"]
    JOB --> DBA___DatabaseBackup___USER_DATABASES___DIFF_1["Step 1: DBA - DatabaseBackup - USER_DATABASES - DIFF [CmdExec]"]`n```

## Steps

### Step 1: DBA - DatabaseBackup - USER_DATABASES - DIFF
**Subsystem:** CmdExec  

```sql
sqlcmd -E -S $(ESCAPE_SQUOTE(SRVR)) -d DBAUtility -Q "EXECUTE [dbo].[DatabaseBackup] @Databases = 'esell,me_01,ma_01,fn_01', @Directory = N'X:\Live2Test', @BackupType = 'DIFF', @Verify = 'Y', @CleanupTime = 168, @CheckSum = 'Y', @LogToTable = 'Y'" -b
```


