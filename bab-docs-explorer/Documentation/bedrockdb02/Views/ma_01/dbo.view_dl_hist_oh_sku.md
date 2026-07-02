# dbo.view_dl_hist_oh_sku

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_dl_hist_oh_sku"]
    dbo_dl_hist_oh_sku(["dbo.dl_hist_oh_sku"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dl_hist_oh_sku |

## View Code

```sql
create view dbo.view_dl_hist_oh_sku AS
SELECT dl_hist_oh_sku_id,
   record_no,     
   upc_number,
   merch_year_wk,
   location_code,
   inventory_status_code,
   price_status_code,
   on_hand_units
FROM dl_hist_oh_sku
```

