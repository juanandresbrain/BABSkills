# WEB.spMergePricebookBundleSkuFact

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WEB.spMergePricebookBundleSkuFact"]
    WEB_PricebookBundleSkuFact(["WEB.PricebookBundleSkuFact"]) --> SP
    WEB_vwBundlePricebookFactPreStage(["WEB.vwBundlePricebookFactPreStage"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WEB.PricebookBundleSkuFact |
| WEB.vwBundlePricebookFactPreStage |

## Stored Procedure Code

```sql
CREATE proc [WEB].[spMergePricebookBundleSkuFact]-- Update to Proper Name 

as 

-------------------------------------------------------------------------------------------------------
--	Tim Callahan	-	2024-03-18	-	Created proc - Merges Bundle Pricing Data from  web.BundlePricebookFactPreStage to [WEB].[PricebookBundleSkuFact] 
-------------------------------------------------------------------------------------------------------

set nocount on

merge into [WEB].[PricebookBundleSkuFact] as target
using 
	( 
	--select 
	--p.BundleSku, 
	--p.BundleDisplayName, 
	--p.PriceBookCatalog as BundleSkuCatalog, 
	--sum (case when p.PriceBookSalePrice is null 
	--		then p.PriceBookCurrentPrice 
	--	else p.PriceBookSalePrice end)  as BundleSkuPrice
	--from web.BundlePricebookFactPreStage p
	--where 1=1
	--and p.GroupingType  = 'Bundle' -- Per Bryce Ahrens on 8/5/2024 Only Skus with this Grouping Type should be allowed 
	----and p.BundleSku = '224099_24174_24175_28093' -- Testing Purposes only
	--group by
	--p.BundleSku, 
	--p.BundleDisplayName, 
	--p.PriceBookCatalog

	-- Replaced above with New View on 9/15/2024 due to duplicate PIM entries data 
	select 
	BundleSku
	,BundleDisplayName
	,BundleSkuCatalog
	,BundleSkuPrice

	from [WEB].[vwBundlePricebookFactPreStage] 

	) as source 
on 
	(
		target.[BundleSku]=source.[BundleSku]
			and 
		target.[BundleSkuCatalog]=source.[BundleSkuCatalog]
	)
When Matched and
	(		
			-- Besure to use isnull logic for compare otherwise may have unintended results 
		    isnull(target.[BundleSkuPrice],99999)<>isnull(source.[BundleSkuPrice],99999) 
				or 
			isnull(target.[BundleDisplayName],'x')<>isnull(source.[BundleDisplayName],'x') 
			
       
	)
Then Update
	-- Fields to be updated
	set     
		target.BundleSkuPrice = source.BundleSkuPrice,
		target.BundleDisplayName = source.BundleDisplayName, -- Added as part of JIRA BIB1024
		target.UpdateDate = getdate(),
		target.CheckDate = getdate()
		,target.Exported = null 
		,target.ExportDate= null
		 
		          
 
When Not Matched by target
Then Insert
	(
		-- Fields to be inserted 
		BundleSku, 
		BundleDisplayName, 
		BundleSkuPrice, 
		BundleSkuCatalog, 
		InsertDate, 
		UpdateDate, 
		CheckDate, 
		Exported, 
		ExportDate
         
	)
Values
	(
		source.BundleSku, 
		source.BundleDisplayName, 
		source.BundleSkuPrice, 
		source.BundleSkuCatalog, 
		getdate(), 
		null, 
		getdate(), 
		null, 
		null 
	)


;
```

