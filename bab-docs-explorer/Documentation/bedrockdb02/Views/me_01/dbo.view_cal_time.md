# dbo.view_cal_time

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_cal_time"]
    dbo_calendar_period(["dbo.calendar_period"]) --> VIEW
    dbo_calendar_week(["dbo.calendar_week"]) --> VIEW
    dbo_calendar_year(["dbo.calendar_year"]) --> VIEW
    dbo_temp_calendar_date(["dbo.temp_calendar_date"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_period |
| dbo.calendar_week |
| dbo.calendar_year |
| dbo.temp_calendar_date |

## View Code

```sql
CREATE view [dbo].[view_cal_time] 


 AS


SELECT 
CASE WHEN cw.calendar_week_code IN ('1','5','10','14','18','23','27','31','36','40','44','49') THEN '01' 
     WHEN cw.calendar_week_code IN ('2','6','11','15','19','24','28','32','37','41','45','50') THEN '02' 
     WHEN cw.calendar_week_code IN ('3','7','12','16','20','25','29','33','38','42','46','51') THEN '03' 
     WHEN cw.calendar_week_code IN ('4','8','13','17','21','26','30','34','39','43','47','52') THEN '04' 
     WHEN cw.calendar_week_code IN ('9','22','35','48') THEN '05' 
     WHEN cw.calendar_week_code IN ('53') THEN '06' 
END AS WEEK,
--CASE WHEN cw.calendar_week_code IN ('1','5','9','14','18','22','27','31','35','40','44','48') THEN '01' 
--     WHEN cw.calendar_week_code IN ('2','6','10','15','19','23','28','32','36','41','45','49') THEN '02' 
--     WHEN cw.calendar_week_code IN ('3','7','11','16','20','24','29','33','37','42','46','50') THEN '03' 
--     WHEN cw.calendar_week_code IN ('4','8','12','17','21','25','30','34','38','43','47','51') THEN '04' 
--     WHEN cw.calendar_week_code IN ('13','26','39','52') THEN '05' 
--     WHEN cw.calendar_week_code IN ('53')
--		THEN CASE WHEN cd.merch_period = 12 
--			THEN '05'
--			ELSE '06'
--		END 
--END AS WEEK,

CASE WHEN cd.merch_period = 1 THEN CAST(cy.calendar_year_code AS VARCHAR)  + 'JAN'
	 WHEN cd.merch_period = 2 THEN CAST(cy.calendar_year_code AS VARCHAR) + 'FEB' 
	 WHEN cd.merch_period = 3 THEN CAST(cy.calendar_year_code AS VARCHAR)  + 'MAR' 
	 WHEN cd.merch_period = 4 THEN CAST(cy.calendar_year_code AS VARCHAR)  + 'APR' 
	 WHEN cd.merch_period = 5 THEN CAST(cy.calendar_year_code AS VARCHAR)  + 'MAY' 
	 WHEN cd.merch_period = 6 THEN CAST(cy.calendar_year_code AS VARCHAR)  +  'JUN' 
	 WHEN cd.merch_period = 7 THEN CAST(cy.calendar_year_code AS VARCHAR) +  'JUL' 
	 WHEN cd.merch_period = 8 THEN CAST(cy.calendar_year_code AS VARCHAR) +  'AUG' 
	 WHEN cd.merch_period = 9 THEN CAST(cy.calendar_year_code AS VARCHAR)  +  'SEP' 
	 WHEN cd.merch_period = 10 THEN CAST(cy.calendar_year_code AS VARCHAR)  +  'OCT' 
	 WHEN cd.merch_period = 11 THEN CAST(cy.calendar_year_code AS VARCHAR)  +  'NOV' 
	 WHEN cd.merch_period = 12 THEN CAST(cy.calendar_year_code AS VARCHAR) +  'DEC' 
END AS MONTH,
CASE WHEN cd.merch_period = 1 THEN 'JAN'
	 WHEN cd.merch_period = 2 THEN 'FEB'
	 WHEN cd.merch_period = 3 THEN 'MAR'
	 WHEN cd.merch_period = 4 THEN 'APR'
	 WHEN cd.merch_period = 5 THEN 'MAY'
	 WHEN cd.merch_period = 6 THEN 'JUN'
	 WHEN cd.merch_period = 7 THEN 'JUL'
	 WHEN cd.merch_period = 8 THEN 'AUG'
	 WHEN cd.merch_period = 9 THEN 'SEP'
	 WHEN cd.merch_period = 10 THEN 'OCT'
	 WHEN cd.merch_period = 11 THEN 'NOV'
	 WHEN cd.merch_period = 12 THEN 'DEC'
END AS MONTH_NAME,
CASE WHEN cd.merch_period = 1 THEN 'JANUARY'
	 WHEN cd.merch_period = 2 THEN 'FEBRUARY'
	 WHEN cd.merch_period = 3 THEN 'MARCH'
	 WHEN cd.merch_period = 4 THEN 'APRIL'
	 WHEN cd.merch_period = 5 THEN 'MAY'
	 WHEN cd.merch_period = 6 THEN 'JUNE'
	 WHEN cd.merch_period = 7 THEN 'JULY'
	 WHEN cd.merch_period = 8 THEN 'AUGUST'
	 WHEN cd.merch_period = 9 THEN 'SEPTEMBER'
	 WHEN cd.merch_period = 10 THEN 'OCTOBER'
	 WHEN cd.merch_period = 11 THEN 'NOVEMBER'
	 WHEN cd.merch_period = 12 THEN 'DECEMBER'
END AS MONTH_DESCRIPTION,
min(cw1.calendar_week_start_date) as MONTH_DATE, 
max(cw1.calendar_week_end_date) as MONTH_END_DATE,
cw.calendar_week_start_date as WEEK_DATE,
cw.calendar_week_end_date as WEEK_END_DATE,
cw.calendar_week_code as WEEK_NUMBER,
--cp.calendar_period_code as WEEK_PERIOD,
WEEK_PERIOD = CASE WHEN DATEDIFF(wk,GETDATE(),cw.calendar_week_start_date) < 0 THEN 'WTD' ELSE 'WTG' END,
CAST(cy.calendar_year_code as varchar) + '' + RIGHT ('0' + CONVERT(VARCHAR,cw.calendar_week_code),2) as WEEK_NAME,	
CAST(cy.calendar_year_code as varchar) + '' + RIGHT ('0' + CONVERT(VARCHAR,cw.calendar_week_code),2) as WEEK_DESCRIPTION,	

DATEDIFF(wk,GETDATE(),cw.calendar_week_start_date) as WEEK_PROG,

'BABWALL' as ALL_TIME,								
CASE WHEN cd.merch_period BETWEEN 1 AND 3 THEN cast(cy.calendar_year_code as varchar) + 'QTR1'
	 WHEN cd.merch_period BETWEEN 4 AND 6 THEN cast(cy.calendar_year_code as varchar) + 'QTR2'
	 WHEN cd.merch_period BETWEEN 7 AND 9 THEN cast(cy.calendar_year_code as varchar)  + 'QTR3'
	 WHEN cd.merch_period BETWEEN 10 AND 12 THEN cast(cy.calendar_year_code as varchar) + 'QTR4'
END AS QUARTER,
CASE WHEN cd.merch_period BETWEEN 1 AND 3 THEN 'QUARTER1'
	 WHEN cd.merch_period BETWEEN 4 AND 6 THEN 'QUARTER2'
	 WHEN cd.merch_period BETWEEN 7 AND 9 THEN 'QUARTER3'
	 WHEN cd.merch_period BETWEEN 10 AND 12 THEN 'QUARTER4'
END AS QUARTER_DESCRIPTION,
CASE WHEN cd.merch_period BETWEEN 1 AND 3 THEN 'QTR1'
	 WHEN cd.merch_period BETWEEN 4 AND 6 THEN 'QTR2'
	 WHEN cd.merch_period BETWEEN 7 AND 9 THEN 'QTR3'
	 WHEN cd.merch_period BETWEEN 10 AND 12 THEN 'QTR4'
END AS QUARTER_NAME,	
cy.calendar_year_code as YEAR
FROM	me_01.dbo.calendar_year cy 
		inner join me_01.dbo.calendar_period cp		on cy.calendar_year_id = cp.calendar_year_id
		inner join me_01.dbo.calendar_week cw		on cp.calendar_period_id = cw.calendar_period_id
														and	cp.calendar_year_id = cw.calendar_year_id
														and	cy.calendar_year_id = cw.calendar_year_id
		inner join me_01.dbo.calendar_week cw1		on cw.calendar_period_id = cw1.calendar_period_id
		inner join me_01.dbo.temp_calendar_date cd		on cy.calendar_year_code = cd.merch_year
														and cw.calendar_week_code = cd.merch_week
														and cd.calendar_date = cw.calendar_week_start_date    

GROUP BY 
cw.calendar_week_code, cy.calendar_year_code, cw.calendar_week_start_date, cw.calendar_week_end_date,
cd.calendar_date, cd.merch_period, cp.calendar_period_code
```

