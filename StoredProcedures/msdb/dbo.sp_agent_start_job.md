# dbo.sp_agent_start_job

**Database:** msdb  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_agent_start_job"]
    SP --> NoRefs(["No table dependencies detected"])
```

## Table Dependencies

_No table references detected automatically._

## Stored Procedure Code

```sql
CREATE PROCEDURE dbo.sp_agent_start_job 
  @job_id      UNIQUEIDENTIFIER
AS
BEGIN
    DECLARE @retval INT 

    EXEC @retval = sys.sp_sqlagent_start_job @job_id

    RETURN(@retval) -- 0 means success 
END
```

