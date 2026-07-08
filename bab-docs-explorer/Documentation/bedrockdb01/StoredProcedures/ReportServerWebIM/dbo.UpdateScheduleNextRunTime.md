# dbo.UpdateScheduleNextRunTime

**Database:** ReportServerWebIM  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.UpdateScheduleNextRunTime"]
    Schedule(["Schedule"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Schedule |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[UpdateScheduleNextRunTime]
@ScheduleID as uniqueidentifier,
@NextRunTime as datetime
as
update Schedule set [NextRunTime] = @NextRunTime where [ScheduleID] = @ScheduleID
```

