# dbo.post_hist_oh_group_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.post_hist_oh_group_$sp"]
    dbo_a(["dbo.a"]) --> SP
    dbo_hist_oh_group_chn_li(["dbo.hist_oh_group_chn_li"]) --> SP
    dbo_hist_oh_group_chn_pd(["dbo.hist_oh_group_chn_pd"]) --> SP
    dbo_hist_oh_group_chn_wk(["dbo.hist_oh_group_chn_wk"]) --> SP
    dbo_hist_oh_group_chn_yr(["dbo.hist_oh_group_chn_yr"]) --> SP
    dbo_hist_oh_group_loc_li(["dbo.hist_oh_group_loc_li"]) --> SP
    dbo_hist_oh_group_loc_pd(["dbo.hist_oh_group_loc_pd"]) --> SP
    dbo_hist_oh_group_loc_wk(["dbo.hist_oh_group_loc_wk"]) --> SP
    dbo_hist_oh_group_loc_yr(["dbo.hist_oh_group_loc_yr"]) --> SP
    dbo_mv_fact_queue(["dbo.mv_fact_queue"]) --> SP
    dbo_plan_exp_table_group(["dbo.plan_exp_table_group"]) --> SP
    dbo_post_oh_work_group_li(["dbo.post_oh_work_group_li"]) --> SP
    dbo_post_oh_work_group_pd(["dbo.post_oh_work_group_pd"]) --> SP
    dbo_post_oh_work_group_wk(["dbo.post_oh_work_group_wk"]) --> SP
    dbo_post_oh_work_group_yr(["dbo.post_oh_work_group_yr"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.a |
| dbo.hist_oh_group_chn_li |
| dbo.hist_oh_group_chn_pd |
| dbo.hist_oh_group_chn_wk |
| dbo.hist_oh_group_chn_yr |
| dbo.hist_oh_group_loc_li |
| dbo.hist_oh_group_loc_pd |
| dbo.hist_oh_group_loc_wk |
| dbo.hist_oh_group_loc_yr |
| dbo.mv_fact_queue |
| dbo.plan_exp_table_group |
| dbo.post_oh_work_group_li |
| dbo.post_oh_work_group_pd |
| dbo.post_oh_work_group_wk |
| dbo.post_oh_work_group_yr |

## Stored Procedure Code

```sql

```

