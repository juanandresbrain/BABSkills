# dbo.pi_populate_work_details_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.pi_populate_work_details_$sp"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
CREATE proc [dbo].[pi_populate_work_details_$sp]

  ( @IclId AS DECIMAL(13,0)
  , @DocId AS DECIMAL(12,0)
  , @LocId AS SMALLINT
  , @LastIbInventoryId AS DECIMAL(13,0)
  , @LastIbPackInventoryId AS DECIMAL(13,0) )

AS

/*
Proc name: pi_populate_work_details_$sp

Description:

For the given inventory control document and location, populate the pi_work_detail and pi_pack_work_detail with the data that will eventually be inserted
into inventory_count_detail and populate pi_work_loc_info with data that will eventually be updating inventory_control_loc

HISTORY:
Date       		Name         		Def#			Desc
November 22,2006   	Jacqueline Lin		80360			Ported over 3.0 def. 63923 - merch:im:physical inventory performance changes.
Jan. 29, 2010		Feng			multi-currency mod VS0458.UC157-158, add local cost for every cost items:
                            total_oh_book_cost_local
                            total_oh_in_transit_cost_local
                            discrepancy_cost_local
                            pending_shrink_cost_local
                            average_cost_local
April 26, 2010		Feng			increase precision from 2 to 6 for cost fields
*/

