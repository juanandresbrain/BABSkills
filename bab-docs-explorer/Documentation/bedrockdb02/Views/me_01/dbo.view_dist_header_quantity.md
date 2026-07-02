# dbo.view_dist_header_quantity

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_dist_header_quantity"]
    dbo_dist_source_sku_qty(["dbo.dist_source_sku_qty"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dist_source_sku_qty |

## View Code

```sql
CREATE VIEW dbo.view_dist_header_quantity 
AS
SELECT distribution_id, 
SUM (available_quantity) AS total_available_qty, 
SUM (reserve_quantity) AS total_reserve_quantity,
SUM (secondary_quantity) AS total_secondary_quantity 
FROM dist_source_sku_qty
GROUP BY distribution_id
```

