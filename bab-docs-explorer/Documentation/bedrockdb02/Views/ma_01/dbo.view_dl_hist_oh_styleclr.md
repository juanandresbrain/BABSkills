# dbo.view_dl_hist_oh_styleclr

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_dl_hist_oh_styleclr"]
    dbo_dl_hist_oh_styleclr(["dbo.dl_hist_oh_styleclr"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dl_hist_oh_styleclr |

## View Code

```sql
create view dbo.view_dl_hist_oh_styleclr AS
SELECT dl_hist_oh_styleclr_id,
   record_no,      
   style_code,
   color_code,
   merch_year_wk,
   location_code,
   inventory_status_code,
   price_status_code,
   on_hand_units,
   on_hand_retail,
   on_hand_retail_te
FROM dl_hist_oh_styleclr
```

