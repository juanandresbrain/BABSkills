# dbo.rpt_core_chain_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.rpt_core_chain_$sp"]
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_hist_group_chn_wk(["dbo.hist_group_chn_wk"]) --> SP
    dbo_hist_oh_group_chn_wk(["dbo.hist_oh_group_chn_wk"]) --> SP
    dbo_oo_all_group_chn_wk(["dbo.oo_all_group_chn_wk"]) --> SP
    dbo_parameter_plan_elements(["dbo.parameter_plan_elements"]) --> SP
    dbo_plan_group_chn_pd(["dbo.plan_group_chn_pd"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_merch_week |
| dbo.hist_group_chn_wk |
| dbo.hist_oh_group_chn_wk |
| dbo.oo_all_group_chn_wk |
| dbo.parameter_plan_elements |
| dbo.plan_group_chn_pd |

## Stored Procedure Code

```sql

```