BEGIN

  EXEC dbo.sp_executesql
    N'INSERT INTO
      pi_work_detail
        ( inventory_control_loc_id
        , inventory_control_id
        , sku_id
        , units_counted
        , extended_units_counted
        , total_oh_book_units
        , total_oh_book_cost
        , total_oh_book_cost_local
        , total_oh_book_val_retail
        , total_oh_book_sell_retail
        , total_oh_in_transit_units
        , total_oh_in_transit_cost
        , total_oh_in_transit_cost_local
        , total_oh_in_tran_val_retail
        , total_oh_in_tran_sell_retail
        , discrepancy_units
        , discrepancy_cost
        , discrepancy_cost_local
        , discrepancy_val_retail
        , discrepancy_sell_retail
        , pending_shrink_units
        , pending_shrink_cost
        , pending_shrink_cost_local
        , pending_shrink_val_retail
        , pending_shrink_sell_retail
        , average_cost
        , average_cost_local
        , valuation_unit_retail
        , selling_unit_retail
        , price_status_id )
    SELECT
      @ParamIclId inventory_control_loc_id
      , @ParamDocId inventory_control_id
      , SKU.sku_id
      , 0 units_counted
      , 0 extended_units_counted
      , total_oh_book_units
      , total_oh_book_cost
      , total_oh_book_cost_local
      , total_oh_book_val_retail
      , total_oh_book_sell_retail
      , total_oh_in_transit_units
      , total_in_transit_cost
      , total_in_transit_cost_local
      , total_in_tran_val_retail
      , total_in_tran_sell_retail
      , discrepancy_units
      , discrepancy_cost
      , discrepancy_cost_local
      , discrepancy_val_retail
      , discrepancy_sell_retail
      , pending_shrink_units
      , pending_shrink_cost
      , pending_shrink_cost_local
      , pending_shrink_val_retail
      , pending_shrink_sell_retail
      , average_cost
      , average_cost_local
      , valuation_unit_retail
      , selling_unit_retail
      , price_status_id
    FROM
      ( SELECT
        sku_id
        , @ParamLocId location_id
        , valuation_unit_retail
        , selling_unit_retail
        , price_status_id
        FROM
            #tt_frozen_retails ) SKU
      JOIN
        (
          SELECT
            sku_id
            , location_id
            , average_cost
            , average_cost_local
            , SUM(total_oh_book_units) total_oh_book_units
            , SUM(total_oh_book_cost) total_oh_book_cost
            , SUM(total_oh_book_cost_local) total_oh_book_cost_local
            , SUM(total_oh_book_val_retail) total_oh_book_val_retail
            , SUM(total_oh_book_sell_retail) total_oh_book_sell_retail
            , SUM(total_oh_in_transit_units) total_oh_in_transit_units
 , SUM(total_oh_in_transit_cost) total_in_transit_cost
            , SUM(total_oh_in_transit_cost_local) total_in_transit_cost_local
            , SUM(total_oh_in_tran_val_retail) total_in_tran_val_retail
            , SUM(total_oh_in_tran_sell_retail) total_in_tran_sell_retail
            , SUM(discrepancy_units) discrepancy_units
            , SUM(discrepancy_cost) discrepancy_cost
            , SUM(discrepancy_cost_local) discrepancy_cost_local
            , SUM(discrepancy_val_retail) discrepancy_val_retail
            , SUM(discrepancy_sell_retail) discrepancy_sell_retail
            , SUM(pending_shrink_units) pending_shrink_units
            , SUM(pending_shrink_cost) pending_shrink_cost
            , SUM(pending_shrink_cost_local) pending_shrink_cost_local
            , SUM(pending_shrink_val_retail) pending_shrink_val_retail
            , SUM(pending_shrink_sell_retail) pending_shrink_sell_retail
          FROM
            (
              SELECT
                sku_id
                , location_id
                , average_cost
                , average_cost_local
                , COALESCE(SUM(on_hand_units), 0) total_oh_book_units
                , COALESCE(SUM(on_hand_cost), 0.000000) total_oh_book_cost
                , COALESCE(SUM(on_hand_cost_local), 0.000000) total_oh_book_cost_local
                , COALESCE(SUM(on_hand_valuation_retail), 0) total_oh_book_val_retail
                , COALESCE(SUM(on_hand_selling_retail), 0) total_oh_book_sell_retail
                , 0 total_oh_in_transit_units
                , 0.000000 total_oh_in_transit_cost
                , 0.000000 total_oh_in_transit_cost_local
                , 0.00 total_oh_in_tran_val_retail
                , 0.00 total_oh_in_tran_sell_retail
                , 0 discrepancy_units
                , 0.000000 discrepancy_cost
                , 0.000000 discrepancy_cost_local
                , 0.00 discrepancy_val_retail
                , 0.00 discrepancy_sell_retail
                , 0 pending_shrink_units
                , 0.000000 pending_shrink_cost
                , 0.000000 pending_shrink_cost_local
                , 0.00 pending_shrink_val_retail
                , 0.00 pending_shrink_sell_retail
              FROM
                #tt_frozen_on_hand toh
              INNER JOIN inventory_status i ON i.inventory_status_id = toh.inventory_status_id
              WHERE
                inventory_status_code NOT IN (''002'', ''013'')
                AND location_id = @ParamLocId
              GROUP BY
                sku_id
                , location_id
                , average_cost
                , average_cost_local
              UNION ALL
              SELECT
                sku_id
                , location_id
                , average_cost
                , average_cost_local
                , 0 total_oh_book_units
                , 0.000000 total_oh_book_cost
                , 0.000000 total_oh_book_cost_local
                , 0.00 total_oh_book_val_retail
                , 0.00 total_oh_book_sell_retail
                , on_hand_units total_oh_in_transit_units
                , on_hand_cost total_oh_in_transit_cost
                , on_hand_cost_local total_oh_in_transit_cost_local
                , on_hand_valuation_retail total_oh_in_tran_val_retail
                , on_hand_selling_retail total_oh_in_tran_sell_retail
                , 0 discrepancy_units
                , 0.000000 discrepancy_cost
                , 0.000000 discrepancy_cost_local
                , 0.00 discrepancy_val_retail
                , 0.00 discrepancy_sell_retail
                , 0 pending_shrink_units
                , 0.000000 pending_shrink_cost
                , 0.000000 pending_shrink_cost_local
                , 0.00 pending_shrink_val_retail
                , 0.00 pending_shrink_sell_retail
              FROM
                #tt_frozen_on_hand toh
              INNER JOIN inventory_status i ON i.inventory_status_id = toh.inventory_status_id
              WHERE
                inventory_status_code IN (''002'', ''013'')
                AND location_id = @ParamLocId
              UNION ALL
              SELECT
                sku_id
                , location_id
                , average_cost
                , average_cost_local
                , 0 total_oh_book_units
                , 0.000000 total_oh_book_cost
                , 0.000000 total_oh_book_cost_local
                , 0.00 total_oh_book_val_retail
                , 0.00 total_oh_book_sell_retail
                , 0 total_oh_in_transit_units
                , 0.000000 total_oh_in_transit_cost
                , 0.000000 total_oh_in_transit_cost_local
                , 0.00 total_oh_in_tran_val_retail
                , 0.00  total_oh_in_tran_sell_retail
                , on_hand_units discrepancy_units
                , on_hand_cost discrepancy_cost
                , on_hand_cost_local discrepancy_cost_local
                , on_hand_valuation_retail discrepancy_val_retail
                , on_hand_selling_retail discrepancy_sell_retail
                , 0 pending_shrink_units
                , 0.000000 pending_shrink_cost
                , 0.000000 pending_shrink_cost_local
                , 0.00 pending_shrink_val_retail
                , 0.00 pending_shrink_sell_retail
              FROM
                #tt_frozen_on_hand
              WHERE
                inventory_status_id = 4
                AND location_id = @ParamLocId
              UNION ALL
              SELECT
                sku_id
                , location_id
                , average_cost
                , average_cost_local
                , 0 total_oh_book_units
                , 0.000000 total_oh_book_cost
                , 0.000000 total_oh_book_cost_local
                , 0.00 total_oh_book_val_retail
                , 0.00 total_oh_book_sell_retail
                , 0 total_oh_in_transit_units
                , 0.000000 total_oh_in_transit_cost
                , 0.000000 total_oh_in_transit_cost_local
                , 0.00 total_oh_in_tran_val_retail
                , 0.00 total_oh_in_tran_sell_retail
                , 0 discrepancy_units
                , 0.000000 discrepancy_cost
                , 0.000000 discrepancy_cost_local
                , 0.00 discrepancy_val_retail
                , 0.00 discrepancy_sell_retail
                , on_hand_units pending_shrink_units
                , on_hand_cost pending_shrink_cost
                , on_hand_cost_local pending_shrink_cost_local
                , on_hand_valuation_retail pending_shrink_val_retail
                , on_hand_selling_retail pending_shrink_sell_retail
              FROM
                #tt_frozen_on_hand
              WHERE
                inventory_status_id = 7
                AND location_id = @ParamLocId
            ) T
          GROUP BY
            sku_id
            , location_id
            , average_cost
            , average_cost_local
        ) ON_HAND ON ( ON_HAND.location_id = SKU.location_id
            AND ON_HAND.sku_id = SKU.sku_id )'
    , N'@ParamLocId AS SMALLINT
      , @ParamIclId AS DECIMAL(13,0)
      , @ParamDocId AS DECIMAL(12,0)'
    , @ParamLocId = @LocId
    , @ParamIclId = @IclId
    , @ParamDocId =  @DocId

  EXEC dbo.sp_executesql
    N'INSERT INTO
      pi_pack_work_detail
        ( inventory_control_loc_id
        , inventory_control_id
        , pack_id
        , units_counted
        , book_pack_units )
    SELECT
      @ParamIclId inventory_control_loc_id
      , @ParamDocId inventory_control_id
      , pack_id
      , 0 units_counted
      , on_hand_units
    FROM
      #tt_pack_frozen_on_hand
    WHERE
      location_id = @ParamLocId'
    , N'@ParamLocId AS SMALLINT
      , @ParamIclId AS DECIMAL(13,0)
      , @ParamDocId AS DECIMAL(12,0)'
    , @ParamLocId = @LocId
    , @ParamIclId = @IclId
    , @ParamDocId =  @DocId

  EXEC dbo.sp_executesql
    N'UPDATE
      pi_work_detail
      SET
      total_retail = 0.00
      , units_counted = 0
      , extended_units_counted = 0
      FROM
      pi_work_detail
      , sku
      , style
      WHERE
      pi_work_detail.inventory_control_loc_id = @ParamIclId
      AND pi_work_detail.inventory_control_id = @ParamDocId
      AND pi_work_detail.sku_id = sku.sku_id
      AND sku.style_id = style.style_id
      AND style.style_type = 2'
    , N'@ParamIclId AS DECIMAL(13,0)
      , @ParamDocId AS DECIMAL(12,0)'
    , @ParamIclId = @IclId
    , @ParamDocId =  @DocId

  EXEC dbo.sp_executesql
    N'INSERT INTO
      pi_work_loc_info
        ( inventory_control_loc_id
        , inventory_control_id
        , last_ib_inventory_id
        , last_ib_pack_inventory_id
        , detail_count )
      SELECT
      @ParamIclId inventory_control_loc_id
      , @ParamDocId inventory_control_id
      , @ParamLastIbInventoryId last_ib_inventory_id
      , @ParamLastIbPackInventoryId last_ib_pack_inventory_id
      , SUM(detail_count) detail_count
      FROM
      ( SELECT
        COUNT(*) detail_count
        FROM
        pi_work_detail
        WHERE
        inventory_control_loc_id = @ParamIclId
        AND inventory_control_id = @ParamDocId
        UNION ALL
        SELECT
        COUNT(*) detail_count
        FROM
        pi_pack_work_detail
        WHERE
        inventory_control_loc_id = @ParamIclId
        AND inventory_control_id = @ParamDocId ) A'
    , N'@ParamIclId AS DECIMAL(13,0)
      , @ParamDocId AS DECIMAL(12,0)
      , @ParamLastIbInventoryId AS DECIMAL(13,0)
      , @ParamLastIbPackInventoryId AS DECIMAL(13,0)'
    , @ParamIclId = @IclId
    , @ParamDocId =  @DocId
    , @ParamLastIbInventoryId = @LastIbInventoryId
    , @ParamLastIbPackInventoryId =  @LastIbPackInventoryId

END
```

