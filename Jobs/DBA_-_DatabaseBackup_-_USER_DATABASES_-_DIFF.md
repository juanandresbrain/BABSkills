# Job: DBA - DatabaseBackup - USER_DATABASES - DIFF

**Enabled:** Yes  
**Description:** Source: https://ola.hallengren.com

## Architecture Diagram

```mermaid
flowchart LR
    JOB["DBA - DatabaseBackup - USER_DATABASES - DIFF"]
    JOB --> DBA___DatabaseBackup___USER_DATABASES___DIFF_1["Step 1: DBA - DatabaseBackup - USER_DATABASES - DIFF [CmdExec]"]`n```

## Steps

### Step 1: DBA - DatabaseBackup - USER_DATABASES - DIFF
**Subsystem:** CmdExec  

```sql
sqlcmd -E -S $(ESCAPE_SQUOTE(SRVR)) -d master -Q "EXECUTE [dbo].[DatabaseBackup] @Databases = 'USER_DATABASES', @Directory = N'\\stl-esxbak-p-32\sqlbackups\', @BackupType = 'DIFF', @Verify = 'Y', @CleanupTime = 168, @CheckSum = 'Y', @LogToTable = 'Y'" -b  
```


