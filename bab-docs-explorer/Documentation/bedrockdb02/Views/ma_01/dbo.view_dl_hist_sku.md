# dbo.view_dl_hist_sku

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_dl_hist_sku"]
    dbo_dl_hist_sku(["dbo.dl_hist_sku"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dl_hist_sku |

## View Code

```sql
create view dbo.view_dl_hist_sku AS
SELECT dl_hist_sku_id,
   record_no,   
   upc_number,
   merch_year_wk,
   location_code,
   received_units,
   return_to_vendor_units,
   distributions_units,
   transfer_in_units,
   transfer_out_units,
   sales_total_units,
   return_units,
   shrink_actual_units,
   adjustments_total_units
FROM dl_hist_sku
```

