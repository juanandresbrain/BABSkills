# dbo.view_hist_oh_sku_loc_wk

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_hist_oh_sku_loc_wk"]
    dbo_hist_oh_sku_loc_wk(["dbo.hist_oh_sku_loc_wk"]) --> VIEW
    dbo_style_color(["dbo.style_color"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.hist_oh_sku_loc_wk |
| dbo.style_color |

## View Code

```sql
create view dbo.view_hist_oh_sku_loc_wk AS
SELECT b.style_color_id, a.style_id, a.color_id, a.size_master_id, a.merch_year_wk, a.location_id, a.inventory_status_id, a.price_status_id, a.on_hand_units FROM hist_oh_sku_loc_wk a, style_color b 
where a.style_id = b.style_id   and a.color_id = b.color_id
```

