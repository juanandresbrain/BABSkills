# dbo.sp_maintplan_open_logentry

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_maintplan_open_logentry"]
    dbo_sysmaintplan_log(["dbo.sysmaintplan_log"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sysmaintplan_log |

## Stored Procedure Code

```sql
CREATE PROCEDURE sp_maintplan_open_logentry
    @plan_id       UNIQUEIDENTIFIER,
    @subplan_id       UNIQUEIDENTIFIER,   
    @start_time       DATETIME            = NULL,
    @task_detail_id  UNIQUEIDENTIFIER    = NULL OUTPUT
AS
BEGIN

   --Set defaults
   IF (@start_time IS NULL)
   BEGIN
      SELECT @start_time = GETDATE()
   END

   SELECT @task_detail_id = NEWID()

   --Insert a new record into sysmaintplan_log table
   INSERT INTO msdb.dbo.sysmaintplan_log(task_detail_id, plan_id, subplan_id, start_time)
    VALUES(@task_detail_id, @plan_id, @subplan_id, @start_time)

   RETURN (@@ERROR)
END
```

