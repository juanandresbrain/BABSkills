# dbo.DeleteTask

**Database:** ReportServerSA  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DeleteTask"]
    Schedule(["Schedule"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Schedule |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[DeleteTask]
@ScheduleID uniqueidentifier
AS
SET NOCOUNT OFF
-- Delete the task with the given task id
DELETE FROM Schedule
WHERE [ScheduleID] = @ScheduleID
```

