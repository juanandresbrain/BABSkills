# dbo.UpdateSubscriptionStatus

**Database:** ReportServerWebIM  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.UpdateSubscriptionStatus"]
    Subscriptions(["Subscriptions"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Subscriptions |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[UpdateSubscriptionStatus]
@SubscriptionID uniqueidentifier,
@Status nvarchar(260)
AS

update Subscriptions set
        [LastStatus] = @Status
where
    [SubscriptionID] = @SubscriptionID
```

