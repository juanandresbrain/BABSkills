# dbo.CreateSubscription

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.CreateSubscription"]
    dbo_Catalog(["dbo.Catalog"]) --> SP
    dbo_GetUserID(["dbo.GetUserID"]) --> SP
    dbo_Subscriptions(["dbo.Subscriptions"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Catalog |
| dbo.GetUserID |
| dbo.Subscriptions |

## Stored Procedure Code

```sql

```

