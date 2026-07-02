# dbo.GetCurrentProductInfo

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetCurrentProductInfo"]
    dbo_ProductInfoHistory(["dbo.ProductInfoHistory"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ProductInfoHistory |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[GetCurrentProductInfo]
AS
    SELECT TOP 1 [DbSchemaHash], [Sku], [BuildNumber]
    FROM [dbo].[ProductInfoHistory]
    ORDER BY DateTime DESC
```

