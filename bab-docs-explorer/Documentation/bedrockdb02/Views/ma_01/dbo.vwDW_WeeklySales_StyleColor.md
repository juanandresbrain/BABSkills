# dbo.vwDW_WeeklySales_StyleColor

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_WeeklySales_StyleColor"]
    dbo_date_dim(["dbo.date_dim"]) --> VIEW
    dbo_hist_styleclr_loc_wk(["dbo.hist_styleclr_loc_wk"]) --> VIEW
    dbo_location(["dbo.location"]) --> VIEW
    dbo_product_dim(["dbo.product_dim"]) --> VIEW
    dbo_sku(["dbo.sku"]) --> VIEW
    dbo_style(["dbo.style"]) --> VIEW
    dbo_upc(["dbo.upc"]) --> VIEW
    dbo_vwDW_Store(["dbo.vwDW_Store"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.date_dim |
| dbo.hist_styleclr_loc_wk |
| dbo.location |
| dbo.product_dim |
| dbo.sku |
| dbo.style |
| dbo.upc |
| dbo.vwDW_Store |

## View Code

```sql
/*

vwDW_WeeklySales_StyleColor
	o sales_total_retail – currently this column is coming straight from hist_styleclr_loc_wk and is currently 
		native currency. However, after the Merchandising system upgrade, it would become US Dollars. 
		Therefore, this column should now pull from the sales_total_sellcurr_retail column in
		the same table. However, the column should be aliased to keep its original name (as to not break reports, etc.).
	o In addition, if the data being pulled in the view is for UK, this field should be blanked per user requirements. 
		This can be done by checking the division of the current product.

select top 1 * from vwDW_WeeklySales_StyleColor

select top 1 * from [vwDW_WeeklySales_StyleColor_42]

select top 1 * from dw_mirror.dbo.vwDW_Store

select top 1 * from [vwDW_WeeklySales_StyleColor]
	where isnull(sales_total_retail_old,0) <> isnull(sales_total_retail,0)

select top 1 * from dw_mirror.dbo.product_dim p
	where division = 'Uk'

select division 
	, count(*)
	from dw_mirror.dbo.product_dim p
	group by division

select count(*) from [vwDW_WeeklySales_StyleColor_42]


select count(*) from [vwDW_WeeklySales_StyleColor]


select top 1 * from hist_styleclr_loc_wk
*/


CREATE VIEW [dbo].[vwDW_WeeklySales_StyleColor]
AS
SELECT
		-- dimension keys
		CAST(p.product_key AS varchar) AS product_key
		,s.store_key
		,d.date_key

		,sales.merch_year_wk

		-- facts
		,sales.perm_md_retail
		,sales.perm_mu_retail
		,sales.perm_mdc_retail
		,sales.perm_muc_retail
		,sales.promo_pc_total_retail
		,sales.received_units
		,sales.received_retail
		,sales.return_to_vendor_units
		,sales.return_to_vendor_retail
		,sales.distributions_units
		,sales.distributions_retail
		,sales.transfer_in_units
		,sales.transfer_in_retail
		,sales.transfer_out_units
		,sales.transfer_out_retail
		,sales.sales_total_units
		--,case when p.division = 'Uk' then null else sales.sales_total_sellcurr_retail end as sales_total_retail
		,sales.sales_total_sellcurr_retail_te as sales_total_retail
			, sales.sales_total_retail_te as sales_total_retail_us_te
			, sales.sales_total_sellcurr_retail_te as sales_total_retail_native_te
		,sales.sales_total_cost
		,sales.return_units
		,sales.return_sellcurr_retail_te as return_retail
			, sales.return_retail_te as return_retail_us_te
			, sales.return_sellcurr_retail_te as return_retail_native_te
		,sales.return_cost
		,sales.shrink_actual_units
		,sales.shrink_actual_retail
		,sales.adjustments_total_units
		,sales.adjustments_total_retail

	FROM dbo.hist_styleclr_loc_wk sales WITH (NOLOCK)
	INNER JOIN dbo.style WITH (NOLOCK) ON style.style_id = sales.style_id
	INNER JOIN dbo.sku WITH (NOLOCK) ON sku.style_id = sales.style_id AND sku.color_id = sales.color_id
	LEFT JOIN dbo.upc  WITH (NOLOCK) ON upc_id =
		(SELECT TOP 1 u2.upc_id
		FROM upc u2 WITH (NOLOCK)
		WHERE u2.sku_id = sku.sku_id
			AND u2.upc_number < '000001000000'
			/*AND u2.upc_number = '000000' + style.style_code*/)
	INNER JOIN dbo.location l WITH (NOLOCK) ON l.location_id = sales.location_id
	INNER JOIN dw_mirror.dbo.vwDW_Store s WITH (NOLOCK) ON s.store_id = CAST(CAST(l.location_code AS int) AS varchar)
	LEFT JOIN dw_mirror.dbo.product_dim p WITH (NOLOCK) ON p.style_id = sales.style_id
		AND p.color_id = sales.color_id
		AND ((upc.upc_number IS NULL AND p.sku IS NULL) OR (p.sku = CAST(upc.upc_number AS int)))
	LEFT JOIN dw_mirror.dbo.date_dim d WITH (NOLOCK) ON d.fiscal_year = CAST(SUBSTRING(CAST(sales.merch_year_wk AS varchar), 1, 4) AS int)
		AND fiscal_week = CAST(SUBSTRING(CAST(sales.merch_year_wk AS varchar), 5, 2) AS int)
		AND day_of_week = 7
```

