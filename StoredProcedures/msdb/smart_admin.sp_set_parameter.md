# smart_admin.sp_set_parameter

**Database:** msdb  

## Architecture Diagram

```mermaid
flowchart LR
    SP["smart_admin.sp_set_parameter"]
    managed_backup_sp_set_parameter(["managed_backup.sp_set_parameter"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| managed_backup.sp_set_parameter |

## Stored Procedure Code

```sql
-- Set the value of an internal system flag. These values govern the behavior of smart-backup algorithms.
--
CREATE PROCEDURE smart_admin.sp_set_parameter
	@parameter_name NVARCHAR(128),
	@parameter_value NVARCHAR(128)
AS
BEGIN
	EXECUTE managed_backup.sp_set_parameter @parameter_name, @parameter_value
END
```

