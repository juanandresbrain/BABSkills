# dbo.SetUpgradeItemStatus

**Database:** ReportServerESell  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SetUpgradeItemStatus"]
    UpgradeInfo(["UpgradeInfo"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| UpgradeInfo |

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

