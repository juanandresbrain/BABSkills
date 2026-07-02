# dbo.ClearScheduleConsistancyFlags

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.ClearScheduleConsistancyFlags"]
    dbo_Schedule(["dbo.Schedule"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Schedule |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[ClearScheduleConsistancyFlags]
AS
update [Schedule] with (tablock, xlock) set [ConsistancyCheck] = NULL
```

