# Job: SQLAAG - Syncronize Critical SQL Objects

**Enabled:** Yes  
**Server:** bearcluster01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["SQLAAG - Syncronize Critical SQL Objects"]
    JOB --> Execute_AlwaysOnSyncronizer_1["Step 1: Execute AlwaysOnSyncronizer [TSQL]"]`n```

## Steps

### Step 1: Execute AlwaysOnSyncronizer
**Subsystem:** TSQL  

```sql
SET NOCOUNT ON;

-- Turn on xp_cmdshell if needed
DECLARE @is_config_changed bit = 0;
IF EXISTS(SELECT * FROM sys.configurations where name = 'xp_cmdshell' AND value_in_use = 0)
BEGIN;
    IF EXISTS (SELECT * FROM sys.configurations WHERE name = 'show advanced options' AND value_in_use = 0)
    BEGIN;
        EXEC sys.sp_configure 'show advanced options', 1; RECONFIGURE WITH OVERRIDE;
    END;

    EXEC sys.sp_configure 'xp_cmdshell', 1; RECONFIGURE WITH OVERRIDE;
    SELECT @is_config_changed =1;
END;


DECLARE @rc int;
EXEC @rc = xp_cmdshell 'D:\AlwaysOnSyncronizer\AlwaysOnSyncronizer.exe', no_output;
SELECT @rc;

IF @rc <> 0
BEGIN;
    RAISERROR (N'AlwaysOnSyncronizer terminated with a return status of: %d. For additional information check the AlwaysOnSyncronizer.log file.', 16, 1, @rc); 
END;


-- Revert back if changed the config
IF @is_config_changed = 1
BEGIN;
    EXEC sys.sp_configure 'xp_cmdshell', 0; RECONFIGURE WITH OVERRIDE;
END;
```


