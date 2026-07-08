# dbo.ListUsedDeliveryProviders

**Database:** ReportServerESell  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.ListUsedDeliveryProviders"]
    Subscriptions(["Subscriptions"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Subscriptions |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[ListUsedDeliveryProviders] 
AS
select distinct [DeliveryExtension] from Subscriptions where [DeliveryExtension] <> ''
```

