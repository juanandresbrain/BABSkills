# dbo.AddAlertSubscription

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.AddAlertSubscription"]
    dbo_AlertSubscribers(["dbo.AlertSubscribers"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.AlertSubscribers |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[AddAlertSubscription]
    @UserID uniqueidentifier,
    @ItemID uniqueidentifier,
    @AlertType nvarchar(50)
AS
BEGIN
    IF NOT EXISTS (SELECT * FROM AlertSubscribers WHERE
    UserID = @UserID AND
    ItemID = @ItemID AND
    AlertType = @AlertType) BEGIN
        INSERT
        INTO [AlertSubscribers] (UserID, ItemID, AlertType)
        VALUES (@UserID, @ItemID, @AlertType)
    END
END
```

