# dbo.insert_pseudo_ols_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.insert_pseudo_ols_$sp"]
    dbo_count_import_sku_temp(["dbo.count_import_sku_temp"]) --> SP
    dbo_country(["dbo.country"]) --> SP
    dbo_currency_conversion(["dbo.currency_conversion"]) --> SP
    dbo_ib_inventory(["dbo.ib_inventory"]) --> SP
    dbo_ib_inventory_total(["dbo.ib_inventory_total"]) --> SP
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
| dbo.ib_inventory |
| dbo.ib_inventory_total |
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
CREATE proc [dbo].[insert_pseudo_ols_$sp] 
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
Proc name: insert_pseudo_$sp 
Description: Procedure called by pi_process_loc_$sp for a physical inventory document of type actual shrink and for pseudo-styles
	Steps:
		1.  	Retrieve skus that have been counted as well as skus that have not been counted but exist in ib_inventory.
			Also retrieve there corresponding units counted and on hand book and in transit units, costs and retails
		2.  	Determine skus that satisfy criteria on the document and insert them into the inventory_count_detail table if 
		    	they do not already exist in the table.  Insert these details with counts of zero for now.
		3.	Update the units_counted, extended_units_counted, and the columns that store the on-hand book and in-transit values

HISTORY: 
Date       	Name         	Def#	Desc
Apr27,09        Michel Benoit   109897  missing batch terminator on last line
Dec10,04        Jacqueline Lin  45792   im throwing error which prevents segment 53005 from running
Sept01,04   	Sameer Patel   	21616	Part of performance improvements for physical inventory
Feb 2, 2010		Feng			multi currency mod, add/set cost_local, total_valuation_retail, total_oh_book_cost_local, total_oh_in_transit_cost_local fields
April 26, 2010		Feng		Increase precision from 2 to 6 for cost fields
*/

BEGIN

