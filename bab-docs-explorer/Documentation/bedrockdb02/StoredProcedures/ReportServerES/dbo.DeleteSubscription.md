# dbo.DeleteSubscription

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DeleteSubscription"]
    dbo_RemoveSubscriptionFromBeingDeleted(["dbo.RemoveSubscriptionFromBeingDeleted"]) --> SP
    dbo_Subscriptions(["dbo.Subscriptions"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.RemoveSubscriptionFromBeingDeleted |
| dbo.Subscriptions |

## Stored Procedure Code

```sql

```

