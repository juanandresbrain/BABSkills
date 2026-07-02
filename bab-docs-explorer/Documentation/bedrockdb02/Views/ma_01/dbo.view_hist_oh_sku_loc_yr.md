# dbo.view_hist_oh_sku_loc_yr

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_hist_oh_sku_loc_yr"]
    dbo_hist_oh_sku_loc_yr(["dbo.hist_oh_sku_loc_yr"]) --> VIEW
    dbo_style_color(["dbo.style_color"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.hist_oh_sku_loc_yr |
| dbo.style_color |

## View Code

```sql
create view dbo.view_hist_oh_sku_loc_yr 
AS
SELECT b.style_color_id, a.style_id, a.color_id, a.size_master_id, a.merch_year, a.location_id, a.inventory_status_id, a.price_status_id, a.on_hand_units FROM hist_oh_sku_loc_yr a, style_color b 
where a.style_id = b.style_id   and a.color_id = b.color_id



dbo,view_hist_oh_style_loc_li,CREATE VIEW dbo.view_hist_oh_style_loc_li
AS

SELECT h.style_id, h.location_id, h.inventory_status_id, h.price_status_id, 
h.on_hand_units, h.on_hand_retail, h.on_hand_cost, h.on_hand_retail_te, h.on_hand_retail_local,
h.on_hand_retail_te_local, h.on_hand_cost_local, j.jurisdiction_id
FROM hist_oh_style_loc_li h
INNER JOIN location l ON h.location_id = l.location_id
INNER JOIN jurisdiction j ON l.jurisdiction_id = j.jurisdiction_id

dbo,view_hist_oh_style_loc_pd,CREATE VIEW dbo.view_hist_oh_style_loc_pd
AS

SELECT h.style_id, h.merch_year_pd,h.location_id, h.inventory_status_id, h.price_status_id, 
h.on_hand_units, h.on_hand_retail, h.on_hand_cost, h.on_hand_retail_te, h.on_hand_retail_local,
h.on_hand_retail_te_local, h.on_hand_cost_local, j.jurisdiction_id
FROM hist_oh_style_loc_pd h
INNER JOIN location l ON h.location_id = l.location_id
INNER JOIN jurisdiction j ON l.jurisdiction_id = j.jurisdiction_id

dbo,view_hist_oh_style_loc_wk,CREATE VIEW dbo.view_hist_oh_style_loc_wk
AS

SELECT h.style_id, h.merch_year_wk, h.location_id, h.inventory_status_id, h.price_status_id, 
h.on_hand_units, h.on_hand_retail, h.on_hand_cost, h.on_hand_retail_te, h.on_hand_retail_local,
h.on_hand_retail_te_local, h.on_hand_cost_local, j.jurisdiction_id
FROM hist_oh_style_loc_wk h
INNER JOIN location l ON h.location_id = l.location_id
INNER JOIN jurisdiction j ON l.jurisdiction_id = j.jurisdiction_id

dbo,view_hist_oh_style_loc_yr,CREATE VIEW dbo.view_hist_oh_style_loc_yr
AS

SELECT h.style_id, h.merch_year, h.location_id, h.inventory_status_id, h.price_status_id, 
h.on_hand_units, h.on_hand_retail, h.on_hand_cost, h.on_hand_retail_te, h.on_hand_retail_local,
h.on_hand_retail_te_local, h.on_hand_cost_local, j.jurisdiction_id
FROM hist_oh_style_loc_yr h
INNER JOIN location l ON h.location_id = l.location_id
INNER JOIN jurisdiction j ON l.jurisdiction_id = j.jurisdiction_id
```

