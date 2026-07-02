# dbo.get_prev_slpd_$fn

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.get_prev_slpd_$fn"]
    dbo_view_cal_year_period(["dbo.view_cal_year_period"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.view_cal_year_period |

## Stored Procedure Code

```sql
create proc dbo.get_prev_slpd_$fn  @dummy int, @dummy2 int

AS

Declare @curr_period_id int

SELECT @curr_period_id  = calendar_period_id 
FROM view_cal_year_period
WHERE cal_year_period_code = (SELECT MAX (cal_year_period_code)
	  	  	FROM view_cal_year_period
			WHERE cal_year_period_code < current_year_pd);


return isnull( @curr_period_id,0);
```

