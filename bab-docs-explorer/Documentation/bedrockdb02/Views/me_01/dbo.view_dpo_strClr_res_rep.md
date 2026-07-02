# dbo.view_dpo_strClr_res_rep

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_dpo_strClr_res_rep"]
    dbo_dist_source_sku_qty(["dbo.dist_source_sku_qty"]) --> VIEW
    dbo_distribution(["dbo.distribution"]) --> VIEW
    dbo_sku(["dbo.sku"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dist_source_sku_qty |
| dbo.distribution |
| dbo.sku |

## View Code

```sql
CREATE VIEW dbo.view_dpo_strClr_res_rep 
AS
SELECT dssq.distribution_id, 
d.po_id,
d.po_shipment_id,
k.style_color_id, 
sum(dssq.reserve_quantity) AS dist_po_strClr_res_qty
FROM dist_source_sku_qty dssq
INNER JOIN distribution d ON d.distribution_id = dssq.distribution_id AND d.document_source = 1
INNER JOIN sku k ON k.sku_id = dssq.sku_id
GROUP BY dssq.distribution_id, d.po_id, d.po_shipment_id, k.style_color_id
```

