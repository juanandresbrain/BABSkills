# dbo.vwDW_WeeklyOnHand_StyleColor_v2

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_WeeklyOnHand_StyleColor_v2"]
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
CREATE VIEW [dbo].[vwDW_WeeklyOnHand_StyleColor_v2]
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
		,case when (p.jurisdiction_code = 'Uk'OR p.division = 'Uk') then null  
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

	FROM dbo.hist_oh_styleclr_loc_wk oh
	INNER JOIN dbo.style WITH (NOLOCK) 
		ON style.style_id = oh.style_id
	INNER JOIN dbo.sku WITH (NOLOCK) 
		ON sku.style_id = oh.style_id AND sku.color_id = oh.color_id
	LEFT JOIN dbo.upc ON upc_id = (SELECT TOP 1 u2.upc_id
											FROM upc u2 WITH (NOLOCK)
											WHERE u2.sku_id = sku.sku_id
												AND u2.upc_number < '000001000000'
												/*AND u2.upc_number = '000000' + style.style_code*/)
	INNER JOIN dbo.location l WITH (NOLOCK)
		ON l.location_id = oh.location_id
	INNER JOIN dw_mirror.dbo.vwDW_Store s WITH (NOLOCK)
		ON s.store_id = CAST(CAST(l.location_code AS int) AS varchar)
	LEFT JOIN dw_mirror.dbo.product_dim p WITH (NOLOCK)
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

	left join oo_all_styleclr_loc_wk oo
        on oo.style_id = oh.style_id
            and oo.color_id = oh.color_id
            and oo.location_id = oh.location_id
            and oo.merch_year_wk = oh.merch_year_wk






dbo,vwDW_WeeklyOnOrder_Style,CREATE VIEW [dbo].[vwDW_WeeklyOnOrder_Style]
AS
-- =============================================================================================================
-- Name: [dbo].[vwDW_WeeklyOnOrder_Style]
--
-- Description: View underlying the SSAS Merchandising Cube used on the dashboard.   
-- Aggregates Weekly Sales information by Style.  
-- Creates dummy products by concatenating subclass_code and style_code 
--
-- Joins dbo.oo_all_style_loc_wk, dbo.location to
-- dw_mirror.dbo.vwDW_Store, dw_mirror.dbo.product_dim and dw_mirror.dbo.date_dim
--
-- Dependencies: 
--
-- Revision History
--		Name:					Date:			Comments:

--		Funmi Agbebi			4/30/2010		dw_mirror.dbo.product_dim.jurisdiction_id pulled in 
--												jurisdiction_id added to product_key for dummy products 
--												with introduction of products into the R-B-Z division
--		Outside Consultant		2006			original creation
-- =============================================================================================================


	SELECT
		-- dimension keys
		--	Commented out 4/30/2010 (FA )
--		p.subclass_code + '-' + p.style_code AS product_key

		-- Additional fields starts (FA - 4/30/2010)
		p.subclass_code + '-' + p.style_code + '-' + cast(p.jurisdiction_id as varchar(2)) AS product_key
		,p.jurisdiction_id as product_jurisdiction_id
		,l.jurisdiction_id as location_jurisdiction_id
		-- Additional fields ends (FA - 4/30/2010)

		,s.store_key
		,d.date_key

		,oo.merch_year_wk

		-- facts
		,oo.on_order_cost

	FROM dbo.oo_all_style_loc_wk oo  WITH (NOLOCK) 
	INNER JOIN dbo.location l  WITH (NOLOCK)  ON l.location_id = oo.location_id
	INNER JOIN dw_mirror.dbo.vwDW_Store s  WITH (NOLOCK) ON s.store_id = CAST(CAST(l.location_code AS int) AS varchar)
	LEFT JOIN dw_mirror.dbo.product_dim p  WITH (NOLOCK) ON p.product_key = (SELECT TOP 1 p2.product_key FROM dw_mirror.dbo.product_dim p2  WITH (NOLOCK) WHERE p2.style_id = oo.style_id)
	LEFT JOIN dw_mirror.dbo.date_dim d  WITH (NOLOCK) ON d.fiscal_year = CAST(SUBSTRING(CAST(oo.merch_year_wk AS varchar), 1, 4) AS int)
		AND fiscal_week = CAST(SUBSTRING(CAST(oo.merch_year_wk AS varchar), 5, 2) AS int)
		AND day_of_week = 7
```

