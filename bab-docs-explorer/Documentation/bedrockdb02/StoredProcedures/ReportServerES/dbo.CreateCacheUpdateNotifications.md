# dbo.CreateCacheUpdateNotifications

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.CreateCacheUpdateNotifications"]
    dbo_Catalog(["dbo.Catalog"]) --> SP
    dbo_Event(["dbo.Event"]) --> SP
    dbo_Notifications(["dbo.Notifications"]) --> SP
    dbo_Subscriptions(["dbo.Subscriptions"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Catalog |
| dbo.Event |
| dbo.Notifications |
| dbo.Subscriptions |

## Stored Procedure Code

```sql

```

