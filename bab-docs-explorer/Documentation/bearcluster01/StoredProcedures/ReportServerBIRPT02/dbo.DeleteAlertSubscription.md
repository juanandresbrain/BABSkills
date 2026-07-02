# dbo.DeleteAlertSubscription

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DeleteAlertSubscription"]
    dbo_AlertSubscribers(["dbo.AlertSubscribers"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.AlertSubscribers |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[DeleteAlertSubscription]
    @AlertSubscriptionID bigint
AS
BEGIN
    DELETE FROM [AlertSubscribers] WHERE
    AlertSubscriptionID = @AlertSubscriptionID
END
```

