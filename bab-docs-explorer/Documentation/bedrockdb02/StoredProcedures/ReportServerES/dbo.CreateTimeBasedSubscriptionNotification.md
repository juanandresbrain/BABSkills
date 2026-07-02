# dbo.CreateTimeBasedSubscriptionNotification

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.CreateTimeBasedSubscriptionNotification"]
    dbo_Event(["dbo.Event"]) --> SP
    dbo_Notifications(["dbo.Notifications"]) --> SP
    dbo_Subscriptions(["dbo.Subscriptions"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Event |
| dbo.Notifications |
| dbo.Subscriptions |

## Stored Procedure Code

```sql

```

