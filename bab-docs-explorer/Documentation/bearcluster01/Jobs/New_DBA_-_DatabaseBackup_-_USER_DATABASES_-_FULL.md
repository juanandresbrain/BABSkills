# Job: New DBA - DatabaseBackup - USER_DATABASES - FULL

**Enabled:** Yes  
**Server:** bearcluster01  
**Description:** Source: https://ola.hallengren.com

## Architecture Diagram

```mermaid
flowchart LR
    JOB["New DBA - DatabaseBackup - USER_DATABASES - FULL"]
    JOB --> New_DBA___DatabaseBackup___USER_DATABASES___FULL_1["Step 1: New DBA - DatabaseBackup - USER_DATABASES - FULL [TSQL]"]`n```

## Steps

### Step 1: New DBA - DatabaseBackup - USER_DATABASES - FULL
**Subsystem:** TSQL  

```sql
IF sys.fn_hadr_backup_is_preferred_replica('DBAUtility') = 1
BEGIN
	EXECUTE [dbo].[DatabaseBackup] @Databases = 'USER_DATABASES', @Directory = N'\\stl-esxbak-p-32\sqlbackups', @BackupType = 'FULL', @Verify = 'Y', @CleanupTime = 72, @CheckSum = 'Y', @CopyOnly = 'Y', @LogToTable = 'Y'
END
```


