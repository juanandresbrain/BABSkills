# Job: DBA - DatabaseBackup - SYSTEM_DATABASES - FULL

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** Source: https://ola.hallengren.com

## Architecture Diagram

```mermaid
flowchart LR
    JOB["DBA - DatabaseBackup - SYSTEM_DATABASES - FULL"]
    JOB --> DBA___DatabaseBackup___SYSTEM_DATABASES___FULL_1["Step 1: DBA - DatabaseBackup - SYSTEM_DATABASES - FULL [CmdExec]"]`n```

## Steps

### Step 1: DBA - DatabaseBackup - SYSTEM_DATABASES - FULL
**Subsystem:** CmdExec  

```sql
sqlcmd -E -S $(ESCAPE_SQUOTE(SRVR)) -d master -Q "EXECUTE [dbo].[DatabaseBackup] @Databases = 'SYSTEM_DATABASES', @Directory = N'\\stl-esxbak-p-32\sqlbackups\', @BackupType = 'FULL', @Verify = 'Y', @CleanupTime = 72, @CheckSum = 'Y', @LogToTable = 'Y'" -b
```


