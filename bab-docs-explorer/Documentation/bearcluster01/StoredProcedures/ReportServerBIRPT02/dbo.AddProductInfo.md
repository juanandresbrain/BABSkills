# dbo.AddProductInfo

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.AddProductInfo"]
    dbo_ProductInfoHistory(["dbo.ProductInfoHistory"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ProductInfoHistory |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[AddProductInfo]
    @DbSchemaHash varchar(128),
    @Sku varchar(25),
    @BuildNumber varchar(25)
AS
    INSERT INTO [dbo].[ProductInfoHistory]
        ([DbSchemaHash], [Sku], [BuildNumber])
    VALUES
        (@DbSchemaHash, @Sku, @BuildNumber)
```

