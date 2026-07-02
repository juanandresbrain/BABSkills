# WEB.vwBundlePricebookFactPreStage_Bak20241003

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WEB.vwBundlePricebookFactPreStage_Bak20241003"]
    web_BundlePricebookFactPreStage(["web.BundlePricebookFactPreStage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| web.BundlePricebookFactPreStage |

## View Code

```sql
create view [WEB].[vwBundlePricebookFactPreStage_Bak20241003]

as



with DataStage as 
(
	select 
	p.BundleSku, 
	p.BundleDisplayName, 
	p.PriceBookCatalog as BundleSkuCatalog, 
	sum (case when p.PriceBookSalePrice is null 
			then p.PriceBookCurrentPrice 
		else p.PriceBookSalePrice end)  as BundleSkuPrice
	from web.BundlePricebookFactPreStage p
	where 1=1
	and p.GroupingType  = 'Bundle' -- Per Bryce Ahrens on 8/5/2024 Only Skus with this Grouping Type should be allowed 
	--and p.BundleSku = '224099_24174_24175_28093' -- Testing Purposes only
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

