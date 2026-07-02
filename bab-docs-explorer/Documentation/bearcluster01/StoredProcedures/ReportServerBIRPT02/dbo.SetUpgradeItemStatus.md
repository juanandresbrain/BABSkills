# dbo.SetUpgradeItemStatus

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SetUpgradeItemStatus"]
    dbo_UpgradeInfo(["dbo.UpgradeInfo"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.UpgradeInfo |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[SetUpgradeItemStatus]
@ItemName nvarchar(260),
@Status nvarchar(512)
AS
UPDATE
    [UpgradeInfo]
SET
    [Status] = @Status
WHERE
    [Item] = @ItemName
```

