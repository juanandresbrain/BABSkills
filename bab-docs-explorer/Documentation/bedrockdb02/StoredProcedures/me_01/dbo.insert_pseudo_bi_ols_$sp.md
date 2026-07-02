# dbo.insert_pseudo_bi_ols_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.insert_pseudo_bi_ols_$sp"]
    dbo_count_import_sku_temp(["dbo.count_import_sku_temp"]) --> SP
    dbo_country(["dbo.country"]) --> SP
    dbo_currency_conversion(["dbo.currency_conversion"]) --> SP
    dbo_inv_control_merch(["dbo.inv_control_merch"]) --> SP
    dbo_inventory_control_loc(["dbo.inventory_control_loc"]) --> SP
    dbo_inventory_count_detail(["dbo.inventory_count_detail"]) --> SP
    dbo_jurisdiction(["dbo.jurisdiction"]) --> SP
    dbo_location(["dbo.location"]) --> SP
    dbo_merch_group_parent(["dbo.merch_group_parent"]) --> SP
    dbo_sku(["dbo.sku"]) --> SP
    dbo_style(["dbo.style"]) --> SP
    dbo_style_group(["dbo.style_group"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.count_import_sku_temp |
| dbo.country |
| dbo.currency_conversion |
| dbo.inv_control_merch |
| dbo.inventory_control_loc |
| dbo.inventory_count_detail |
| dbo.jurisdiction |
| dbo.location |
| dbo.merch_group_parent |
| dbo.sku |
| dbo.style |
| dbo.style_group |

## Stored Procedure Code

```sql
create proc [dbo].[insert_pseudo_bi_ols_$sp] 

(
	@DocId AS DECIMAL(12,0), 
	@IclId AS DECIMAL(13,0), 
	@LocId AS SMALLINT, 
	@DocDate AS SMALLDATETIME, 
	@LastItemId AS DECIMAL, 
	@HierarchyLevelId AS DECIMAL, 
	@ParentLevelId AS DECIMAL,
	@ReplaceOrInc AS SMALLINT
)
AS

/* 
Proc name: insert_pseudo_bi_ols_$sp 
Description: Procedure called by pi_process_loc_$sp for a physical inventory document of type beginning inventory and for pseudo-styles
	Steps:
		1.  	Retrieve skus that have been counted.
		2.  	Determine skus that satisfy criteria on the document and insert them into the inventory_count_detail table if 
		    	they do not already exist in the table.  Insert these details with counts of zero for now.
		3.	Update the units_counted, extended_units_counted, cost and total_retail columns.

HISTORY: 
Date       	Name         	Def#	Desc
Sept01,04   	Sameer Patel   	21616	Part of performance improvements for physical inventory
Feb 2, 2010		Feng			Multi Currency mod. add/set cost_local, total_cost_local, total_valuation_retail
*/

BEGIN

/*--------------------------------------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------*/
-- Declartions of various temporary tables
CREATE TABLE [#sku_loc] (
		[sku_id] decimal(13, 0) NOT NULL ,
		[sku_loc_id] decimal (13,0) identity)

/*--------------------------------------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------*/
-- Get skus that were imported through a file
-- If counted from the GUI, skus have already been inserted into the inventory_count_detail table

	-- Get skus that were counted
	SELECT
		sku.sku_id,
		SUM(count_import_sku_temp.cost) cost,
		SUM(count_import_sku_temp.cost_local) cost_local,
		SUM(count_import_sku_temp.total_retail) total_retail,
		SUM(count_import_sku_temp.total_valuation_retail) total_valuation_retail,
		SUM(count_import_sku_temp.units_counted) units_counted,
		SUM(count_import_sku_temp.units_counted) extended_units_counted
	INTO #PI_SKU_OH_TEMP
	FROM
		count_import_sku_temp,
		sku
	WHERE
		count_import_sku_temp.location_id = @LocId
		AND count_import_sku_temp.sku_id = sku.sku_id
		AND count_import_sku_temp.total_retail IS NOT NULL
	GROUP BY
		sku.sku_id
	
	If (ISNULL(@HierarchyLevelId, 0) <> 0 AND ISNULL(@ParentLevelId, 0) = 0) -- Chain-level count
		
		BEGIN

			INSERT INTO 
				#sku_loc
			SELECT 
				sku.sku_id
			FROM
				#PI_SKU_OH_TEMP,
				sku,
				style
			WHERE
				sku.sku_id = #PI_SKU_OH_TEMP.sku_id
				AND style.style_id = sku.style_id
				AND style.style_type = 2
				AND NOT EXISTS
			 		(
						SELECT 1
						FROM
							inventory_count_detail WITH (NOLOCK)
						WHERE
							inventory_count_detail.sku_id = #PI_SKU_OH_TEMP.sku_id
							AND inventory_count_detail.inventory_control_id = @DocId
							AND inventory_count_detail.inventory_control_loc_id = @IclId
					)

		END

	ELSE IF (ISNULL(@HierarchyLevelId, 0) <> 0 AND ISNULL(@ParentLevelId, 0) <> 0) -- Non chain-level count
		
		BEGIN

			INSERT INTO 
				#sku_loc
			SELECT
				sku.sku_id
			FROM
				#PI_SKU_OH_TEMP,
				inv_control_merch,
				merch_group_parent,
				style_group,
				sku,
				style
			WHERE
				#PI_SKU_OH_TEMP.sku_id = sku.sku_id
				AND inv_control_merch.hierarchy_group_id = merch_group_parent.parent_hierarchy_group_id	
				AND inv_control_merch.inventory_control_id = @DocId
				AND merch_group_parent.hierarchy_group_id = style_group.hierarchy_group_id
				AND style_group.style_id = sku.style_id
				AND style.style_id = sku.style_id
				AND style.style_id = style_group.style_id
				AND style.style_type = 2
				AND NOT EXISTS
			 		(
						SELECT 1
						FROM
							inventory_count_detail WITH (NOLOCK)
						WHERE
							inventory_count_detail.sku_id = #PI_SKU_OH_TEMP.sku_id
							AND inventory_count_detail.inventory_control_id = @DocId
							AND inventory_count_detail.inventory_control_loc_id = @IclId
					)

		END

	ELSE IF (ISNULL(@HierarchyLevelId, 0) = 0 AND ISNULL(@ParentLevelId, 0) = 0) -- Non chain-level count
		
		BEGIN

			INSERT INTO 
				#sku_loc
			SELECT
				sku.sku_id
			FROM
				#PI_SKU_OH_TEMP,
				inv_control_merch,
				sku,
				style
			WHERE
				#PI_SKU_OH_TEMP.sku_id = sku.sku_id
				AND inv_control_merch.style_id = sku.style_id
				AND style.style_id = sku.style_id
				AND style.style_type = 2
				AND inv_control_merch.inventory_control_id = @DocId
				AND NOT EXISTS
			 		(
						SELECT 1
						FROM
							inventory_count_detail WITH (NOLOCK)
						WHERE
							inventory_count_detail.sku_id = #PI_SKU_OH_TEMP.sku_id
							AND inventory_count_detail.inventory_control_id = @DocId
							AND inventory_count_detail.inventory_control_loc_id = @IclId
					)

		END

	INSERT INTO
		inventory_count_detail (inventory_count_detail_id, inventory_control_loc_id, inventory_control_id, sku_id, units_counted, extended_units_counted)
	SELECT
		(@IclId * 1000000) + @LastItemId + sku_loc_id,
		@IclId,
		@DocId,
		sku_id,
		0 units_counted,
		0 extended_units_counted
	FROM
		#sku_loc
	-- Update last_item_id in inventory_control_loc_table

	UPDATE
		inventory_control_loc
	SET
		last_item_id = (SELECT ISNULL(@LastItemId + MAX(#sku_loc.sku_loc_id), @LastItemId) FROM #sku_loc)
	WHERE
		inventory_control_loc_id = @IclId
		AND inventory_control_id = @DocId

/*--------------------------------------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------*/
-- Update units_counted, extended_units_counted, cost and total_retail columns

	IF @ReplaceOrInc = 0

		BEGIN

			UPDATE
				inventory_count_detail
			SET 
				inventory_count_detail.extended_units_counted = inventory_count_detail.units_counted,
				inventory_count_detail.total_cost = inventory_count_detail.cost,
				inventory_count_detail.total_cost_local = inventory_count_detail.cost_local
			FROM
				inventory_count_detail WITH (NOLOCK)
			WHERE
				inventory_count_detail.inventory_control_id = @DocId
				AND inventory_count_detail.inventory_control_loc_id = @IclId
				AND inventory_count_detail.pack_id IS NULL

		END

	ELSE IF @ReplaceOrInc = 1 -- replace count
	
		BEGIN

			UPDATE
				inventory_count_detail
			SET 
				inventory_count_detail.units_counted = #PI_SKU_OH_TEMP.units_counted,
				inventory_count_detail.extended_units_counted = #PI_SKU_OH_TEMP.extended_units_counted,
				inventory_count_detail.cost = #PI_SKU_OH_TEMP.cost,
				inventory_count_detail.cost_local = #PI_SKU_OH_TEMP.cost_local,
				inventory_count_detail.total_cost = #PI_SKU_OH_TEMP.cost,
				inventory_count_detail.total_cost_local = #PI_SKU_OH_TEMP.cost_local,
				inventory_count_detail.total_retail = #PI_SKU_OH_TEMP.total_retail,
				inventory_count_detail.total_valuation_retail = #PI_SKU_OH_TEMP.total_valuation_retail
			FROM
				inventory_count_detail WITH (NOLOCK),
				#PI_SKU_OH_TEMP
			WHERE
				inventory_count_detail.sku_id = #PI_SKU_OH_TEMP.sku_id		
				AND inventory_count_detail.inventory_control_id = @DocId
				AND inventory_count_detail.inventory_control_loc_id = @IclId
				AND inventory_count_detail.pack_id IS NULL

		END

	ELSE IF @ReplaceOrInc = 2 -- increment count
	
		BEGIN

			UPDATE
				inventory_count_detail
			SET 
				inventory_count_detail.units_counted = inventory_count_detail.units_counted + #PI_SKU_OH_TEMP.units_counted,
				inventory_count_detail.extended_units_counted = inventory_count_detail.extended_units_counted + #PI_SKU_OH_TEMP.extended_units_counted,
				inventory_count_detail.cost = #PI_SKU_OH_TEMP.cost,
				inventory_count_detail.cost_local = #PI_SKU_OH_TEMP.cost_local,
				inventory_count_detail.total_cost = #PI_SKU_OH_TEMP.cost,
				inventory_count_detail.total_cost_local = #PI_SKU_OH_TEMP.cost_local,
				inventory_count_detail.total_retail = #PI_SKU_OH_TEMP.total_retail,
				inventory_count_detail.total_valuation_retail = #PI_SKU_OH_TEMP.total_valuation_retail
			FROM
				inventory_count_detail WITH (NOLOCK),
				#PI_SKU_OH_TEMP
			WHERE
				inventory_count_detail.sku_id = #PI_SKU_OH_TEMP.sku_id		
				AND inventory_count_detail.inventory_control_id = @DocId
				AND inventory_count_detail.inventory_control_loc_id = @IclId
				AND inventory_count_detail.pack_id IS NULL

		END

/*--------------------------------------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------*/
-- PSEUDO-STYLE / INTERNATIONATIONALIZATION CHANGES

	-- Determine exchange rate
	DECLARE @ExchangeRate AS FLOAT
	
	SELECT
		@ExchangeRate = exchange_rate
	FROM
		currency_conversion
	WHERE
		to_currency_id = 
			(
				SELECT
					currency_id from_currency_id
				FROM
					country,
					jurisdiction,
					location
				WHERE
					location.jurisdiction_id = jurisdiction.jurisdiction_id
					AND country.country_id= jurisdiction.country_id
					AND location.location_id = @LocId
			)
		AND from_currency_id = 
			(
				SELECT
					currency_id to_currency_id
				FROM
					country,
					jurisdiction
				WHERE
					country.country_id= jurisdiction.country_id
					AND jurisdiction.home_jurisdiction_flag = 1
			)
		AND effective_from_date <= @DocDate
		AND (effective_to_date >= @DocDate OR effective_to_date IS NULL)
		AND currency_conversion_type = 2

	-- Calculate the total_valuation_retail based on the total_retail (selling) for pseudo-styles
	UPDATE
		inventory_count_detail
	SET
		total_valuation_retail = total_retail * @ExchangeRate
	WHERE
		inventory_count_detail.total_retail IS NOT NULL
		AND inventory_count_detail.inventory_control_id = @DocId
		AND inventory_count_detail.inventory_control_loc_id = @IclId
		AND inventory_count_detail.pack_id IS NULL
		AND inventory_count_detail.total_valuation_retail IS NULL

/*--------Multi currency mod --------------------------------------------------------------------*/
-- Determine purchasing exchange rate
	DECLARE @ExchangeRate1 AS FLOAT
	
	SELECT
		@ExchangeRate1 = exchange_rate
	FROM
		currency_conversion
	WHERE
		to_currency_id = 
			(
				SELECT
					currency_id from_currency_id
				FROM
					country,
					jurisdiction,
					location
				WHERE
					location.jurisdiction_id = jurisdiction.jurisdiction_id
					AND country.country_id= jurisdiction.country_id
					AND location.location_id = @LocId
			)
		AND from_currency_id = 
			(
				SELECT
					currency_id to_currency_id
				FROM
					country,
					jurisdiction
				WHERE
					country.country_id= jurisdiction.country_id
					AND jurisdiction.home_jurisdiction_flag = 1
			)
		AND effective_from_date <= @DocDate
		AND (effective_to_date >= @DocDate OR effective_to_date IS NULL)
		AND currency_conversion_type = 1

--update cost_local, total_cost_local
	UPDATE
		inventory_count_detail
	SET
		cost_local = cost / @ExchangeRate1
	WHERE
		inventory_count_detail.cost IS NOT NULL
		AND inventory_count_detail.inventory_control_id = @DocId
		AND inventory_count_detail.inventory_control_loc_id = @IclId
		AND inventory_count_detail.pack_id IS NULL
		AND inventory_count_detail.cost_local IS NULL
--update total_cost_local
	UPDATE
		inventory_count_detail
	SET
		total_cost_local = cost / @ExchangeRate1
	WHERE
		inventory_count_detail.cost IS NOT NULL
		AND inventory_count_detail.inventory_control_id = @DocId
		AND inventory_count_detail.inventory_control_loc_id = @IclId
		AND inventory_count_detail.pack_id IS NULL
		AND inventory_count_detail.total_cost_local IS NULL

/*--------------------------------------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------*/

	DROP TABLE #sku_loc
	DROP TABLE #PI_SKU_OH_TEMP
		
/*--------------------------------------------------------------------------------------------------------------*/

END
```

