# dbo.import_hist_cmp_sku_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.import_hist_cmp_sku_$sp"]
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_hist_cmp_sku_loc_wk(["dbo.hist_cmp_sku_loc_wk"]) --> SP
    dbo_history_component(["dbo.history_component"]) --> SP
    dbo_imp_cd_hist_cmp_sku(["dbo.imp_cd_hist_cmp_sku"]) --> SP
    dbo_imp_cd_hist_cmp_sku_error(["dbo.imp_cd_hist_cmp_sku_error"]) --> SP
    dbo_imp_id_hist_cmp_sku(["dbo.imp_id_hist_cmp_sku"]) --> SP
    dbo_location(["dbo.location"]) --> SP
    dbo_post_parameter(["dbo.post_parameter"]) --> SP
    dbo_price_status(["dbo.price_status"]) --> SP
    dbo_sku(["dbo.sku"]) --> SP
    dbo_syn_transaction_reason(["dbo.syn_transaction_reason"]) --> SP
    dbo_upc(["dbo.upc"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_merch_week |
| dbo.hist_cmp_sku_loc_wk |
| dbo.history_component |
| dbo.imp_cd_hist_cmp_sku |
| dbo.imp_cd_hist_cmp_sku_error |
| dbo.imp_id_hist_cmp_sku |
| dbo.location |
| dbo.post_parameter |
| dbo.price_status |
| dbo.sku |
| dbo.syn_transaction_reason |
| dbo.upc |

## Stored Procedure Code

```sql

```

