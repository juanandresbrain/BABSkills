# dbo.es_calc_sell_thru_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.es_calc_sell_thru_$sp"]
    dbo_calendar_date(["dbo.calendar_date"]) --> SP
    dbo_es_sell_thru(["dbo.es_sell_thru"]) --> SP
    dbo_hist_oh_sku_loc_li(["dbo.hist_oh_sku_loc_li"]) --> SP
    dbo_hist_oh_sku_loc_wk(["dbo.hist_oh_sku_loc_wk"]) --> SP
    dbo_hist_sku_loc_li(["dbo.hist_sku_loc_li"]) --> SP
    dbo_hist_sku_loc_wk(["dbo.hist_sku_loc_wk"]) --> SP
    dbo_sku(["dbo.sku"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_date |
| dbo.es_sell_thru |
| dbo.hist_oh_sku_loc_li |
| dbo.hist_oh_sku_loc_wk |
| dbo.hist_sku_loc_li |
| dbo.hist_sku_loc_wk |
| dbo.sku |

## Stored Procedure Code

```sql

```

