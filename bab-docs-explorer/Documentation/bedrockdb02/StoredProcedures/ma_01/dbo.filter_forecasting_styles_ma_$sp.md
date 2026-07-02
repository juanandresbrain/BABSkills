# dbo.filter_forecasting_styles_ma_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.filter_forecasting_styles_ma_$sp"]
    dbo_calendar_date(["dbo.calendar_date"]) --> SP
    dbo_comp_set_style_color(["dbo.comp_set_style_color"]) --> SP
    dbo_hist_oh_style_loc_li(["dbo.hist_oh_style_loc_li"]) --> SP
    dbo_hist_style_chn_wk(["dbo.hist_style_chn_wk"]) --> SP
    dbo_location(["dbo.location"]) --> SP
    dbo_oo_all_style_loc_li(["dbo.oo_all_style_loc_li"]) --> SP
    dbo_style(["dbo.style"]) --> SP
    dbo_style_color(["dbo.style_color"]) --> SP
    dbo_view_calendar_merch_week_rel(["dbo.view_calendar_merch_week_rel"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_date |
| dbo.comp_set_style_color |
| dbo.hist_oh_style_loc_li |
| dbo.hist_style_chn_wk |
| dbo.location |
| dbo.oo_all_style_loc_li |
| dbo.style |
| dbo.style_color |
| dbo.view_calendar_merch_week_rel |

## Stored Procedure Code

```sql

```

