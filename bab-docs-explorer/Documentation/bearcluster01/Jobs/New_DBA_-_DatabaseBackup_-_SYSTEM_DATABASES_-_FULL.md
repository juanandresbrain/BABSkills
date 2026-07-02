# Job: New DBA - DatabaseBackup - SYSTEM_DATABASES - FULL

**Enabled:** Yes  
**Server:** bearcluster01  
**Description:** Source: https://ola.hallengren.com

## Architecture Diagram

```mermaid
flowchart LR
    JOB["New DBA - DatabaseBackup - SYSTEM_DATABASES - FULL"]
    JOB --> New_DBA___DatabaseBackup___SYSTEM_DATABASES___FULL_1["Step 1: New DBA - DatabaseBackup - SYSTEM_DATABASES - FULL [CMDEXEC]"]`n```

## Steps

### Step 1: New DBA - DatabaseBackup - SYSTEM_DATABASES - FULL
**Subsystem:** CMDEXEC  

```sql
sqlcmd -E -S $(ESCAPE_SQUOTE(SRVR)) -d master -Q "EXECUTE [dbo].[DatabaseBackup] @Databases = 'SYSTEM_DATABASES', @Directory = N'\\stl-esxbak-p-32\sqlbackups', @BackupType = 'FULL', @Verify = 'Y', @CleanupTime = 72, @CheckSum = 'Y', @LogToTable = 'Y'" -b
```


