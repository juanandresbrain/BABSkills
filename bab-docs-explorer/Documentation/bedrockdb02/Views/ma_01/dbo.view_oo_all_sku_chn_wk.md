# dbo.view_oo_all_sku_chn_wk

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_oo_all_sku_chn_wk"]
    dbo_oo_all_sku_chn_wk(["dbo.oo_all_sku_chn_wk"]) --> VIEW
    dbo_style_color(["dbo.style_color"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.oo_all_sku_chn_wk |
| dbo.style_color |

## View Code

```sql
create view dbo.view_oo_all_sku_chn_wk 

AS
SELECT b.style_color_id, a.style_id, a.color_id, a.size_master_id, a.merch_year_wk, a.on_order_units, a.allocation_units FROM oo_all_sku_chn_wk a, style_color b 
where a.style_id = b.style_id   and a.color_id = b.color_id
```

