# dbo.view_fcast_group_loc_pd

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_fcast_group_loc_pd"]
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> VIEW
    dbo_color(["dbo.color"]) --> VIEW
    dbo_forecast(["dbo.forecast"]) --> VIEW
    dbo_forecast_detail(["dbo.forecast_detail"]) --> VIEW
    dbo_forecast_sale(["dbo.forecast_sale"]) --> VIEW
    dbo_sku(["dbo.sku"]) --> VIEW
    dbo_style(["dbo.style"]) --> VIEW
    dbo_style_color(["dbo.style_color"]) --> VIEW
    dbo_style_group(["dbo.style_group"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_merch_week |
| dbo.color |
| dbo.forecast |
| dbo.forecast_detail |
| dbo.forecast_sale |
| dbo.sku |
| dbo.style |
| dbo.style_color |
| dbo.style_group |

## View Code

```sql
CREATE view dbo.view_fcast_group_loc_pd AS
SELECT DISTINCT d.location_id,
		d.forecast_run_date,
		d.hierarchy_group_id,
 		(cm.merch_year *100 +cm.merch_period)merch_year_pd, 
		SUM(d.forecast_error) forecast_error,
		SUM(d.safety_stock) safety_stock,
		SUM(d.forecast_value) forecast_value,
		SUM(d.adjustment_factor) adjustment_factor
FROM
(
		SELECT DISTINCT gg.location_id,
			gg.forecast_run_date,
			sg.hierarchy_group_id,
 			gg.merch_year_wk, 
			SUM(gg.forecast_error) forecast_error,
			SUM(gg.safety_stock) safety_stock,
			SUM(gg.forecast_value) forecast_value,
			SUM(gg.adjustment_factor) adjustment_factor
		FROM
		(		--style level
				SELECT DISTINCT 
						fs.forecast_id,
						fs.forecast_detail_id,
						fd.location_id, 
						b.max_forecast_run_date AS forecast_run_date,
						b.style_id, 
						(cw.merch_year *100 +cw.merch_week) AS merch_year_wk,
						fs.adjustment_factor, 
						fs.forecast_value, 
						fs.forecast_error, 
						fs.safety_stock
				FROM forecast f 
				INNER JOIN
					(
						SELECT 
						a.location_id, 
						a.run_date_no_time,
						max(a.forecast_run_date) max_forecast_run_date,
						a.style_id
						FROM 
							(SELECT DISTINCT 
									f.forecast_id,
									fd.forecast_detail_id,
									fd.location_id, 
									convert(smalldatetime,convert(varchar, f.forecast_run_date,101)) AS run_date_no_time,
									f.forecast_run_date,
									fd.style_id 
							FROM forecast f 
							INNER JOIN forecast_detail fd ON f.forecast_id = fd.forecast_id 
							INNER JOIN style s ON fd.style_id IS NOT NULL AND fd.style_id = s.style_id AND fd.style_color_id IS NULL AND fd.sku_id IS NULL
							) a
						GROUP BY 
						a.location_id, 
						a.run_date_no_time,
						a.style_id 
						HAVING max(a.forecast_run_date) = (select MAX(f.forecast_run_date) from forecast f)
					) b ON f.forecast_run_date = b.max_forecast_run_date
				INNER JOIN forecast_detail fd ON f.forecast_id = fd.forecast_id AND fd.style_id IS NOT NULL AND fd.style_id = b.style_id AND fd.location_id = b.location_id
				INNER JOIN forecast_sale fs ON fd.forecast_detail_id = fs.forecast_detail_id
				INNER JOIN calendar_merch_week cw ON cw.calendar_week_id = fs.calendar_week_id

				UNION ALL --style color level
				SELECT DISTINCT 
						fs.forecast_id,
						fs.forecast_detail_id,
						fd.location_id, 
						b.max_forecast_run_date AS forecast_run_date,
						b.style_id, 
						(cw.merch_year *100 +cw.merch_week) AS merch_year_wk,
						fs.adjustment_factor, 
						fs.forecast_value, 
						fs.forecast_error, 
						fs.safety_stock
				FROM forecast f 
				INNER JOIN
					(
						SELECT 
						a.location_id, 
						a.run_date_no_time,
						max(a.forecast_run_date) max_forecast_run_date,
						a.style_id, 
						a.color_id, 
						a.style_color_id
						FROM 
							(SELECT DISTINCT 
									f.forecast_id,
									fd.forecast_detail_id,
									fd.location_id, 
									convert(smalldatetime,convert(varchar, f.forecast_run_date,101)) AS run_date_no_time,
									f.forecast_run_date,
									s.style_id, 
									r.color_id,
									fd.style_color_id
							FROM forecast f 
							INNER JOIN forecast_detail fd ON f.forecast_id = fd.forecast_id 
							INNER JOIN style_color sc ON fd.style_color_id IS NOT NULL AND fd.style_color_id = sc.style_color_id
							INNER JOIN style s ON s.style_id = sc.style_id
							INNER JOIN color r ON r.color_id = sc.color_id
							) a
						GROUP BY 
						a.location_id, 
						a.run_date_no_time,
						a.style_id, 
						a.color_id,
						a.style_color_id 
						HAVING max(a.forecast_run_date) = (select MAX(f.forecast_run_date) from forecast f)
					) b ON f.forecast_run_date = b.max_forecast_run_date
				INNER JOIN forecast_detail fd ON f.forecast_id = fd.forecast_id AND fd.style_color_id IS NOT NULL AND fd.style_color_id = b.style_color_id AND fd.location_id = b.location_id
				INNER JOIN forecast_sale fs ON fd.forecast_detail_id = fs.forecast_detail_id
				INNER JOIN calendar_merch_week cw ON cw.calendar_week_id = fs.calendar_week_id
				
				UNION ALL --sku level
				SELECT DISTINCT 
						fs.forecast_id,
						fs.forecast_detail_id,
						fd.location_id, 
						b.max_forecast_run_date AS forecast_run_date,
						b.style_id, 
						(cw.merch_year *100 +cw.merch_week) AS merch_year_wk,
						fs.adjustment_factor, 
						fs.forecast_value, 
						fs.forecast_error, 
						fs.safety_stock
				FROM forecast f 
				INNER JOIN
					(
						SELECT 
						a.location_id, 
						a.run_date_no_time,
						max(a.forecast_run_date) max_forecast_run_date,
						a.style_id, 
						a.color_id, 
						a.size_master_id,
						a.sku_id 
						FROM 
							(SELECT DISTINCT 
									f.forecast_id,
									fd.forecast_detail_id,
									fd.location_id, 
									convert(smalldatetime,convert(varchar, f.forecast_run_date,101)) AS run_date_no_time,
									f.forecast_run_date,
									sk.style_id, 
									sk.color_id, 
									sk.size_master_id,
									fd.sku_id 
							FROM forecast f 
							INNER JOIN forecast_detail fd ON f.forecast_id = fd.forecast_id 
							INNER JOIN sku sk ON fd.sku_id IS NOT NULL AND fd.sku_id = sk.sku_id
							) a
						GROUP BY 
						a.location_id, 
						a.run_date_no_time,
						a.style_id, 
						a.color_id, 
						a.size_master_id,
						a.sku_id 
						HAVING max(a.forecast_run_date) = (select MAX(f.forecast_run_date) from forecast f)
					) b ON f.forecast_run_date = b.max_forecast_run_date
				INNER JOIN forecast_detail fd ON f.forecast_id = fd.forecast_id AND fd.sku_id IS NOT NULL AND fd.sku_id = b.sku_id AND fd.location_id = b.location_id
				INNER JOIN forecast_sale fs ON fd.forecast_detail_id = fs.forecast_detail_id
				INNER JOIN calendar_merch_week cw ON cw.calendar_week_id = fs.calendar_week_id
		)
		gg
		INNER JOIN style_group sg ON gg.style_id = sg.style_id
		GROUP BY gg.location_id,
			gg.forecast_run_date,
			sg.hierarchy_group_id,
 			gg.merch_year_wk

)
d
INNER JOIN calendar_merch_week cm ON d.merch_year_wk =(cm.merch_year *100 +cm.merch_week)
GROUP BY d.location_id,
	     d.forecast_run_date,
	     d.hierarchy_group_id,
 	     (cm.merch_year *100 +cm.merch_period)
```

