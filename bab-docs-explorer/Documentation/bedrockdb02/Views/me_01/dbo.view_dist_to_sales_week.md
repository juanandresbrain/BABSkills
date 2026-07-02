# dbo.view_dist_to_sales_week

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_dist_to_sales_week"]
    dbo_calendar_week(["dbo.calendar_week"]) --> VIEW
    dbo_calendar_year(["dbo.calendar_year"]) --> VIEW
    dbo_distribution(["dbo.distribution"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_week |
| dbo.calendar_year |
| dbo.distribution |

## View Code

```sql
create view dbo.view_dist_to_sales_week  AS
SELECT DISTINCT 
 d.distribution_id,
 c.calendar_week_id,
 c.sales_to_cal_yr_code,
 c.sales_to_cal_wk_code,
 c.sales_to_cal_yr_wk_code
FROM distribution d
LEFT JOIN 
(SELECT 
   cw.calendar_week_id,   
   cy.calendar_year_code sales_to_cal_yr_code,   
   cw.calendar_week_code sales_to_cal_wk_code,  
  (cy.calendar_year_code *100) + cw.calendar_week_code sales_to_cal_yr_wk_code  
FROM calendar_week cw, calendar_year cy  
WHERE cw.calendar_year_id = cy.calendar_year_id 
) c
ON d.sales_to_calendar_week_id =c.calendar_week_id
```

