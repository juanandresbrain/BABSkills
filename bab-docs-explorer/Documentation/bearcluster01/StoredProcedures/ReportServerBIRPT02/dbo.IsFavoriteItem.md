# dbo.IsFavoriteItem

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.IsFavoriteItem"]
    dbo_Favorites(["dbo.Favorites"]) --> SP
    dbo_GetUserIDWithNoCreate(["dbo.GetUserIDWithNoCreate"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Favorites |
| dbo.GetUserIDWithNoCreate |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[IsFavoriteItem]
@ItemID uniqueidentifier,
@UserName nvarchar (425),
@UserSid varbinary(85) = NULL,
@AuthType int
AS

DECLARE @UserID uniqueidentifier
EXEC GetUserIDWithNoCreate @UserSid, @UserName, @AuthType, @UserID OUTPUT

SELECT CAST(
    CASE WHEN EXISTS (SELECT ItemID FROM [dbo].[Favorites] WHERE UserID = @UserID AND ItemID = @ItemID) THEN 1
    ELSE 0
    END
AS BIT)
```

