# dbo.UpdateSubscription

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.UpdateSubscription"]
    dbo_GetUserID(["dbo.GetUserID"]) --> SP
    dbo_Subscriptions(["dbo.Subscriptions"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.GetUserID |
| dbo.Subscriptions |

## Stored Procedure Code

```sql

```

