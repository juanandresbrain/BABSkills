# dbo.pi_pack_rmv_future_oh_loc_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.pi_pack_rmv_future_oh_loc_$sp"]
    dbo_ib_pack_inventory(["dbo.ib_pack_inventory"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ib_pack_inventory |

## Stored Procedure Code

```sql
create proc dbo.pi_pack_rmv_future_oh_loc_$sp 







	( @CountDate DATETIME
	, @LocId SMALLINT
	, @MaxId DECIMAL(13,0) )
WITH RECOMPILE
AS

-- R3 version
/*
Proc name: pi_pack_rmv_future_oh_loc_$sp

Description: 

For the given location on the inventory control document, a snapshot of the ib_pack_inventory_total table has been taken.
From this snapshot, remove any on hand with a transaction date greater than the count date on the inventory control document.
When querying ib_pack_inventory, the ib_pack_inventory_id must be less than or eqaul to the maximum ib_pack_inventory_id passed in;
this was the id stored upon taking the valid snapshot.

HISTORY:
Date       		Name         		Def#			Desc
November 22,2006   	Jacqueline Lin		80360			Ported over 3.0 def. 63923 - merch:im:physical inventory performance changes.  
December 15, 2010	Ivan Dimitrov		123081			inventory count loading running for to a long time	
*/

BEGIN

	EXEC dbo.sp_executesql 
		N'TRUNCATE TABLE #tt_pack_future_on_hand'

	-- Retrieve any on hand from ib_pack_inventory with a transaction date greater than the count date
	-- The ib_pack_inventory_id should be less than or equal to the maximum ib_pack_inventory_id passed in
		INSERT INTO
		#tt_pack_future_on_hand
			( pack_id
			, location_id
			, on_hand_units )
	  SELECT
		#tt_pack_frozen_on_hand.pack_id
		, #tt_pack_frozen_on_hand.location_id
		, COALESCE(SUM(transaction_units), 0) on_hand_units
	  FROM
		ib_pack_inventory
		, #tt_pack_frozen_on_hand
	  WHERE
		transaction_date > @CountDate
		AND ib_pack_inventory.location_id = @LocId
		AND ib_pack_inventory_id <= @MaxId
		AND #tt_pack_frozen_on_hand.pack_id = ib_pack_inventory.pack_id
		AND #tt_pack_frozen_on_hand.location_id = ib_pack_inventory.location_id
	  GROUP BY
		#tt_pack_frozen_on_hand.pack_id
		, #tt_pack_frozen_on_hand.location_id
	  OPTION(RECOMPILE)
	
	-- Update the #tt_pack_frozen_on_hand table by removing future on hand
	UPDATE
		#tt_pack_frozen_on_hand
	  SET
		#tt_pack_frozen_on_hand.on_hand_units = #tt_pack_frozen_on_hand.on_hand_units - #tt_pack_future_on_hand.on_hand_units
	  FROM
		#tt_pack_frozen_on_hand
		, #tt_pack_future_on_hand
	  WHERE
		#tt_pack_frozen_on_hand.pack_id = #tt_pack_future_on_hand.pack_id
		AND #tt_pack_frozen_on_hand.location_id = #tt_pack_future_on_hand.location_id
	OPTION(RECOMPILE)
	
END
```

