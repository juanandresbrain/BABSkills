# smart_admin.sp_backup_master_switch

**Database:** msdb  

## Architecture Diagram

```mermaid
flowchart LR
    SP["smart_admin.sp_backup_master_switch"]
    managed_backup_sp_backup_master_switch(["managed_backup.sp_backup_master_switch"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| managed_backup.sp_backup_master_switch |

## Stored Procedure Code

```sql
CREATE PROCEDURE smart_admin.sp_backup_master_switch 
	@new_state bit
AS
BEGIN
	EXECUTE [managed_backup].[sp_backup_master_switch] @new_state
END
```

