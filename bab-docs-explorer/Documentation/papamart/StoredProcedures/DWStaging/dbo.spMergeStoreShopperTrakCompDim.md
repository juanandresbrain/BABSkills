# dbo.spMergeStoreShopperTrakCompDim

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMergeStoreShopperTrakCompDim"]
    dbo_Store_Shoppertrak_Comp_Dim(["dbo.Store_Shoppertrak_Comp_Dim"]) --> SP
    dbo_Store_Shoppertrak_Comp_Dim_Stage(["dbo.Store_Shoppertrak_Comp_Dim_Stage"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Store_Shoppertrak_Comp_Dim |
| dbo.Store_Shoppertrak_Comp_Dim_Stage |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMergeStoreShopperTrakCompDim] -- Update to Proper Name 

as 

-------------------------------------------------------------------------------------------------------
--	Tim Callahan	-	2021-10-25	-	Created proc - Merges Data from Store_Shoppertrak_Comp_Dim_Stage to Store_Shoppertrak_Comp_Dim
-------------------------------------------------------------------------------------------------------

set nocount on

merge into dw.dbo.Store_Shoppertrak_Comp_Dim  as target
using DWStaging.dbo.Store_Shoppertrak_Comp_Dim_Stage as source -- Use Entire Table as Source 
--using ( select * from table) as source -- Use SQL Command As Source
on 
	(
		target.[store_key]=source.[store_key] 
		and
		target.[date_key_from]=source.[date_key_from]
		
	)
When Matched and
	(		
			-- Besure to use isnull logic for compare otherwise may have unintended results 
		    --isnull(target.[date_key_from],0)<>isnull(source.[date_key_from],0) or 
			isnull(target.[date_key_thru],0)<>isnull(source.[date_key_thru],0) 
       
	)
Then Update
	-- Fields to be updated
	set     
		 --target.[date_key_from]=source.[date_key_from],
		 target.[date_key_thru]=source.[date_key_thru], 
		 target.[UPDT_DT]=getdate()
          
 
When Not Matched by target
Then Insert
	(
		-- Fields to be inserted 
		   [store_key],
		   [date_key_from],
		   [date_key_thru],
		   [INS_DT]
         
	)
Values
	(
           source.[store_key],
		   source.[date_key_from],
		   source.[date_key_thru],
           getdate()

	)

When Not Matched by source 
 Then delete 
;
```

