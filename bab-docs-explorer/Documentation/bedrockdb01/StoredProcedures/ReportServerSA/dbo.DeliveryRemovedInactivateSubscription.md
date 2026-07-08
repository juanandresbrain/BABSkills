# dbo.DeliveryRemovedInactivateSubscription

**Database:** ReportServerSA  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DeliveryRemovedInactivateSubscription"]
    Subscriptions(["Subscriptions"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Subscriptions |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[DeliveryRemovedInactivateSubscription] 
@DeliveryExtension nvarchar(260),
@Status nvarchar(260)
AS
update 
    Subscriptions
set
    [DeliveryExtension] = '',
    [InactiveFlags] = [InactiveFlags] | 1, -- Delivery Provider Removed Flag == 1
    [LastStatus] = @Status
where
    [DeliveryExtension] = @DeliveryExtension
```

