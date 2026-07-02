# Job: DBA - AdHoc DatabaseBackup - ME_01 - FULL

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Source: https://ola.hallengren.com

## Architecture Diagram

```mermaid
flowchart LR
    JOB["DBA - AdHoc DatabaseBackup - ME_01 - FULL"]
    JOB --> Execute_Backup_Job_1["Step 1: Execute Backup Job [CmdExec]"]`n```

## Steps

### Step 1: Execute Backup Job
**Subsystem:** CmdExec  

```sql
sqlcmd -E -S $(ESCAPE_SQUOTE(SRVR)) -d master -Q "EXECUTE [DBAUtility].[dbo].[DatabaseBackup] @Databases = 'me_01', @Directory = N'\\stl-esxbak-p-34\sqlbackups\', @BackupType = 'FULL', @Verify = 'Y', @CleanupTime = 72, @CheckSum = 'Y', @LogToTable = 'Y',@NumberOfFiles = 8" -b
```


