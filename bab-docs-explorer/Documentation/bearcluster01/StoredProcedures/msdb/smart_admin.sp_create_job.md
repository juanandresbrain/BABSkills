# smart_admin.sp_create_job

**Database:** msdb  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["smart_admin.sp_create_job"]
    managed_backup_sp_create_job(["managed_backup.sp_create_job"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| managed_backup.sp_create_job |

## Stored Procedure Code

```sql
CREATE PROCEDURE smart_admin.sp_create_job
    @task_command NVARCHAR(MAX),
    @task_job_id UNIQUEIDENTIFIER = NULL OUTPUT,
    @task_job_step_id UNIQUEIDENTIFIER = NULL OUTPUT
AS
	EXECUTE managed_backup.sp_create_job 
		@task_command, 
		@task_job_id OUTPUT, 
		@task_job_step_id OUTPUT
```

