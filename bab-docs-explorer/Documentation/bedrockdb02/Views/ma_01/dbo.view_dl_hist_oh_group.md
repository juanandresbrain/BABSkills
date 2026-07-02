# dbo.view_dl_hist_oh_group

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_dl_hist_oh_group"]
    dbo_dl_hist_oh_group(["dbo.dl_hist_oh_group"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dl_hist_oh_group |

## View Code

```sql
create view dbo.view_dl_hist_oh_group AS
SELECT dl_hist_oh_group_id,
   record_no,   
   hierarchy_group_code,
   merch_year_wk,
   location_code,
   inventory_status_code,
   price_status_code,
   on_hand_units,
   on_hand_retail,
   on_hand_cost,
   on_hand_retail_te
FROM dl_hist_oh_group
```

