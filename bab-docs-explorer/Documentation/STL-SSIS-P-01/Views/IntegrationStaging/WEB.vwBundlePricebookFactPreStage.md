# WEB.vwBundlePricebookFactPreStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WEB.vwBundlePricebookFactPreStage"]
    web_BundlePricebookFactPreStage(["web.BundlePricebookFactPreStage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| web.BundlePricebookFactPreStage |

## View Code

```sql
CREATE view [WEB].[vwBundlePricebookFactPreStage]

as



with DataStage as 
(
	select 
	p.BundleSku, 
	p.BundleDisplayName, 
	p.PriceBookCatalog as BundleSkuCatalog, 
	--sum (case when p.PriceBookSalePrice is null 
	--		then p.PriceBookCurrentPrice 
	--	else p.PriceBookSalePrice end)  as BundleSkuPrice, 
		sum (
		case when p.PriceBookSalePrice is null 
			then p.PriceBookCurrentPrice*p.ComponentQuantity
		else p.PriceBookSalePrice*p.ComponentQuantity end)  as BundleSkuPrice -- Replaced above on 9/26/2024 as related to JIRA BIB-1024
	from web.BundlePricebookFactPreStage p
	where 1=1
	and p.GroupingType  = 'Bundle' -- Per Bryce Ahrens on 8/5/2024 Only Skus with this Grouping Type should be allowed 
	--and p.BundleSku in ('225448_25681_25626','32498_32495_22920_22920') -- Testing Purposes only
	group by
	p.BundleSku, 
	p.BundleDisplayName, 
	p.PriceBookCatalog

)
, 
NoDuplicates  as (
select 
ds.BundleSku
,ds.BundleSkuCatalog
--, count (*)
from DataStage ds
where 1=1
group by 
ds.BundleSku
,ds.BundleSkuCatalog
having count (*) = 1
) 


Select 
ds.BundleSku
,ds.BundleDisplayName
,ds.BundleSkuCatalog
,ds.BundleSkuPrice

from DataStage ds 
join NoDuplicates nd on ds.BundleSku = nd.BundleSku and ds.BundleSkuCatalog = nd.BundleSkuCatalog
```

