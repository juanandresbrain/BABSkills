# dbo.DeleteEvent

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DeleteEvent"]
    dbo_Event(["dbo.Event"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Event |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[DeleteEvent]
@ID uniqueidentifier
AS
delete from [Event] where [EventID] = @ID
```

