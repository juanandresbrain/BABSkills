# dbo.post_oh_work_group_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.post_oh_work_group_$sp"]
    dbo_calendar(["dbo.calendar"]) --> SP
    dbo_calendar_merch_period(["dbo.calendar_merch_period"]) --> SP
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_post_hist_oh_group(["dbo.post_hist_oh_group"]) --> SP
    dbo_post_oh_work_group_li(["dbo.post_oh_work_group_li"]) --> SP
    dbo_post_oh_work_group_pd(["dbo.post_oh_work_group_pd"]) --> SP
    dbo_post_oh_work_group_wk(["dbo.post_oh_work_group_wk"]) --> SP
    dbo_post_oh_work_group_yr(["dbo.post_oh_work_group_yr"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar |
| dbo.calendar_merch_period |
| dbo.calendar_merch_week |
| dbo.post_hist_oh_group |
| dbo.post_oh_work_group_li |
| dbo.post_oh_work_group_pd |
| dbo.post_oh_work_group_wk |
| dbo.post_oh_work_group_yr |

## Stored Procedure Code

```sql
CREATE PROC [dbo].[post_oh_work_group_$sp]
```

