# dbo.GetSubscriptionsForUpgrade

**Database:** ReportServerWebIM  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetSubscriptionsForUpgrade"]
    Subscriptions(["Subscriptions"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Subscriptions |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[GetSubscriptionsForUpgrade]
@CurrentVersion int
AS
SELECT 
    [SubscriptionID]
FROM 
    [Subscriptions]
WHERE
    [Version] != @CurrentVersion
```

