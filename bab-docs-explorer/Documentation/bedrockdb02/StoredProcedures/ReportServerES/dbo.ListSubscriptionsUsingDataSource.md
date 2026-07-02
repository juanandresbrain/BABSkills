# dbo.ListSubscriptionsUsingDataSource

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.ListSubscriptionsUsingDataSource"]
    dbo_ActiveSubscriptions(["dbo.ActiveSubscriptions"]) --> SP
    dbo_Catalog(["dbo.Catalog"]) --> SP
    dbo_DataSource(["dbo.DataSource"]) --> SP
    dbo_SecData(["dbo.SecData"]) --> SP
    dbo_Subscriptions(["dbo.Subscriptions"]) --> SP
    dbo_Users(["dbo.Users"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ActiveSubscriptions |
| dbo.Catalog |
| dbo.DataSource |
| dbo.SecData |
| dbo.Subscriptions |
| dbo.Users |

## Stored Procedure Code

```sql

```

