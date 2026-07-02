# dbo.post_oh_work_styleclr_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.post_oh_work_styleclr_$sp"]
    dbo_calendar(["dbo.calendar"]) --> SP
    dbo_calendar_merch_period(["dbo.calendar_merch_period"]) --> SP
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_post_hist_oh_styleclr(["dbo.post_hist_oh_styleclr"]) --> SP
    dbo_post_oh_work_styleclr_li(["dbo.post_oh_work_styleclr_li"]) --> SP
    dbo_post_oh_work_styleclr_pd(["dbo.post_oh_work_styleclr_pd"]) --> SP
    dbo_post_oh_work_styleclr_wk(["dbo.post_oh_work_styleclr_wk"]) --> SP
    dbo_post_oh_work_styleclr_yr(["dbo.post_oh_work_styleclr_yr"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar |
| dbo.calendar_merch_period |
| dbo.calendar_merch_week |
| dbo.post_hist_oh_styleclr |
| dbo.post_oh_work_styleclr_li |
| dbo.post_oh_work_styleclr_pd |
| dbo.post_oh_work_styleclr_wk |
| dbo.post_oh_work_styleclr_yr |

## Stored Procedure Code

```sql
CREATE PROC dbo.post_oh_work_styleclr_$sp
```

