# dbo.spMergePimBundleSkuExtract_Bak20241003

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMergePimBundleSkuExtract_Bak20241003"]
    dbo_PimBundleSkuExtract(["dbo.PimBundleSkuExtract"]) --> SP
    dbo_PimBundleSkuExtractStageConsolidatedAndCleansed(["dbo.PimBundleSkuExtractStageConsolidatedAndCleansed"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.PimBundleSkuExtract |
| dbo.PimBundleSkuExtractStageConsolidatedAndCleansed |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMergePimBundleSkuExtract_Bak20241003] -- Update to Proper Name 

as 

-------------------------------------------------------------------------------------------------------
--	Tim Callahan	-	2024-03-13	-	Created proc - Merges PIM Bundle Sku Data
--	Tim Callahan	-	2024-09-05	-	Updated merge to update Display name and KeyStory, updated source definition as well 
-------------------------------------------------------------------------------------------------------

set nocount on

merge into [PimBundleSkuExtract] as target
--using PimBundleSkuExtractStageConsolidatedAndCleansed as source -- Use Entire Table as Source 

using 
(
select *
from PimBundleSkuExtractStageConsolidatedAndCleansed
where 1=1
and GroupingType = 'Bundle' -- Per Bryce Only Entries with a Grouping Type of Bundle should flow to SFCC -- So eliminating that noise 
)
as source 

on 
	(
		target.[PrimaryId]=source.[PrimaryId] -- Key 
			and 
		target.[Catalog] = source.[Catalog] -- Key 
			and 
		--target.[KeyStory]=source.[KeyStory] -- Key 
		--	and 
		target.[GroupingType]=source.[GroupingType] -- Key 
			and
		target.[ComponentProducts]=source.[ComponentProducts] -- Key 
			
	)
When Matched and
	(				
		    isnull(target.[DisplayName],'x')<>isnull(source.[DisplayName],'x')
				or 
			isnull(target.[KeyStory],'x')<>isnull(source.[KeyStory],'x')
			       
	)
Then Update
	-- Fields to be updated
	set     
		 target.[DisplayName]=source.[DisplayName],		 
		 target.[KeyStory]=source.[KeyStory],		 
		 target.[UpdateDate]=getdate()

When Not Matched by target
Then Insert
	(
		-- Fields to be inserted 
		 PrimaryId
		,LocalProductCode
		,KeyStory
		,GroupingType
		,MSTAT
		,ComponentProducts
		,DisplayName
		,Catalog
		,CountComponentProducts
		,InsertDate
         
	)
Values
	(
		  source.PrimaryId
		, source.LocalProductCode
		, source.KeyStory
		, source.GroupingType
		, source.MSTAT
		, source.ComponentProducts
		, source.DisplayName
		, source.Catalog
		, source.CountComponentProducts
		,getdate()

	)
;
```

