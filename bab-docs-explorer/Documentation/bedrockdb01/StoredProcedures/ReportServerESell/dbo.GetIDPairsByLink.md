# dbo.GetIDPairsByLink

**Database:** ReportServerESell  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetIDPairsByLink"]
    Catalog(["Catalog"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Catalog |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[GetIDPairsByLink]
@Link uniqueidentifier
AS
SELECT LinkSourceID, ItemID
FROM Catalog
WHERE LinkSourceID = @Link
```

