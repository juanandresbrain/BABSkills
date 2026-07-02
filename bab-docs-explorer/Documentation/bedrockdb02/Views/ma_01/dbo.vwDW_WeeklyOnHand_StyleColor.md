# dbo.vwDW_WeeklyOnHand_StyleColor

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_WeeklyOnHand_StyleColor"]
    dbo_date_dim(["dbo.date_dim"]) --> VIEW
    dbo_hist_oh_styleclr_loc_wk(["dbo.hist_oh_styleclr_loc_wk"]) --> VIEW
    dbo_location(["dbo.location"]) --> VIEW
    dbo_oo_all_styleclr_loc_wk(["dbo.oo_all_styleclr_loc_wk"]) --> VIEW
    dbo_product_dim(["dbo.product_dim"]) --> VIEW
    dbo_sku(["dbo.sku"]) --> VIEW
    dbo_style(["dbo.style"]) --> VIEW
    dbo_style_retail(["dbo.style_retail"]) --> VIEW
    dbo_upc(["dbo.upc"]) --> VIEW
    dbo_vwDW_Store(["dbo.vwDW_Store"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.date_dim |
| dbo.hist_oh_styleclr_loc_wk |
| dbo.location |
| dbo.oo_all_styleclr_loc_wk |
| dbo.product_dim |
| dbo.sku |
| dbo.style |
| dbo.style_retail |
| dbo.upc |
| dbo.vwDW_Store |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_WeeklyOnHand_StyleColor]
AS
SELECT
		-- dimension keys
		CAST(p.product_key AS varchar) AS product_key
		,s.store_key
		,d.date_key
		,oh.inventory_status_id
		,oh.price_status_id

		,oh.merch_year_wk
		,oh.style_id
		,oh.color_id
		,oh.location_id
		,oh.on_hand_units
			, oh.on_hand_units as on_hand_units_woa
			, oo.allocation_units  as allocation_units

--Changed for Oct 2008 go-live to match Mark's validation query for OH Retail
			, oh.on_hand_retail as on_hand_retail
-- Tax exclusive USD - Keith L 4/29/2010
			, oh.on_hand_retail_te as on_hand_retail_te

		,case when (p.division = 'Uk' OR p.jurisdiction_code = 'Uk') then null  
			else (oh.on_hand_units) * isnull(sr.current_sellcurr_retail,0) 
		  end as on_hand_retail_old
				


--Changed for Oct 2008 go-live to match Mark's validation query for OH retail
--		,case when p.division = 'Uk' then null  
--			else (oh.on_hand_units) * isnull(sr.current_sellcurr_retail,0) 
--		  end as on_hand_retail
--			, oh.on_hand_retail as on_hand_retail_old
--		
			, sr.current_sellcurr_retail as current_retail_native
			, sr.current_retail
			, l.location_code

	FROM dbo.hist_oh_styleclr_loc_wk oh WITH (NOLOCK) 
	INNER JOIN dbo.style WITH (NOLOCK) 
		ON style.style_id = oh.style_id
	INNER JOIN dbo.sku WITH (NOLOCK) 
		ON sku.style_id = oh.style_id AND sku.color_id = oh.color_id
	LEFT JOIN dbo.upc  WITH (NOLOCK) ON upc_id = (SELECT TOP 1 u2.upc_id
											FROM upc u2 WITH (NOLOCK)
											WHERE u2.sku_id = sku.sku_id
												AND u2.upc_number < '000001000000'
												/*AND u2.upc_number = '000000' + style.style_code*/)
	INNER JOIN dbo.location l WITH (NOLOCK)
		ON l.location_id = oh.location_id
	INNER JOIN dw_mirror.dbo.vwDW_Store s WITH (NOLOCK)
		ON s.store_id = CAST(CAST(l.location_code AS int) AS varchar)
	left JOIN dw_mirror.dbo.product_dim p WITH (NOLOCK)
		ON p.style_id = oh.style_id
		AND p.color_id = oh.color_id
		AND ((upc.upc_number IS NULL AND p.sku IS NULL) OR (p.sku = CAST(upc.upc_number AS int)))
	LEFT JOIN dw_mirror.dbo.date_dim d WITH (NOLOCK)
		ON d.fiscal_year = CAST(SUBSTRING(CAST(oh.merch_year_wk AS varchar), 1, 4) AS int)
		AND fiscal_week = CAST(SUBSTRING(CAST(oh.merch_year_wk AS varchar), 5, 2) AS int)
		AND day_of_week = 7

	inner join style_retail sr WITH (NOLOCK)
		on sr.style_id = oh.style_id
			and sr.jurisdiction_id = l.jurisdiction_id

	left join oo_all_styleclr_loc_wk oo WITH (NOLOCK) 
        on oo.style_id = oh.style_id
            and oo.color_id = oh.color_id
            and oo.location_id = oh.location_id
            and oo.merch_year_wk = oh.merch_year_wk
```

