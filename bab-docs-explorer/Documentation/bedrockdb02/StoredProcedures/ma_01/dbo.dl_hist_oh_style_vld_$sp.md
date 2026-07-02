# dbo.dl_hist_oh_style_vld_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.dl_hist_oh_style_vld_$sp"]
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_dl_hist_oh_style(["dbo.dl_hist_oh_style"]) --> SP
    dbo_dl_hist_task(["dbo.dl_hist_task"]) --> SP
    dbo_hist_oh_style_loc_wk(["dbo.hist_oh_style_loc_wk"]) --> SP
    dbo_inventory_status(["dbo.inventory_status"]) --> SP
    dbo_location(["dbo.location"]) --> SP
    dbo_post_parameter(["dbo.post_parameter"]) --> SP
    dbo_price_status(["dbo.price_status"]) --> SP
    dbo_style(["dbo.style"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_merch_week |
| dbo.dl_hist_oh_style |
| dbo.dl_hist_task |
| dbo.hist_oh_style_loc_wk |
| dbo.inventory_status |
| dbo.location |
| dbo.post_parameter |
| dbo.price_status |
| dbo.style |

## Stored Procedure Code

```sql

```

