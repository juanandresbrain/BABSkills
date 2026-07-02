# dbo.sp_DistroRowsReadyForSplitForAGivenStoreAndDate_rpt

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_DistroRowsReadyForSplitForAGivenStoreAndDate_rpt"]
    dbo_distribution_split_rpt(["dbo.distribution_split_rpt"]) --> SP
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> SP
    dbo_style(["dbo.style"]) --> SP
    dbo_style_group(["dbo.style_group"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.distribution_split_rpt |
| dbo.hierarchy_group |
| dbo.style |
| dbo.style_group |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[sp_DistroRowsReadyForSplitForAGivenStoreAndDate_rpt] 
	(@storeNum  int,
	 @warehouseNum int)
	
	
AS

	SET NOCOUNT ON 



-----------------------------------------------------------------------------------------------------------------------
--Old Logic
-----------------------------------------------------------------------------------------------------------------------

	--SELECT 
	--	distribution_split.Id
	--	, distribution_split.SourceID
	--	, distribution_split.DestID
	--	, distribution_split.style_code
	--	, distribution_split.quantity
	--	, distribution_split.rec_Type
	--	, distribution_split.sequencenbr
	--	, distribution_split.distribution_number
	--	, distribution_split.ref_field_1
	--	, distribution_split.release_date
	--	, distribution_split.active_pick_flag
	--	, SortType = CASE 
	--		WHEN distribution_split.active_pick_flag = 'Y' THEN 0
	--		WHEN distribution_split.rec_type = 11 THEN 1
	--		WHEN substring(hg.hierarchy_group_code,7,2)<>'60' THEN 2
	--		--WHEN isSupply = 0 then 2
	--		ELSE 3
 --       END
	--FROM 
	--	distribution_split (NOLOCK)
	--INNER JOIN
	--	style s (NOLOCK) ON distribution_split.style_code = s.style_code
	--JOIN 
	--	style_group sg (NOLOCK) ON s.style_id = sg.style_id
	--JOIN 
	--	hierarchy_group hg (NOLOCK) ON sg.hierarchy_group_id = hg.hierarchy_group_id		
	--WHERE 
	--	destid = @storeNum
	--AND 
	--	sourceid = @warehouseNum
	--AND 
	--	released = 0
	--ORDER BY 
	--	SortType
	--	, distribution_split.style_code DESC
	--	, distribution_split.release_date DESC

--------------------------------------------------------------------------------------------------------------------------
	
DECLARE @sumCartons AS INT

SELECT @sumCartons = SUM([quantity])
  FROM [me_01].[dbo].[distribution_split_rpt] ds
  INNER JOIN
		style s (NOLOCK) ON ds.style_code = s.style_code
	JOIN 
		style_group sg (NOLOCK) ON s.style_id = sg.style_id
	JOIN 
		hierarchy_group hg (NOLOCK) ON sg.hierarchy_group_id = hg.hierarchy_group_id
  WHERE destid = @storeNum
  AND sourceid = @warehouseNum
  AND released = 0 
  AND active_pick_flag = 'N' AND substring(hg.hierarchy_group_code,7,2)<>'60'

SELECT inner_table.Id
		, inner_table.SourceID
		, inner_table.DestID
		, inner_table.style_code
		, inner_table.quantity
		, inner_table.rec_Type
		, inner_table.sequencenbr
		, inner_table.distribution_number
		, inner_table.ref_field_1
		, inner_table.release_date
		, inner_table.active_pick_flag
		, SortType = CASE 
			WHEN active_pick_flag = 'Y' THEN 0
			WHEN rec_type = 11 THEN 1
			WHEN substring(inner_table.hierarchy_group_code,7,2)<>'60' THEN 2--AND percentOfShipment > 0.75 THEN 2
			--WHEN isSupply = 0 then 2
			--WHEN substring(inner_table.hierarchy_group_code,7,2)<>'60' AND percentOfShipment <= 0.75 THEN 3
			ELSE 3
        END
		,inner_table.percentOfShipment
FROM (SELECT 
		 distribution_split_rpt.[id]
		,distribution_split_rpt.[sourceid]
		,distribution_split_rpt.[destid]
		,distribution_split_rpt.[style_code]
		,distribution_split_rpt.[quantity]
		,distribution_split_rpt.[rec_type]
		,distribution_split_rpt.[sequencenbr]
		,distribution_split_rpt.[distribution_number]
		,distribution_split_rpt.[ref_field_1]
		,distribution_split_rpt.[release_date]
		,distribution_split_rpt.[active_pick_flag]
		,distribution_split_rpt.[released]
		,distribution_split_rpt.[exported_date]
		, percentOfShipment = CASE 
			WHEN distribution_split_rpt.active_pick_flag = 'Y' THEN 0
			WHEN substring(hg.hierarchy_group_code,7,2) = '60' THEN 0
			ELSE CAST((CAST([sumQuantity] AS DECIMAL(7,4))/@sumCartons)*100 AS DECIMAL(7,4))
		END
		,hg.hierarchy_group_code
	FROM 
		distribution_split_rpt (NOLOCK)
		INNER JOIN
		style s (NOLOCK) ON distribution_split_rpt.style_code = s.style_code
	JOIN 
		style_group sg (NOLOCK) ON s.style_id = sg.style_id
	JOIN 
		hierarchy_group hg (NOLOCK) ON sg.hierarchy_group_id = hg.hierarchy_group_id
	JOIN (SELECT style_code, SUM(quantity) 'sumQuantity' FROM 
		distribution_split_rpt (NOLOCK) WHERE destid = @storeNum AND sourceid = @warehouseNum AND released = 0 GROUP BY style_code) AS sumQuantity ON sumQuantity.style_code = s.style_code		
	WHERE 
		destid = @storeNum
	AND 
		sourceid = @warehouseNum
	AND 
		released = 0) AS inner_table
	ORDER BY 
		SortType
		, percentOfShipment DESC
		, inner_table.style_code DESC
		, release_date DESC
```

