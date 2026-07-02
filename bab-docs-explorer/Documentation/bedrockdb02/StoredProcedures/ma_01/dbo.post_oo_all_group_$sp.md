# dbo.post_oo_all_group_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.post_oo_all_group_$sp"]
    dbo_a(["dbo.a"]) --> SP
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_mv_fact_queue(["dbo.mv_fact_queue"]) --> SP
    dbo_oo_all_group_chn_li(["dbo.oo_all_group_chn_li"]) --> SP
    dbo_oo_all_group_chn_pd(["dbo.oo_all_group_chn_pd"]) --> SP
    dbo_oo_all_group_chn_wk(["dbo.oo_all_group_chn_wk"]) --> SP
    dbo_oo_all_group_chn_yr(["dbo.oo_all_group_chn_yr"]) --> SP
    dbo_oo_all_group_loc_li(["dbo.oo_all_group_loc_li"]) --> SP
    dbo_oo_all_group_loc_pd(["dbo.oo_all_group_loc_pd"]) --> SP
    dbo_oo_all_group_loc_wk(["dbo.oo_all_group_loc_wk"]) --> SP
    dbo_oo_all_group_loc_yr(["dbo.oo_all_group_loc_yr"]) --> SP
    dbo_plan_exp_table_group(["dbo.plan_exp_table_group"]) --> SP
    dbo_post_oo_all_group_sum(["dbo.post_oo_all_group_sum"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.a |
| dbo.calendar_merch_week |
| dbo.mv_fact_queue |
| dbo.oo_all_group_chn_li |
| dbo.oo_all_group_chn_pd |
| dbo.oo_all_group_chn_wk |
| dbo.oo_all_group_chn_yr |
| dbo.oo_all_group_loc_li |
| dbo.oo_all_group_loc_pd |
| dbo.oo_all_group_loc_wk |
| dbo.oo_all_group_loc_yr |
| dbo.plan_exp_table_group |
| dbo.post_oo_all_group_sum |

## Stored Procedure Code

```sql

```

