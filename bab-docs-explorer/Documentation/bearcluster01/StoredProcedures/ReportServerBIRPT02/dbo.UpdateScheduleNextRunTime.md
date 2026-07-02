# dbo.UpdateScheduleNextRunTime

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.UpdateScheduleNextRunTime"]
    dbo_Schedule(["dbo.Schedule"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Schedule |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[UpdateScheduleNextRunTime]
@ScheduleID as uniqueidentifier,
@NextRunTime as datetime
as
update Schedule set [NextRunTime] = @NextRunTime where [ScheduleID] = @ScheduleID
```

