# dbo.post_hist_group_rim_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.post_hist_group_rim_$sp"]
    dbo_calendar_merch_period(["dbo.calendar_merch_period"]) --> SP
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_h(["dbo.h"]) --> SP
    dbo_hist_group_chn_li(["dbo.hist_group_chn_li"]) --> SP
    dbo_hist_group_chn_pd(["dbo.hist_group_chn_pd"]) --> SP
    dbo_hist_group_chn_wk(["dbo.hist_group_chn_wk"]) --> SP
    dbo_hist_group_chn_yr(["dbo.hist_group_chn_yr"]) --> SP
    dbo_hist_group_loc_li(["dbo.hist_group_loc_li"]) --> SP
    dbo_hist_group_loc_pd(["dbo.hist_group_loc_pd"]) --> SP
    dbo_hist_group_loc_wk(["dbo.hist_group_loc_wk"]) --> SP
    dbo_hist_group_loc_yr(["dbo.hist_group_loc_yr"]) --> SP
    dbo_hist_rim_oh_group_chn_li(["dbo.hist_rim_oh_group_chn_li"]) --> SP
    dbo_hist_rim_oh_group_chn_pd(["dbo.hist_rim_oh_group_chn_pd"]) --> SP
    dbo_hist_rim_oh_group_chn_yr(["dbo.hist_rim_oh_group_chn_yr"]) --> SP
    dbo_hist_rim_oh_group_loc_li(["dbo.hist_rim_oh_group_loc_li"]) --> SP
    dbo_hist_rim_oh_group_loc_pd(["dbo.hist_rim_oh_group_loc_pd"]) --> SP
    dbo_hist_rim_oh_group_loc_yr(["dbo.hist_rim_oh_group_loc_yr"]) --> SP
    dbo_mv_fact_queue(["dbo.mv_fact_queue"]) --> SP
    dbo_plan_exp_table_group(["dbo.plan_exp_table_group"]) --> SP
    dbo_post_hist_group_rim(["dbo.post_hist_group_rim"]) --> SP
    dbo_post_parameter(["dbo.post_parameter"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_merch_period |
| dbo.calendar_merch_week |
| dbo.h |
| dbo.hist_group_chn_li |
| dbo.hist_group_chn_pd |
| dbo.hist_group_chn_wk |
| dbo.hist_group_chn_yr |
| dbo.hist_group_loc_li |
| dbo.hist_group_loc_pd |
| dbo.hist_group_loc_wk |
| dbo.hist_group_loc_yr |
| dbo.hist_rim_oh_group_chn_li |
| dbo.hist_rim_oh_group_chn_pd |
| dbo.hist_rim_oh_group_chn_yr |
| dbo.hist_rim_oh_group_loc_li |
| dbo.hist_rim_oh_group_loc_pd |
| dbo.hist_rim_oh_group_loc_yr |
| dbo.mv_fact_queue |
| dbo.plan_exp_table_group |
| dbo.post_hist_group_rim |
| dbo.post_parameter |

## Stored Procedure Code

```sql
CREATE proc [dbo].[post_hist_group_rim_$sp]
```

