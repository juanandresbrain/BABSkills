# dbo.CreateSnapShotNotifications

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.CreateSnapShotNotifications"]
    dbo_Event(["dbo.Event"]) --> SP
    dbo_History(["dbo.History"]) --> SP
    dbo_Notifications(["dbo.Notifications"]) --> SP
    dbo_Subscriptions(["dbo.Subscriptions"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Event |
| dbo.History |
| dbo.Notifications |
| dbo.Subscriptions |

## Stored Procedure Code

```sql

```

