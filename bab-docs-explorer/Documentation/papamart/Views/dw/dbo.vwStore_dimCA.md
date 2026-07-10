# dbo.vwStore_dimCA

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwStore_dimCA"]
    dbo_date_dim(["dbo.date_dim"]) --> VIEW
    dbo_demographics_dim(["dbo.demographics_dim"]) --> VIEW
    dbo_store_dim(["dbo.store_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.date_dim |
| dbo.demographics_dim |
| dbo.store_dim |

## View Code

```sql
CREATE VIEW [dbo].[vwStore_dimCA]
AS
SELECT sd.store_key, sd.store_id, sd.store_name,
storeNameNum = CASE
	when country <> 'UK' then RIGHT('000' + CAST(sd.store_id AS varchar), 3) + ' ' + sd.store_name
	else RIGHT('000' + CAST(sd.store_id AS varchar), 4) + ' ' + sd.store_name
	end,


               CASE WHEN sd.store_id IN (130, 174, 188, 205, 215, 217, 228, 229) THEN 'Upstate NY' 
				WHEN sd.store_id IN (119, 124, 150, 177) THEN 'Northwest' 
				WHEN sd.store_id IN (204) THEN 'New England' 
				WHEN sd.store_id IN (13, 136, 473, - 991) THEN 'Web Stores' ELSE sd.bearea 
	END AS bearea, 
				CASE
					WHEN sd.store_id IN (130, 174, 188, 204, 205, 215, 217, 228, 229) THEN 'Upstate NY'
					WHEN sd.store_id IN (119, 124, 150, 177) THEN 'Northwest'
					WHEN sd.store_id IN (13, 136, 473, - 991) THEN 'Web Stores' 
					WHEN sd.bearritory IN ('Southwest','Southeast') AND sd.country = 'GB' THEN sd.bearritory + '-UK'
					ELSE sd.bearritory 
				END AS bearritory, 
				CASE
					WHEN sd.store_id IN (130, 174, 188, 204, 205, 215, 217, 228, 229) THEN 'North US'
					WHEN sd.store_id IN (119, 124, 150, 177) THEN 'West'
					WHEN sd.store_id IN (13, 136, 473, - 991) THEN 'Web Stores'
				ELSE sd.region 
	END AS region, sd.country, d.dma_name, sd.opening_date, 
               dd.day_id AS opening_date_id, 
				sd.closing_date, 
				sd.comp_week_id, 
				dd.period_id AS open_fp_id,
				 dd.week_id AS open_week_id
FROM  dbo.store_dim AS sd LEFT OUTER JOIN
  dbo.demographics_dim AS d ON sd.demographics_bg_key = d.demographics_bg_key LEFT OUTER JOIN
  dbo.date_dim AS dd ON sd.opening_date = dd.actual_date
WHERE (sd.store_id < 990 or sd.store_id > 1999 ) and sd.store_id not in (489, 471)
AND country = 'CA'
```

