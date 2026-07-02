# dbo.rpt_mar_chain_md_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.rpt_mar_chain_md_$sp"]
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_hist_cmp_group_chn_wk(["dbo.hist_cmp_group_chn_wk"]) --> SP
    dbo_hist_group_chn_wk(["dbo.hist_group_chn_wk"]) --> SP
    dbo_hist_oh_group_chn_wk(["dbo.hist_oh_group_chn_wk"]) --> SP
    dbo_oo_all_group_chn_wk(["dbo.oo_all_group_chn_wk"]) --> SP
    dbo_parameter_plan_elements(["dbo.parameter_plan_elements"]) --> SP
    dbo_plan_group_chn_wk(["dbo.plan_group_chn_wk"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_merch_week |
| dbo.hist_cmp_group_chn_wk |
| dbo.hist_group_chn_wk |
| dbo.hist_oh_group_chn_wk |
| dbo.oo_all_group_chn_wk |
| dbo.parameter_plan_elements |
| dbo.plan_group_chn_wk |

## Stored Procedure Code

```sql

```

