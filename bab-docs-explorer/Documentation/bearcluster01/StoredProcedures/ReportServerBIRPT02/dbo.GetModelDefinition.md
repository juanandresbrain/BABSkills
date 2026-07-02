# dbo.GetModelDefinition

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetModelDefinition"]
    dbo_Catalog(["dbo.Catalog"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Catalog |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[GetModelDefinition]
@CatalogItemID as uniqueidentifier
AS

SELECT
    C.[Content]
FROM
    [Catalog] AS C
WHERE
    C.[ItemID] = @CatalogItemID
```

