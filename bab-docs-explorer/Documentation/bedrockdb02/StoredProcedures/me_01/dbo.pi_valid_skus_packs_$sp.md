# dbo.pi_valid_skus_packs_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.pi_valid_skus_packs_$sp"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
CREATE PROC dbo.pi_valid_skus_packs_$sp ( @DocId DECIMAL(12,0)
	, @HierarchyLevelId DECIMAL(13,0)
	, @ParentLevelId DECIMAL(13,0) )
AS

/*
Proc name: pi_valid_skus_packs_$sp

Description: 

For the given inventory control document, determine the skus and packs that are valid for this count
based on the hierarchy_level_id and parent_level_id passed in as parameters.

If the hierarchy_level_id is not zero and the parent_level_id is zero, then the count is being done at the chain-level;
therefore, all skus and packs are valid.

If the hierarchy_level_id is not zero and the parent_level_id is not zero, then the count is being done for one or more hierarchy groups;
therefore, all skus and packs that are descendants of these hierarchy groups are valid.

If both the hierarchy_level_id and parent_level_id are zero, then the count is being done for one or more styles;
therefore, all skus and packs that are descendants of these styles are valid.

HISTORY:
Date       		Name         		Def#			Desc
November 23,2006   	Jacqueline Lin		80360			Ported over 3.0 def. 63923 - merch:im:physical inventory performance changes.
									Ported over 3.0 def. 64101 - merch:im:error occurs importing count for document at style or group level
*/

BEGIN

	-- If the hierarchy_level_id is not null and the parent_level_id is null, then the count is being done at the chain-level;
	-- therefore, all skus and packs are valid.
	IF (COALESCE(@HierarchyLevelId, 0) <> 0 AND COALESCE(@ParentLevelId, 0) = 0) 
	
		BEGIN
			
			EXEC dbo.sp_executesql
				N'INSERT INTO 
					#tt_sku
				  SELECT
					sku_id
				  FROM
					sku
				  ORDER BY
					sku_id'
		
			EXEC dbo.sp_executesql
				N'INSERT INTO 
					#tt_pack
				  SELECT
					pack_id
				  FROM
					pack
				  ORDER BY
					pack_id'
		
		END;

	-- If the hierarchy_level_id is not null and the parent_level_id is not null, then the count is being done for one or more hierarchy groups;
	-- therefore, all skus and packs that are descendants of these hierarchy groups are valid.		
	ELSE IF (COALESCE(@HierarchyLevelId, 0) <> 0 AND COALESCE(@ParentLevelId, 0) <> 0)  
	
		BEGIN

			EXEC dbo.sp_executesql
				N'INSERT INTO 
					#tt_sku
				  SELECT
					sku_id
				  FROM
					sku
					, style_group
					, merch_group_parent
					, inv_control_merch
				  WHERE
					sku.style_id = style_group.style_id
					AND style_group.hierarchy_group_id = merch_group_parent.hierarchy_group_id
					AND merch_group_parent.parent_hierarchy_group_id = inv_control_merch.hierarchy_group_id
					AND inv_control_merch.inventory_control_id = @ParamDocId
				  ORDER BY
					sku_id'
				, N'@ParamDocId AS DECIMAL(12,0)'
				, @ParamDocId = @DocId
		
			EXEC dbo.sp_executesql
				N'INSERT INTO 
					#tt_pack
				  SELECT
					pack_id
				  FROM
					pack
					, style_group
					, merch_group_parent
					, inv_control_merch
				  WHERE
					pack.style_id = style_group.style_id
					AND style_group.hierarchy_group_id = merch_group_parent.hierarchy_group_id
					AND merch_group_parent.parent_hierarchy_group_id = inv_control_merch.hierarchy_group_id
					AND inv_control_merch.inventory_control_id = @ParamDocId
				  ORDER BY
					pack_id'
				, N'@ParamDocId AS DECIMAL(12,0)'
				, @ParamDocId = @DocId
				
		END;

	-- If both the hierarchy_level_id and parent_level_id are null, then the count is being done for one or more styles;
	-- therefore, all skus and packs that are descendants of these styles are valid.		
	ELSE IF (COALESCE(@HierarchyLevelId, 0) = 0 AND COALESCE(@ParentLevelId, 0) = 0) 
	
		BEGIN

			EXEC dbo.sp_executesql 
				N'INSERT INTO 
					#tt_sku
				  SELECT
					sku_id
				  FROM
					sku
					, inv_control_merch
				  WHERE
					sku.style_id = inv_control_merch.style_id
					AND inv_control_merch.inventory_control_id = @ParamDocId 
				  ORDER BY
					sku_id'
				, N'@ParamDocId AS DECIMAL(12,0)'
				, @ParamDocId = @DocId
		
			EXEC dbo.sp_executesql 
				N'INSERT INTO 
					#tt_pack
				  SELECT
					pack_id
				  FROM
					pack
					, inv_control_merch
				  WHERE
					pack.style_id = inv_control_merch.style_id
					AND inv_control_merch.inventory_control_id = @ParamDocId 
				  ORDER BY
					pack_id'
				, N'@ParamDocId AS DECIMAL(12,0)'
				, @ParamDocId = @DocId
		
		END

--- added by gd		
EXEC dbo.sp_executesql
		--		N'create index #tt_sku_idx on #tt_sku (sku_id)'
	N'ALTER TABLE 
                        #tt_sku
            ADD UNIQUE CLUSTERED
                        ( sku_id)'
	

--- added end


END
```

