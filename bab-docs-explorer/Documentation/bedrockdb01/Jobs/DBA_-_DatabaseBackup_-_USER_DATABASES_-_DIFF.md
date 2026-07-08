# Job: DBA - DatabaseBackup - USER_DATABASES - DIFF

**Enabled:** Yes  
**Server:** bedrockdb01  
**Description:** Source: https://ola.hallengren.com  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["DBA - DatabaseBackup - USER_DATABASES - DIFF"]
    JOB --> S1["Step 1: DBA - DatabaseBackup - USER_DATABASES - DIFF [CMDEXEC]"]
```

## Steps

### Step 1: DBA - DatabaseBackup - USER_DATABASES - DIFF
**Subsystem:** CMDEXEC  

```sql
sqlcmd -E -S $(ESCAPE_SQUOTE(SRVR)) -d master -Q "EXECUTE [dbo].[DatabaseBackup] @Databases = 'USER_DATABASES', @Directory = N'\\stl-esxbak-p-32\sqlbackups\', @BackupType = 'DIFF', @Verify = 'Y', @CleanupTime = 168, @CheckSum = 'Y', @LogToTable = 'Y'" -b
```

