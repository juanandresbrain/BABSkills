# Job: DBA - sp_delete_backuphistory

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Source: https://ola.hallengren.com

## Architecture Diagram

```mermaid
flowchart LR
    JOB["DBA - sp_delete_backuphistory"]
    JOB --> New_DBA___sp_delete_backuphistory_1["Step 1: New DBA - sp_delete_backuphistory [CMDEXEC]"]`n```

## Steps

### Step 1: New DBA - sp_delete_backuphistory
**Subsystem:** CMDEXEC  

```sql
sqlcmd -E -S $(ESCAPE_SQUOTE(SRVR)) -d msdb -Q "DECLARE @CleanupDate datetime SET @CleanupDate = DATEADD(dd,-30,GETDATE()) EXECUTE dbo.sp_delete_backuphistory @oldest_date = @CleanupDate" -b
```


