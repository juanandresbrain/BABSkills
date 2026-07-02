# dbo.startup_hist_rim_oh_group_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.startup_hist_rim_oh_group_$sp"]
    dbo_calendar_merch_period(["dbo.calendar_merch_period"]) --> SP
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_h(["dbo.h"]) --> SP
    dbo_hist_rim_oh_group_chn_li(["dbo.hist_rim_oh_group_chn_li"]) --> SP
    dbo_hist_rim_oh_group_chn_pd(["dbo.hist_rim_oh_group_chn_pd"]) --> SP
    dbo_hist_rim_oh_group_chn_yr(["dbo.hist_rim_oh_group_chn_yr"]) --> SP
    dbo_hist_rim_oh_group_loc_li(["dbo.hist_rim_oh_group_loc_li"]) --> SP
    dbo_hist_rim_oh_group_loc_pd(["dbo.hist_rim_oh_group_loc_pd"]) --> SP
    dbo_hist_rim_oh_group_loc_yr(["dbo.hist_rim_oh_group_loc_yr"]) --> SP
    dbo_post_parameter(["dbo.post_parameter"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_merch_period |
| dbo.calendar_merch_week |
| dbo.h |
| dbo.hist_rim_oh_group_chn_li |
| dbo.hist_rim_oh_group_chn_pd |
| dbo.hist_rim_oh_group_chn_yr |
| dbo.hist_rim_oh_group_loc_li |
| dbo.hist_rim_oh_group_loc_pd |
| dbo.hist_rim_oh_group_loc_yr |
| dbo.post_parameter |

## Stored Procedure Code

```sql

```

