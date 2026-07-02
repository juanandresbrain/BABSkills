# smart_admin.sp_add_task_command

**Database:** msdb  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["smart_admin.sp_add_task_command"]
    managed_backup_sp_add_task_command(["managed_backup.sp_add_task_command"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| managed_backup.sp_add_task_command |

## Stored Procedure Code

```sql
CREATE PROCEDURE smart_admin.sp_add_task_command 
    @task_name			NVARCHAR(50), 
    @additional_params	NVARCHAR(MAX),
    @cmd_output			NVARCHAR(MAX) = NULL OUTPUT
AS 
BEGIN
	EXECUTE managed_backup.sp_add_task_command 
		@task_name, 
		@additional_params, 
		@cmd_output OUTPUT
END
```

