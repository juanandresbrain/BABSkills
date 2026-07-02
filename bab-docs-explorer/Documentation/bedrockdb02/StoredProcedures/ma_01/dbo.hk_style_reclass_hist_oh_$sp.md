# dbo.hk_style_reclass_hist_oh_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.hk_style_reclass_hist_oh_$sp"]
    dbo_hist_oh_style_loc_li(["dbo.hist_oh_style_loc_li"]) --> SP
    dbo_hist_oh_style_loc_pd(["dbo.hist_oh_style_loc_pd"]) --> SP
    dbo_hist_oh_style_loc_wk(["dbo.hist_oh_style_loc_wk"]) --> SP
    dbo_hist_oh_style_loc_yr(["dbo.hist_oh_style_loc_yr"]) --> SP
    dbo_post_hist_oh_group(["dbo.post_hist_oh_group"]) --> SP
    dbo_post_hist_oh_style(["dbo.post_hist_oh_style"]) --> SP
    dbo_post_oh_work_group_li(["dbo.post_oh_work_group_li"]) --> SP
    dbo_post_oh_work_group_pd(["dbo.post_oh_work_group_pd"]) --> SP
    dbo_post_oh_work_group_wk(["dbo.post_oh_work_group_wk"]) --> SP
    dbo_post_oh_work_group_yr(["dbo.post_oh_work_group_yr"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.hist_oh_style_loc_li |
| dbo.hist_oh_style_loc_pd |
| dbo.hist_oh_style_loc_wk |
| dbo.hist_oh_style_loc_yr |
| dbo.post_hist_oh_group |
| dbo.post_hist_oh_style |
| dbo.post_oh_work_group_li |
| dbo.post_oh_work_group_pd |
| dbo.post_oh_work_group_wk |
| dbo.post_oh_work_group_yr |

## Stored Procedure Code

```sql

```

