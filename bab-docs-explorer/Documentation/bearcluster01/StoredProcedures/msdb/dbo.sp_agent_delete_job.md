# dbo.sp_agent_delete_job

**Database:** msdb  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_agent_delete_job"]
    dbo_sp_delete_job(["dbo.sp_delete_job"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_delete_job |

## Stored Procedure Code

```sql
CREATE PROCEDURE dbo.sp_agent_delete_job 
    @job_id                UNIQUEIDENTIFIER,
    @is_system             TINYINT = 0
AS 
BEGIN 
    DECLARE @retval INT 

    IF(@is_system = 1)
    BEGIN
        -- Delete system job 
        EXEC @retval = sys.sp_sqlagent_delete_job
            @job_id 
    END
    ELSE
    BEGIN
        -- delete user job
        EXEC msdb.dbo.sp_delete_job @job_id = @job_id
        SELECT @retval = @@error 
    END
    
    RETURN(@retval) -- 0 means success 
END
```

