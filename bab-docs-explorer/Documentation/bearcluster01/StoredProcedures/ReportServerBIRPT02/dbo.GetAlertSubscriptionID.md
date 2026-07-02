# dbo.GetAlertSubscriptionID

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetAlertSubscriptionID"]
    dbo_AlertSubscribers(["dbo.AlertSubscribers"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.AlertSubscribers |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[GetAlertSubscriptionID]
@UserID uniqueidentifier,
@ItemID uniqueidentifier,
@AlertType nvarchar(50)
AS
BEGIN
    SELECT
        AlertSubscriptionID
    FROM [AlertSubscribers]
    WHERE
        UserID = @UserID AND
        ItemID = @ItemID AND
        AlertType = @AlertType
END
```

