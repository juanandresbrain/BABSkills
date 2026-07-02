# dbo.view_dist_line_secondary_qty

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_dist_line_secondary_qty"]
    dbo_dist_source_sku_qty(["dbo.dist_source_sku_qty"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dist_source_sku_qty |

## View Code

```sql
CREATE VIEW dbo.view_dist_line_secondary_qty 
AS
SELECT distribution_id, line_id, 
SUM (secondary_quantity) AS line_secondary_qty 
FROM dist_source_sku_qty 
GROUP BY distribution_id, line_id
```

