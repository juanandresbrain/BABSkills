# dbo.rpt_par_chain_rim_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.rpt_par_chain_rim_$sp"]
    dbo_calendar_merch_period(["dbo.calendar_merch_period"]) --> SP
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_hist_group_chn_pd(["dbo.hist_group_chn_pd"]) --> SP
    dbo_hist_oh_group_chn_pd(["dbo.hist_oh_group_chn_pd"]) --> SP
    dbo_hist_rim_oh_group_chn_pd(["dbo.hist_rim_oh_group_chn_pd"]) --> SP
    dbo_oo_all_group_chn_pd(["dbo.oo_all_group_chn_pd"]) --> SP
    dbo_parameter_plan_elements(["dbo.parameter_plan_elements"]) --> SP
    dbo_plan_element(["dbo.plan_element"]) --> SP
    dbo_plan_group_chn_pd(["dbo.plan_group_chn_pd"]) --> SP
    dbo_post_parameter(["dbo.post_parameter"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_merch_period |
| dbo.calendar_merch_week |
| dbo.hist_group_chn_pd |
| dbo.hist_oh_group_chn_pd |
| dbo.hist_rim_oh_group_chn_pd |
| dbo.oo_all_group_chn_pd |
| dbo.parameter_plan_elements |
| dbo.plan_element |
| dbo.plan_group_chn_pd |
| dbo.post_parameter |

## Stored Procedure Code

```sql

```

