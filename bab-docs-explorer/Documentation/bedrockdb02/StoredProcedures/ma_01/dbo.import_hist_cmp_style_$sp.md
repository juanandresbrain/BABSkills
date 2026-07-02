# dbo.import_hist_cmp_style_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.import_hist_cmp_style_$sp"]
    dbo_calendar_date(["dbo.calendar_date"]) --> SP
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_cost_factor(["dbo.cost_factor"]) --> SP
    dbo_discount(["dbo.discount"]) --> SP
    dbo_hist_cmp_style_loc_wk(["dbo.hist_cmp_style_loc_wk"]) --> SP
    dbo_history_component(["dbo.history_component"]) --> SP
    dbo_imp_cd_hist_cmp_style(["dbo.imp_cd_hist_cmp_style"]) --> SP
    dbo_imp_cd_hist_cmp_style_home(["dbo.imp_cd_hist_cmp_style_home"]) --> SP
    dbo_imp_cd_hist_cmp_style_local(["dbo.imp_cd_hist_cmp_style_local"]) --> SP
    dbo_imp_id_hist_cmp_style(["dbo.imp_id_hist_cmp_style"]) --> SP
    dbo_location(["dbo.location"]) --> SP
    dbo_multi_currency_location_cost_wk(["dbo.multi_currency_location_cost_wk"]) --> SP
    dbo_multi_currency_location_retail_wk(["dbo.multi_currency_location_retail_wk"]) --> SP
    dbo_post_parameter(["dbo.post_parameter"]) --> SP
    dbo_price_status(["dbo.price_status"]) --> SP
    dbo_style(["dbo.style"]) --> SP
    dbo_style_currency_rate(["dbo.style_currency_rate"]) --> SP
    dbo_syn_transaction_reason(["dbo.syn_transaction_reason"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_date |
| dbo.calendar_merch_week |
| dbo.cost_factor |
| dbo.discount |
| dbo.hist_cmp_style_loc_wk |
| dbo.history_component |
| dbo.imp_cd_hist_cmp_style |
| dbo.imp_cd_hist_cmp_style_home |
| dbo.imp_cd_hist_cmp_style_local |
| dbo.imp_id_hist_cmp_style |
| dbo.location |
| dbo.multi_currency_location_cost_wk |
| dbo.multi_currency_location_retail_wk |
| dbo.post_parameter |
| dbo.price_status |
| dbo.style |
| dbo.style_currency_rate |
| dbo.syn_transaction_reason |

## Stored Procedure Code

```sql

```

