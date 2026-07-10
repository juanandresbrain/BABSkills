# dbo.spMergeUTAWorkBrainTeam

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMergeUTAWorkBrainTeam"]
    dbo_UTAWorkBrainTeam(["dbo.UTAWorkBrainTeam"]) --> SP
    dbo_UTAWorkBrainTeamStage(["dbo.UTAWorkBrainTeamStage"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.UTAWorkBrainTeam |
| dbo.UTAWorkBrainTeamStage |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMergeUTAWorkBrainTeam]

as 

-------------------------------------------------------------------------------------------------------
-- Dan Tweedie	2019-01-16	Created Proc for merging data from new UTA system that replaces Workbrain
-------------------------------------------------------------------------------------------------------

set nocount on

merge into DW.dbo.UTAWorkBrainTeam as target
using DWStaging.dbo.UTAWorkBrainTeamStage as source 
on 
	(
		target.WBT_ID=source.WBT_ID
	)
When Matched and
	(
		isnull(target.WBT_Name,'x')<>isnull(source.WBT_Name,'x')
		OR
		isnull(target.WBT_Parent_ID,0)<>isnull(source.WBT_Parent_ID,0)
		OR
		isnull(target.wbt_lft,0)<>isnull(source.wbt_lft,0)
		OR
		isnull(target.wbt_rgt,0)<>isnull(source.wbt_rgt,0)
	)
Then Update
	set 
		target.WBT_Name=source.WBT_Name,
		target.WBT_Parent_ID=source.WBT_Parent_ID,
		target.wbt_lft=source.wbt_lft,
		target.wbt_rgt=source.wbt_rgt,
		target.UpdateDate=getdate()
When Not Matched by target
Then Insert
	(
		WBT_ID,
		WBT_Name,
		WBT_Parent_ID,
		wbt_lft,
		wbt_rgt,
		InsertDate
	)
Values
	(
		source.WBT_ID,
		source.WBT_Name,
		source.WBT_Parent_ID,
		source.wbt_lft,
		source.wbt_rgt,
		getdate()
	)
;
```

