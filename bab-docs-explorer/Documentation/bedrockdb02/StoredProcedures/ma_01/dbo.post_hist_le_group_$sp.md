# dbo.post_hist_le_group_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.post_hist_le_group_$sp"]
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_h(["dbo.h"]) --> SP
    dbo_hist_le_group_chn_li(["dbo.hist_le_group_chn_li"]) --> SP
    dbo_hist_le_group_chn_pd(["dbo.hist_le_group_chn_pd"]) --> SP
    dbo_hist_le_group_chn_wk(["dbo.hist_le_group_chn_wk"]) --> SP
    dbo_hist_le_group_chn_yr(["dbo.hist_le_group_chn_yr"]) --> SP
    dbo_hist_le_group_loc_li(["dbo.hist_le_group_loc_li"]) --> SP
    dbo_hist_le_group_loc_pd(["dbo.hist_le_group_loc_pd"]) --> SP
    dbo_hist_le_group_loc_wk(["dbo.hist_le_group_loc_wk"]) --> SP
    dbo_hist_le_group_loc_yr(["dbo.hist_le_group_loc_yr"]) --> SP
    dbo_post_hist_le_group(["dbo.post_hist_le_group"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_merch_week |
| dbo.h |
| dbo.hist_le_group_chn_li |
| dbo.hist_le_group_chn_pd |
| dbo.hist_le_group_chn_wk |
| dbo.hist_le_group_chn_yr |
| dbo.hist_le_group_loc_li |
| dbo.hist_le_group_loc_pd |
| dbo.hist_le_group_loc_wk |
| dbo.hist_le_group_loc_yr |
| dbo.post_hist_le_group |

## Stored Procedure Code

```sql

```

