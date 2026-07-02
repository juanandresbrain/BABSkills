# dbo.rpt_vendor_analysis_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.rpt_vendor_analysis_$sp"]
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> SP
    dbo_hierarchy_level(["dbo.hierarchy_level"]) --> SP
    dbo_hist_cmp_style_chn_wk(["dbo.hist_cmp_style_chn_wk"]) --> SP
    dbo_hist_oh_style_chn_wk(["dbo.hist_oh_style_chn_wk"]) --> SP
    dbo_hist_style_chn_wk(["dbo.hist_style_chn_wk"]) --> SP
    dbo_history_component(["dbo.history_component"]) --> SP
    dbo_oo_all_style_chn_wk(["dbo.oo_all_style_chn_wk"]) --> SP
    dbo_style(["dbo.style"]) --> SP
    dbo_style_parent(["dbo.style_parent"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_merch_week |
| dbo.hierarchy_group |
| dbo.hierarchy_level |
| dbo.hist_cmp_style_chn_wk |
| dbo.hist_oh_style_chn_wk |
| dbo.hist_style_chn_wk |
| dbo.history_component |
| dbo.oo_all_style_chn_wk |
| dbo.style |
| dbo.style_parent |

## Stored Procedure Code

```sql

```

