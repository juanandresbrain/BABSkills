# dbo.AddEvent

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.AddEvent"]
    dbo_Event(["dbo.Event"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Event |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[AddEvent]
@EventType nvarchar (260),
@EventData nvarchar (260)
AS

insert into [Event]
    ([EventID], [EventType], [EventData], [TimeEntered], [ProcessStart], [BatchID])
values
    (NewID(), @EventType, @EventData, GETUTCDATE(), NULL, NULL)
```

