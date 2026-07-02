# dbo.GetCatalogItemContent

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetCatalogItemContent"]
    dbo_Catalog(["dbo.Catalog"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Catalog |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].GetCatalogItemContent
@CatalogItemID AS uniqueidentifier
AS

SELECT
    [Content]
FROM
    [Catalog]
WHERE
    [ItemID] = @CatalogItemID
```

