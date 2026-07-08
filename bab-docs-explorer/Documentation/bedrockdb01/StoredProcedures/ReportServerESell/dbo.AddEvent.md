# dbo.AddEvent

**Database:** ReportServerESell  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.AddEvent"]
    Event(["Event"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Event |

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

