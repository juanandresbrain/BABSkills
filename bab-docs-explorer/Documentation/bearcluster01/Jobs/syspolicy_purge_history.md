# Job: syspolicy_purge_history

**Enabled:** Yes  
**Server:** bearcluster01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["syspolicy_purge_history"]
    JOB --> Verify_that_automation_is_enabled__1["Step 1: Verify that automation is enabled. [TSQL]"]`n    JOB --> Purge_history__2["Step 2: Purge history. [TSQL]"]`n    JOB --> Erase_Phantom_System_Health_Records__3["Step 3: Erase Phantom System Health Records. [PowerShell]"]`n```

## Steps

### Step 1: Verify that automation is enabled.
**Subsystem:** TSQL  

```sql
IF (msdb.dbo.fn_syspolicy_is_automation_enabled() != 1)
        BEGIN
            RAISERROR(34022, 16, 1)
        END
```

### Step 2: Purge history.
**Subsystem:** TSQL  

```sql
EXEC msdb.dbo.sp_syspolicy_purge_history
```

### Step 3: Erase Phantom System Health Records.
**Subsystem:** PowerShell  

```sql
if ('$(ESCAPE_SQUOTE(INST))' -eq 'MSSQLSERVER') {$a = '\DEFAULT'} ELSE {$a = ''};
(Get-Item SQLSERVER:\SQLPolicy\$(ESCAPE_NONE(SRVR))$a).EraseSystemHealthPhantomRecords()
```


