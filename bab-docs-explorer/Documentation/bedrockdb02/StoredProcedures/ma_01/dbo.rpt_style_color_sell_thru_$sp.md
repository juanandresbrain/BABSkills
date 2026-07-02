# dbo.rpt_style_color_sell_thru_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.rpt_style_color_sell_thru_$sp"]
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_color(["dbo.color"]) --> SP
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> SP
    dbo_hist_oh_styleclr_chn_li(["dbo.hist_oh_styleclr_chn_li"]) --> SP
    dbo_hist_styleclr_chn_li(["dbo.hist_styleclr_chn_li"]) --> SP
    dbo_hist_styleclr_chn_wk(["dbo.hist_styleclr_chn_wk"]) --> SP
    dbo_ib_activity_date(["dbo.ib_activity_date"]) --> SP
    dbo_oo_all_styleclr_chn_li(["dbo.oo_all_styleclr_chn_li"]) --> SP
    dbo_price_status(["dbo.price_status"]) --> SP
    dbo_style(["dbo.style"]) --> SP
    dbo_style_color(["dbo.style_color"]) --> SP
    dbo_style_parent(["dbo.style_parent"]) --> SP
    dbo_style_vendor(["dbo.style_vendor"]) --> SP
    dbo_vendor(["dbo.vendor"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_merch_week |
| dbo.color |
| dbo.hierarchy_group |
| dbo.hist_oh_styleclr_chn_li |
| dbo.hist_styleclr_chn_li |
| dbo.hist_styleclr_chn_wk |
| dbo.ib_activity_date |
| dbo.oo_all_styleclr_chn_li |
| dbo.price_status |
| dbo.style |
| dbo.style_color |
| dbo.style_parent |
| dbo.style_vendor |
| dbo.vendor |

## Stored Procedure Code

```sql

```

