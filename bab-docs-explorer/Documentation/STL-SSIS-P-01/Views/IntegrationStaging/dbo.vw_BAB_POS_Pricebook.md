# dbo.vw_BAB_POS_Pricebook

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vw_BAB_POS_Pricebook"]
    web_PricebookFact(["web.PricebookFact"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| web.PricebookFact |

## View Code

```sql
CREATE VIEW [dbo].[vw_BAB_POS_Pricebook]
AS

select Catalog, Style_code, CurrentPrice, SalePrice
from web.PricebookFact
--order by Catalog desc, style_code


dbo,vw_stgAllItems,CREATE VIEW dbo.vw_stgAllItems
AS
select row_Number() Over(Order by OrderID,sku) as OrderItemID,* from 
(
select OrderID,sku,qty from stgParentItems
union all
select P.OrderID,C.sku,c.qty from stgChildItems c inner Join stgParentItems p on (c.ParentItem = p.idNum)
where not c.sku is null) as allList

dbo,vwPBIBundledSKU,CREATE view [dbo].[vwPBIBundledSKU]

as 

--select DerivedUSStyleCode StyleCode, cast('1' as INT) as isBundle
--from PimBundleSkuExtract
--group by DerivedUSStyleCode
--union
--select DerivedUKStyleCode StyleCode, cast('1' as INT) as isBundle
--from PimBundleSkuExtract
--group by DerivedUKStyleCode

select cast(ComponentProducts as varchar(12)) as StyleCode, cast('1' as INT) as isBundle
from PimBundleSkuExtract
group by ComponentProducts
```