/*--------------------------------------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------*/
-- Declartions of various temporary tables

	CREATE TABLE [#sku_loc] (
		[sku_id] decimal(13, 0) NOT NULL ,
		[sku_loc_id] decimal (13,0) identity)

	CREATE TABLE [#PI_SKU_OH_TEMP] (
		[sku_id] decimal(13, 0) NOT NULL ,
		[cost] decimal (18,6) NOT NULL ,
		[cost_local] decimal (18,6) NOT NULL ,
		[total_retail] decimal (14,2) NOT NULL ,
		[total_valuation_retail] decimal (14,2) NOT NULL ,
		[units_counted] decimal (10,0) NOT NULL ,
		[extended_units_counted] decimal (10,0) NOT NULL ,
		[total_oh_book_units] decimal (10, 0) NOT NULL ,
		[total_oh_book_cost] decimal (18,6) NOT NULL ,
		[total_oh_book_cost_local] decimal (18,6) NOT NULL ,
		[total_oh_book_val_retail] decimal (14,2) NOT NULL ,
		[total_oh_book_sell_retail] decimal (14,2) NOT NULL ,
		[total_oh_in_transit_units] decimal (10, 0) NOT NULL ,
		[total_oh_in_transit_cost] decimal (18,6) NOT NULL ,
		[total_oh_in_transit_cost_local] decimal (18,6) NOT NULL ,
		[total_oh_in_tran_val_retail] decimal (14,2) NOT NULL, 
		[total_oh_in_tran_sell_retail] decimal (14,2) NOT NULL) 

	CREATE  NONCLUSTERED  INDEX [#PI_SKU_OH_TEMP_$ndx1] ON [dbo].[#PI_SKU_OH_TEMP]([sku_id])

/*--------------------------------------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------*/
-- Insert skus from pseudo-styles that satisfy criteria from the inv_control_merch table into the inventory_count_detail table
-- that have inventory in ib_inventory

	-- Get disticints skus that exist in ib_inventory
	IF @ReplaceOrInc = 0
		
		BEGIN

			INSERT INTO 
				#PI_SKU_OH_TEMP
			SELECT
				IB_TOTAL.sku_id,
				SUM(cost) cost,
				SUM(cost_local) cost_local,
				SUM(total_retail) total_retail,
				SUM(total_valuation_retail) total_valuation_retail,
				ISNULL(SUM(units_counted), 0) units_counted,
				ISNULL(SUM(extended_units_counted), 0) extended_units_counted,
				ISNULL(SUM(IB_TOTAL.total_oh_book_units), 0) - ISNULL(SUM(IB.post_oh_book_units), 0) total_oh_book_units,
				ISNULL(SUM(IB_TOTAL.total_oh_book_cost), 0) - ISNULL(SUM(IB.post_oh_book_cost), 0) total_oh_book_cost,
				ISNULL(SUM(IB_TOTAL.total_oh_book_cost_local), 0) - ISNULL(SUM(IB.post_oh_book_cost_local), 0) total_oh_book_cost_local,
				ISNULL(SUM(IB_TOTAL.total_oh_book_val_retail), 0) - ISNULL(SUM(IB.post_oh_book_val_retail), 0) total_oh_book_val_retail,
				ISNULL(SUM(IB_TOTAL.total_oh_book_sell_retail), 0) - ISNULL(SUM(IB.post_oh_book_sell_retail), 0) total_oh_book_sell_retail,
				ISNULL(SUM(IB_TOTAL.total_oh_in_transit_units), 0) - ISNULL(SUM(IB.post_oh_in_transit_units), 0) total_oh_in_transit_units,
				ISNULL(SUM(IB_TOTAL.total_oh_in_transit_cost), 0) - ISNULL(SUM(IB.post_oh_in_transit_cost), 0) total_oh_in_transit_cost,
				ISNULL(SUM(IB_TOTAL.total_oh_in_transit_cost_local), 0) - ISNULL(SUM(IB.post_oh_in_transit_cost_local), 0) total_oh_in_transit_cost_local,
				ISNULL(SUM(IB_TOTAL.total_oh_in_tran_val_retail), 0) - ISNULL(SUM(IB.post_oh_in_tran_val_retail), 0) total_oh_in_tran_val_retail,
				ISNULL(SUM(IB_TOTAL.total_oh_in_tran_sell_retail), 0) - ISNULL(SUM(IB.post_oh_in_tran_sell_retail), 0) total_oh_in_tran_sell_retail
			FROM
				(
					SELECT
						sku.sku_id,
						0 units_counted,
						0 extended_units_counted,
						0 cost,
						0 cost_local,
						0 total_retail,
						0 total_valuation_retail,
						SUM(total_on_hand_units) total_oh_book_units,
						SUM(total_on_hand_cost) total_oh_book_cost,
						SUM(total_on_hand_cost_local) total_oh_book_cost_local,
						SUM(total_on_hand_valuation_retail) total_oh_book_val_retail,
						SUM(total_on_hand_selling_retail) total_oh_book_sell_retail,
						0 total_oh_in_transit_units,
						0 total_oh_in_transit_cost,
						0 total_oh_in_transit_cost_local,
						0 total_oh_in_tran_val_retail,
						0 total_oh_in_tran_sell_retail
					FROM
						ib_inventory_total,
						sku,
						style
					WHERE
						location_id = @LocId
						AND inventory_status_id <> 2
						AND sku.sku_id = ib_inventory_total.sku_id
						AND style.style_id = sku.style_id
						AND style.style_type = 2
					GROUP BY 
						sku.sku_id
					UNION ALL
					SELECT
						sku.sku_id,
						0 units_counted,
						0 extended_units_counted,
						0 cost,
						0 cost_local,
						0 total_retail,
						0 total_valuation_retail,
						0 total_oh_book_units,
						0 total_oh_book_cost,
						0 total_oh_book_cost_local,
						0 total_oh_book_val_retail,
						0 total_oh_book_sell_retail,
						SUM(total_on_hand_units) total_oh_in_transit_units,
						SUM(total_on_hand_cost) total_oh_in_transit_cost,
						SUM(total_on_hand_cost_local) total_oh_in_transit_cost_local,
						SUM(total_on_hand_valuation_retail) total_oh_in_tran_val_retail,
						SUM(total_on_hand_selling_retail) total_oh_in_tran_sell_retail
					FROM
						ib_inventory_total,
						sku,
						style
					WHERE
						location_id = @LocId
						AND inventory_status_id = 2
						AND sku.sku_id = ib_inventory_total.sku_id
						AND style.style_id = sku.style_id
						AND style.style_type = 2
					GROUP BY 
						sku.sku_id
					UNION ALL
					SELECT
						sku_id,
						inventory_count_detail.units_counted,
						inventory_count_detail.units_counted extended_units_counted,
						inventory_count_detail.cost cost,
						inventory_count_detail.cost_local cost_local,
						inventory_count_detail.total_retail total_retail,
						inventory_count_detail.total_valuation_retail total_valuation_retail,
						0 total_oh_book_units,
						0 total_oh_book_cost,
						0 total_oh_book_cost_local,
						0 total_oh_book_val_retail,
						0 total_oh_book_sell_retail,
						0 total_oh_in_transit_units,
						0 total_oh_in_transit_cost,
						0 total_oh_in_transit_cost_local,
						0 total_oh_in_tran_val_retail,
						0 total_oh_in_tran_sell_retail
					FROM
						inventory_count_detail
					WHERE
						inventory_control_loc_id = @IclId
						AND inventory_control_id = @DocId
						AND total_retail IS NOT NULL
				) IB_TOTAL
			LEFT OUTER JOIN
				(
					SELECT
						sku.sku_id,
						SUM(transaction_units) post_oh_book_units,
						SUM(transaction_cost) post_oh_book_cost,
						SUM(transaction_cost_local) post_oh_book_cost_local,
						SUM(transaction_valuation_retail) post_oh_book_val_retail,
						SUM(transaction_selling_retail) post_oh_book_sell_retail,
						0 post_oh_in_transit_units,
						0 post_oh_in_transit_cost,
						0 post_oh_in_transit_cost_local,
						0 post_oh_in_tran_val_retail,
						0 post_oh_in_tran_sell_retail
					FROM
						ib_inventory,
						sku,
						style
					WHERE
						location_id = @LocId
						AND inventory_status_id <> 2
						AND transaction_date > CONVERT (DATETIME, @DocDate, 101)
						AND sku.sku_id = ib_inventory.sku_id
						AND style.style_id = sku.style_id
						AND style.style_type = 2
					GROUP BY 
						sku.sku_id
					UNION ALL
					SELECT
						sku.sku_id,
						0 post_oh_book_units,
						0 post_oh_book_cost,
						0 post_oh_book_cost_local,
						0 post_oh_book_val_retail,
						0 post_oh_book_sell_retail,
						SUM(transaction_units) post_oh_in_transit_units,
						SUM(transaction_cost) post_oh_in_transit_cost,
						SUM(transaction_cost_local) post_oh_in_transit_cost_local,
						SUM(transaction_valuation_retail) post_oh_in_tran_val_retail,
						SUM(transaction_selling_retail) post_oh_in_tran_sell_retail
					FROM
						ib_inventory,
						sku,
						style
					WHERE
						location_id = @LocId
						AND inventory_status_id = 2
						AND transaction_date > CONVERT (DATETIME, @DocDate, 101)
						AND sku.sku_id = ib_inventory.sku_id
						AND style.style_id = sku.style_id
						AND style.style_type = 2
					GROUP BY 
						sku.sku_id
				) IB
			ON
				IB_TOTAL.sku_id = IB.sku_id
			GROUP BY
				IB_TOTAL.sku_id

		END

	ELSE
		
		BEGIN

			INSERT INTO 
				#PI_SKU_OH_TEMP
			SELECT
				IB_TOTAL.sku_id,
				SUM(cost) cost,
				SUM(cost_local) cost_local,
				SUM(total_retail) total_retail,
				SUM(total_valuation_retail) total_valuation_retail,
				ISNULL(SUM(units_counted), 0) units_counted,
				ISNULL(SUM(extended_units_counted), 0) extended_units_counted,
				ISNULL(SUM(IB_TOTAL.total_oh_book_units), 0) - ISNULL(SUM(IB.post_oh_book_units), 0) total_oh_book_units,
				ISNULL(SUM(IB_TOTAL.total_oh_book_cost), 0) - ISNULL(SUM(IB.post_oh_book_cost), 0) total_oh_book_cost,
				ISNULL(SUM(IB_TOTAL.total_oh_book_cost_local), 0) - ISNULL(SUM(IB.post_oh_book_cost_local), 0) total_oh_book_cost_local,
				ISNULL(SUM(IB_TOTAL.total_oh_book_val_retail), 0) - ISNULL(SUM(IB.post_oh_book_val_retail), 0) total_oh_book_val_retail,
				ISNULL(SUM(IB_TOTAL.total_oh_book_sell_retail), 0) - ISNULL(SUM(IB.post_oh_book_sell_retail), 0) total_oh_book_sell_retail,
				ISNULL(SUM(IB_TOTAL.total_oh_in_transit_units), 0) - ISNULL(SUM(IB.post_oh_in_transit_units), 0) total_oh_in_transit_units,
				ISNULL(SUM(IB_TOTAL.total_oh_in_transit_cost), 0) - ISNULL(SUM(IB.post_oh_in_transit_cost), 0) total_oh_in_transit_cost,
				ISNULL(SUM(IB_TOTAL.total_oh_in_transit_cost_local), 0) - ISNULL(SUM(IB.post_oh_in_transit_cost_local), 0) total_oh_in_transit_cost_local,
				ISNULL(SUM(IB_TOTAL.total_oh_in_tran_val_retail), 0) - ISNULL(SUM(IB.post_oh_in_tran_val_retail), 0) total_oh_in_tran_val_retail,
				ISNULL(SUM(IB_TOTAL.total_oh_in_tran_sell_retail), 0) - ISNULL(SUM(IB.post_oh_in_tran_sell_retail), 0) total_oh_in_tran_sell_retail
			FROM
				(
					SELECT
						sku.sku_id,
						0 units_counted,
						0 extended_units_counted,
						0 cost,
						0 cost_local,
						0 total_retail,
						0 total_valuation_retail,
						SUM(total_on_hand_units) total_oh_book_units,
						SUM(total_on_hand_cost) total_oh_book_cost,
						SUM(total_on_hand_cost_local) total_oh_book_cost_local,
						SUM(total_on_hand_valuation_retail) total_oh_book_val_retail,
						SUM(total_on_hand_selling_retail) total_oh_book_sell_retail,
						0 total_oh_in_transit_units,
						0 total_oh_in_transit_cost,
						0 total_oh_in_transit_cost_local,
						0 total_oh_in_tran_val_retail,
						0 total_oh_in_tran_sell_retail
					FROM
						ib_inventory_total,
						sku,
						style
					WHERE
						location_id = @LocId
						AND inventory_status_id <> 2
						AND sku.sku_id = ib_inventory_total.sku_id
						AND style.style_id = sku.style_id
						AND style.style_type = 2
					GROUP BY 
						sku.sku_id
					UNION ALL
					SELECT
						sku.sku_id,
						0 units_counted,
						0 extended_units_counted,
						0 cost,
						0 cost_local,
						0 total_retail,
						0 total_valuation_retail,
						0 total_oh_book_units,
						0 total_oh_book_cost,
						0 total_oh_book_cost_local,
						0 total_oh_book_val_retail,
						0 total_oh_book_sell_retail,
						SUM(total_on_hand_units) total_oh_in_transit_units,
						SUM(total_on_hand_cost) total_oh_in_transit_cost,
						SUM(total_on_hand_cost_local) total_oh_in_transit_cost_local,
						SUM(total_on_hand_valuation_retail) total_oh_in_tran_val_retail,
						SUM(total_on_hand_selling_retail) total_oh_in_tran_sell_retail
					FROM
						ib_inventory_total,
						sku,
						style
					WHERE
						location_id = @LocId
						AND inventory_status_id = 2
						AND sku.sku_id = ib_inventory_total.sku_id
						AND style.style_id = sku.style_id
						AND style.style_type = 2
					GROUP BY 
						sku.sku_id
					UNION ALL
					SELECT
						sku.sku_id,
						SUM(count_import_sku_temp.units_counted) units_counted,
						SUM(count_import_sku_temp.units_counted) extended_units_counted,
						SUM(count_import_sku_temp.cost) cost,
						SUM(count_import_sku_temp.cost_local) cost_local,
						SUM(count_import_sku_temp.total_retail) total_retail,
						SUM(count_import_sku_temp.total_valuation_retail) total_valuation_retail,
						0 total_oh_book_units,
						0 total_oh_book_cost,
						0 total_oh_book_cost_local,
						0 total_oh_book_val_retail,
						0 total_oh_book_sell_retail,
						0 total_oh_in_transit_units,
						0 total_oh_in_transit_cost,
						0 total_oh_in_transit_cost_local,
						0 total_oh_in_tran_val_retail,
						0 total_oh_in_tran_sell_retail
					FROM
						count_import_sku_temp,
						sku,
						style
					WHERE
						count_import_sku_temp.location_id = @LocId
						AND count_import_sku_temp.sku_id = sku.sku_id
						AND style.style_id = sku.style_id
						AND style.style_type = 2
					GROUP BY
						sku.sku_id
				) IB_TOTAL
			LEFT OUTER JOIN
				(
					SELECT
						sku.sku_id,
						SUM(transaction_units) post_oh_book_units,
						SUM(transaction_cost) post_oh_book_cost,
						SUM(transaction_cost_local) post_oh_book_cost_local,
						SUM(transaction_valuation_retail) post_oh_book_val_retail,
						SUM(transaction_selling_retail) post_oh_book_sell_retail,
						0 post_oh_in_transit_units,
						0 post_oh_in_transit_cost,
						0 post_oh_in_transit_cost_local,
						0 post_oh_in_tran_val_retail,
						0 post_oh_in_tran_sell_retail
					FROM
						ib_inventory,
						sku,
						style
					WHERE
						location_id = @LocId
						AND inventory_status_id <> 2
						AND transaction_date > CONVERT (DATETIME, @DocDate, 101)
						AND sku.sku_id = ib_inventory.sku_id
						AND style.style_id = sku.style_id
						AND style.style_type = 2
					GROUP BY 
						sku.sku_id
					UNION ALL
					SELECT
						sku.sku_id,
						0 post_oh_book_units,
						0 post_oh_book_cost,
						0 post_oh_book_cost_local,
						0 post_oh_book_val_retail,
						0 post_oh_book_sell_retail,
						SUM(transaction_units) post_oh_in_transit_units,
						SUM(transaction_cost) post_oh_in_transit_cost,
						SUM(transaction_cost_local) post_oh_in_transit_cost_local,
						SUM(transaction_valuation_retail) post_oh_in_tran_val_retail,
						SUM(transaction_selling_retail) post_oh_in_tran_sell_retail
					FROM
						ib_inventory,
						sku,
						style
					WHERE
						location_id = @LocId
						AND inventory_status_id = 2
						AND transaction_date > CONVERT (DATETIME, @DocDate, 101)
						AND sku.sku_id = ib_inventory.sku_id
						AND style.style_id = sku.style_id
						AND style.style_type = 2
					GROUP BY 
						sku.sku_id
				) IB
			ON
				IB_TOTAL.sku_id = IB.sku_id
			GROUP BY
				IB_TOTAL.sku_id

		END	
		
	
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
		inventory_count_detail (inventory_count_detail_id, inventory_control_loc_id, inventory_control_id, sku_id, units_counted, extended_units_counted, cost, cost_local, total_retail, total_valuation_retail)
	SELECT
		(@IclId * 1000000) + @LastItemId + sku_loc_id,
		@IclId,
		@DocId,
		sku_id,
		0 units_counted,
		0 extended_units_counted,
		0.00 cost,
		0.00 cost_local,
		0.00 total_retail,
		0.00 total_valuation_retail
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
-- Retrieve the total on hand book and in-transit values for pseudo-style skus

	IF @ReplaceOrInc = 0

		BEGIN

			UPDATE
				inventory_count_detail
			SET 
				inventory_count_detail.extended_units_counted = inventory_count_detail.units_counted,
				inventory_count_detail.total_cost = inventory_count_detail.cost,
				inventory_count_detail.total_cost_local = inventory_count_detail.cost_local,
				inventory_count_detail.total_oh_book_units = #PI_SKU_OH_TEMP.total_oh_book_units,
				inventory_count_detail.total_oh_book_cost = #PI_SKU_OH_TEMP.total_oh_book_cost,
				inventory_count_detail.total_oh_book_cost_local = #PI_SKU_OH_TEMP.total_oh_book_cost_local,
				inventory_count_detail.total_oh_book_val_retail = #PI_SKU_OH_TEMP.total_oh_book_val_retail,
				inventory_count_detail.total_oh_book_sell_retail = #PI_SKU_OH_TEMP.total_oh_book_sell_retail,
				inventory_count_detail.total_oh_in_transit_units = #PI_SKU_OH_TEMP.total_oh_in_transit_units,
				inventory_count_detail.total_oh_in_transit_cost = #PI_SKU_OH_TEMP.total_oh_in_transit_cost,
				inventory_count_detail.total_oh_in_transit_cost_local = #PI_SKU_OH_TEMP.total_oh_in_transit_cost_local,
				inventory_count_detail.total_oh_in_tran_val_retail = #PI_SKU_OH_TEMP.total_oh_in_tran_val_retail,
				inventory_count_detail.total_oh_in_tran_sell_retail = #PI_SKU_OH_TEMP.total_oh_in_tran_sell_retail
			FROM
				inventory_count_detail WITH (NOLOCK),
				#PI_SKU_OH_TEMP
			WHERE
				inventory_count_detail.sku_id = #PI_SKU_OH_TEMP.sku_id		
				AND inventory_count_detail.inventory_control_id = @DocId
				AND inventory_count_detail.inventory_control_loc_id = @IclId
				AND inventory_count_detail.pack_id IS NULL
				AND inventory_count_detail.total_retail IS NOT NULL

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
				inventory_count_detail.total_valuation_retail = #PI_SKU_OH_TEMP.total_valuation_retail,
				inventory_count_detail.total_oh_book_units = #PI_SKU_OH_TEMP.total_oh_book_units,
				inventory_count_detail.total_oh_book_cost = #PI_SKU_OH_TEMP.total_oh_book_cost,
				inventory_count_detail.total_oh_book_cost_local = #PI_SKU_OH_TEMP.total_oh_book_cost_local,
				inventory_count_detail.total_oh_book_val_retail = #PI_SKU_OH_TEMP.total_oh_book_val_retail,
				inventory_count_detail.total_oh_book_sell_retail = #PI_SKU_OH_TEMP.total_oh_book_sell_retail,
				inventory_count_detail.total_oh_in_transit_units = #PI_SKU_OH_TEMP.total_oh_in_transit_units,
				inventory_count_detail.total_oh_in_transit_cost = #PI_SKU_OH_TEMP.total_oh_in_transit_cost,
				inventory_count_detail.total_oh_in_transit_cost_local = #PI_SKU_OH_TEMP.total_oh_in_transit_cost_local,
				inventory_count_detail.total_oh_in_tran_val_retail = #PI_SKU_OH_TEMP.total_oh_in_tran_val_retail,
				inventory_count_detail.total_oh_in_tran_sell_retail = #PI_SKU_OH_TEMP.total_oh_in_tran_sell_retail
			FROM
				inventory_count_detail WITH (NOLOCK),
				#PI_SKU_OH_TEMP
			WHERE
				inventory_count_detail.sku_id = #PI_SKU_OH_TEMP.sku_id		
				AND inventory_count_detail.inventory_control_id = @DocId
				AND inventory_count_detail.inventory_control_loc_id = @IclId
				AND inventory_count_detail.pack_id IS NULL
				AND inventory_count_detail.total_retail IS NOT NULL

		END

	ELSE IF @ReplaceOrInc = 2 -- increment count
	
		BEGIN

			UPDATE
				inventory_count_detail
			SET 
				inventory_count_detail.units_counted = inventory_count_detail.units_counted + #PI_SKU_OH_TEMP.units_counted,
				inventory_count_detail.extended_units_counted = inventory_count_detail.extended_units_counted + #PI_SKU_OH_TEMP.extended_units_counted,
				inventory_count_detail.cost = inventory_count_detail.cost + #PI_SKU_OH_TEMP.cost,
				inventory_count_detail.cost_local = inventory_count_detail.cost_local + #PI_SKU_OH_TEMP.cost_local,
				inventory_count_detail.total_cost = inventory_count_detail.cost + #PI_SKU_OH_TEMP.cost,
				inventory_count_detail.total_cost_local = inventory_count_detail.cost_local + #PI_SKU_OH_TEMP.cost_local,
				inventory_count_detail.total_retail = inventory_count_detail.total_retail + #PI_SKU_OH_TEMP.total_retail,
				inventory_count_detail.total_valuation_retail = inventory_count_detail.total_valuation_retail + #PI_SKU_OH_TEMP.total_valuation_retail,
				inventory_count_detail.total_oh_book_units = #PI_SKU_OH_TEMP.total_oh_book_units,
				inventory_count_detail.total_oh_book_cost = #PI_SKU_OH_TEMP.total_oh_book_cost,
				inventory_count_detail.total_oh_book_cost_local = #PI_SKU_OH_TEMP.total_oh_book_cost_local,
				inventory_count_detail.total_oh_book_val_retail = #PI_SKU_OH_TEMP.total_oh_book_val_retail,
				inventory_count_detail.total_oh_book_sell_retail = #PI_SKU_OH_TEMP.total_oh_book_sell_retail,
				inventory_count_detail.total_oh_in_transit_units = #PI_SKU_OH_TEMP.total_oh_in_transit_units,
				inventory_count_detail.total_oh_in_transit_cost = #PI_SKU_OH_TEMP.total_oh_in_transit_cost,
				inventory_count_detail.total_oh_in_transit_cost_local = #PI_SKU_OH_TEMP.total_oh_in_transit_cost_local,
				inventory_count_detail.total_oh_in_tran_val_retail = #PI_SKU_OH_TEMP.total_oh_in_tran_val_retail,
				inventory_count_detail.total_oh_in_tran_sell_retail = #PI_SKU_OH_TEMP.total_oh_in_tran_sell_retail
			FROM
				inventory_count_detail WITH (NOLOCK),
				#PI_SKU_OH_TEMP
			WHERE
				inventory_count_detail.sku_id = #PI_SKU_OH_TEMP.sku_id		
				AND inventory_count_detail.inventory_control_id = @DocId
				AND inventory_count_detail.inventory_control_loc_id = @IclId
				AND inventory_count_detail.pack_id IS NULL
				AND inventory_count_detail.total_retail IS NOT NULL

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

-- For those pseudo-styles that don't have a cost, calculate cost based on total_oh_book_cost
	UPDATE
		inventory_count_detail
	SET
		cost = (total_oh_book_cost / total_oh_book_val_retail) / (total_retail * @ExchangeRate1),
		total_cost = (total_oh_book_cost / total_oh_book_val_retail) / (total_retail * @ExchangeRate1)
	WHERE
		inventory_count_detail.total_retail IS NOT NULL
		AND inventory_count_detail.cost IS NULL
		AND inventory_count_detail.inventory_control_id = @DocId
		AND inventory_count_detail.inventory_control_loc_id = @IclId
		AND inventory_count_detail.pack_id IS NULL

	UPDATE
		inventory_count_detail
	SET
		cost_local = (total_oh_book_cost_local / total_oh_book_sell_retail) / (total_retail / @ExchangeRate1),
		total_cost_local = (total_oh_book_cost_local / total_oh_book_sell_retail) / (total_retail / @ExchangeRate1)
	WHERE
		inventory_count_detail.total_retail IS NOT NULL
		AND inventory_count_detail.cost_local IS NULL
		AND inventory_count_detail.inventory_control_id = @DocId
		AND inventory_count_detail.inventory_control_loc_id = @IclId
		AND inventory_count_detail.pack_id IS NULL
		AND inventory_count_detail.total_oh_book_sell_retail IS NOT NULL
		AND inventory_count_detail.total_retail <> 0

/*--------------------------------------------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------*/

	DROP TABLE #sku_loc
	DROP TABLE #PI_SKU_OH_TEMP
		
/*--------------------------------------------------------------------------------------------------------------*/

END
```

