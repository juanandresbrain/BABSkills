# dbo.RemoveSubscriptionFromBeingDeleted

**Database:** ReportServerESell  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.RemoveSubscriptionFromBeingDeleted"]
    SubscriptionsBeingDeleted(["SubscriptionsBeingDeleted"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| SubscriptionsBeingDeleted |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[RemoveSubscriptionFromBeingDeleted] 
@SubscriptionID uniqueidentifier
AS
delete from [SubscriptionsBeingDeleted] where SubscriptionID = @SubscriptionID
```

