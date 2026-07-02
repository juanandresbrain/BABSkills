# dbo.pi_pack_freeze_on_hand_loc_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.pi_pack_freeze_on_hand_loc_$sp"]
    dbo_ib_pack_inventory_total(["dbo.ib_pack_inventory_total"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ib_pack_inventory_total |

## Stored Procedure Code

```sql
create proc dbo.pi_pack_freeze_on_hand_loc_$sp 	( @LocId SMALLINT
	, @MaxId DECIMAL(13,0) OUTPUT )
WITH RECOMPILE
AS

-- R3 version
/*
Proc name: pi_pack_freeze_on_hand_loc_$sp

Description: 

For the given location on the inventory control document, a snapshot of the ib_pack_inventory_total table is taken.
The snapshot is valid only if the maximum ib_pack_inventory_id remains the before and after the snapshot.
Once a valid snaphot has been taken, the procedure returns the maximum ib_pack_inventory_id which is stored later in the inventory_control_loc table.

HISTORY:
Date       		Name         		Def#			Desc
November 22,2006   	Jacqueline Lin		80360			Ported over 3.0 def. 63923 - merch:im:physical inventory performance changes.
November 24,2006	Jacqueline Lin		80360			Ported over 3.0 def. 64632 - merch:im:book units for packs not retrieved properly for inventory counts
December 15, 2010	Ivan Dimitrov		123081		inventory count loading running to a long time
*/

BEGIN

	DECLARE @PreMaxId AS DECIMAL(13,0)
	DECLARE @PostMaxId AS DECIMAL(13,0)
	
	DECLARE @Flag AS BIT

	SET @PreMaxId = 0
	SET @PostMaxId = 0
	SET @Flag = 0

	EXEC dbo.sp_executesql
		N'TRUNCATE TABLE #tt_pack_frozen_on_hand'

	WHILE (@Flag <> 1)

		BEGIN

			-- Store the maximum ib_pack_inventory_id prior to taking the snapshot
			EXEC dbo.sp_executesql
				N'SELECT @ParamPreMaxId = COALESCE(MAX(ib_pack_inventory_id), 0) FROM ib_pack_inventory'
				, N'@ParamPreMaxId AS DECIMAL(13,0) OUTPUT'
				, @ParamPreMaxId = @PreMaxId OUTPUT
				
			-- Take snapshot and store values in #tt_pack_frozen_on_hand table.
			-- The ib_pack_inventory_total table is joined to the #tt_pack table to ensure we are only freezing values for valid packs
			INSERT INTO
				#tt_pack_frozen_on_hand
					( pack_id
					, location_id
					, on_hand_units )
			  SELECT
				#tt_pack.pack_id
				, location_id
				, total_on_hand_units on_hand_units
			  FROM
				ib_pack_inventory_total
				, #tt_pack
			  WHERE
				ib_pack_inventory_total.pack_id = #tt_pack.pack_id
				AND location_id = @LocId
			  ORDER BY
				#tt_pack.pack_id
				, location_id
			OPTION(RECOMPILE)
				
	
			-- Store the maximum ib_pack_inventory_id after taking the snapshot			
			EXEC dbo.sp_executesql
				N'SELECT @ParamPostMaxId = COALESCE(MAX(ib_pack_inventory_id), 0) FROM ib_pack_inventory'
				, N'@ParamPostMaxId AS DECIMAL(13,0) OUTPUT'
				, @ParamPostMaxId = @PostMaxId OUTPUT
	
			-- If the maximum ib_pack_inventory_id is the same before and after the snapshot, then the snapshot is accurate		
			IF (@PreMaxId = @PostMaxId) 
				SET @Flag = 1
			-- If the maximum ib_pack_inventory_id is not the same before and after the snapshot, then the snapshot is invalid
			-- and the #tt_pack_frozen_on_hand table is truncated			
			ELSE
				EXEC dbo.sp_executesql
					N'TRUNCATE TABLE #tt_pack_frozen_on_hand'


		END

	SET @MaxId = @PostMaxId

END
```

