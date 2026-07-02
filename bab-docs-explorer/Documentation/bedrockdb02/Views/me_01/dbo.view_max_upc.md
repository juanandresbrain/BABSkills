# dbo.view_max_upc

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_max_upc"]
    dbo_upc(["dbo.upc"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.upc |

## View Code

```sql
CREATE VIEW dbo.view_max_upc
         (sku_id,
          max_upc)
AS
   SELECT DISTINCT
          sku_id,
          MAX(upc_number)"max_upc"
     FROM dbo.upc
   GROUP BY sku_id
```

