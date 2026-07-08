# Job: DBA - AdHoc Database Backup - DIFF

**Enabled:** Yes  
**Server:** bedrockdb01  
**Description:** Source: https://ola.hallengren.com  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["DBA - AdHoc Database Backup - DIFF"]
    JOB --> S1["Step 1: DBA - DatabaseBackup - USER_DATABASES - DIFF [CmdExec]"]
```

## Steps

### Step 1: DBA - DatabaseBackup - USER_DATABASES - DIFF
**Subsystem:** CmdExec  

```sql
sqlcmd -E -S $(ESCAPE_SQUOTE(SRVR)) -d master -Q "EXECUTE [dbo].[DatabaseBackup] @Databases = 'auditworks,auditworks_work,Foundation,foundation_event', @Directory = N'\\stl-esxbak-p-34\sqlbackups\AptosLive2Test', @BackupType = 'DIFF', @Verify = 'Y', @CleanupTime = 168, @CheckSum = 'Y', @LogToTable = 'Y'" -b
```

