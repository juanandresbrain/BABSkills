# Job: New DBA - DatabaseBackup - USER_DATABASES - DIFF

**Enabled:** Yes  
**Server:** bearcluster01  
**Description:** Source: https://ola.hallengren.com

## Architecture Diagram

```mermaid
flowchart LR
    JOB["New DBA - DatabaseBackup - USER_DATABASES - DIFF"]
    JOB --> DBA___DatabaseBackup___USER_DATABASES___DIFF_1["Step 1: DBA - DatabaseBackup - USER_DATABASES - DIFF [TSQL]"]`n```

## Steps

### Step 1: DBA - DatabaseBackup - USER_DATABASES - DIFF
**Subsystem:** TSQL  

```sql
IF sys.fn_hadr_backup_is_preferred_replica('DBAUtility') = 1
BEGIN
 EXECUTE [dbo].[DatabaseBackup] @Databases = 'USER_DATABASES', @Directory = N'\\stl-esxbak-p-32\sqlbackups', @BackupType = 'DIFF', @Verify = 'Y', @CleanupTime = 168, @CheckSum = 'Y', @LogToTable = 'Y'
END
```


