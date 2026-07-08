# dbo.ClearScheduleConsistancyFlags

**Database:** ReportServerESell  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.ClearScheduleConsistancyFlags"]
    Schedule(["Schedule"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Schedule |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[ClearScheduleConsistancyFlags]
AS
update [Schedule] with (tablock, xlock) set [ConsistancyCheck] = NULL
```

