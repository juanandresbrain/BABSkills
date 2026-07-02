# dbo.import_hist_cmp_group_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.import_hist_cmp_group_$sp"]
    dbo_calendar_date(["dbo.calendar_date"]) --> SP
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_cost_factor(["dbo.cost_factor"]) --> SP
    dbo_discount(["dbo.discount"]) --> SP
    dbo_group_currency_rate(["dbo.group_currency_rate"]) --> SP
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> SP
    dbo_hist_cmp_group_loc_wk(["dbo.hist_cmp_group_loc_wk"]) --> SP
    dbo_history_component(["dbo.history_component"]) --> SP
    dbo_imp_cd_hist_cmp_group(["dbo.imp_cd_hist_cmp_group"]) --> SP
    dbo_imp_cd_hist_cmp_group_home(["dbo.imp_cd_hist_cmp_group_home"]) --> SP
    dbo_imp_cd_hist_cmp_group_local(["dbo.imp_cd_hist_cmp_group_local"]) --> SP
    dbo_imp_id_hist_cmp_group(["dbo.imp_id_hist_cmp_group"]) --> SP
    dbo_location(["dbo.location"]) --> SP
    dbo_multi_currency_location_cost_wk(["dbo.multi_currency_location_cost_wk"]) --> SP
    dbo_multi_currency_location_retail_wk(["dbo.multi_currency_location_retail_wk"]) --> SP
    dbo_post_parameter(["dbo.post_parameter"]) --> SP
    dbo_price_status(["dbo.price_status"]) --> SP
    dbo_syn_transaction_reason(["dbo.syn_transaction_reason"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_date |
| dbo.calendar_merch_week |
| dbo.cost_factor |
| dbo.discount |
| dbo.group_currency_rate |
| dbo.hierarchy_group |
| dbo.hist_cmp_group_loc_wk |
| dbo.history_component |
| dbo.imp_cd_hist_cmp_group |
| dbo.imp_cd_hist_cmp_group_home |
| dbo.imp_cd_hist_cmp_group_local |
| dbo.imp_id_hist_cmp_group |
| dbo.location |
| dbo.multi_currency_location_cost_wk |
| dbo.multi_currency_location_retail_wk |
| dbo.post_parameter |
| dbo.price_status |
| dbo.syn_transaction_reason |

## Stored Procedure Code

```sql

```

