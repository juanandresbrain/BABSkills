# dbo.CreateDataDrivenNotification

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.CreateDataDrivenNotification"]
    dbo_GetUserID(["dbo.GetUserID"]) --> SP
    dbo_Notifications(["dbo.Notifications"]) --> SP
    dbo_Subscriptions(["dbo.Subscriptions"]) --> SP
    dbo_SubscriptionsBeingDeleted(["dbo.SubscriptionsBeingDeleted"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.GetUserID |
| dbo.Notifications |
| dbo.Subscriptions |
| dbo.SubscriptionsBeingDeleted |

## Stored Procedure Code

```sql

```

