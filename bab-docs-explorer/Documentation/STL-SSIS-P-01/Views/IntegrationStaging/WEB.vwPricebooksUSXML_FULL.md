# WEB.vwPricebooksUSXML_FULL

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WEB.vwPricebooksUSXML_FULL"]
    WEB_vwPricebookListUSXML_FULL(["WEB.vwPricebookListUSXML_FULL"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WEB.vwPricebookListUSXML_FULL |

## View Code

```sql
CREATE view [WEB].[vwPricebooksUSXML_FULL]

as 

--------------------------------------------------------------------------------------------------
-- vwPricebooksUSXML - Outputs XML for eCommerce US pricebooks
--- 2017-05-31 - Dan Tweedie - Created View
--- 2022-07-06 - Tim Callahan - Modified View to Only Send List Price XML data 
--- 2023-08-28 - Tim Callahan - Created for Feedonomics Integration
---------------------------------------------------------------------------------------------------

WITH
Stage1 (XML) as
	(
		select cast(XMLData as nvarchar(max)) as XMLData
		from WEB.vwPricebookListUSXML_FULL
		--UNION
		--select cast(XMLData as nvarchar(max)) as XMLData
		--from WEB.vwPricebookSaleUSXML
	),
Stage2 (XML) as
	(
		select cast(XML as xml)
		from Stage1
		for xml path, Type
	),
Stage3 (XML) as
	(
		select --yes this is confusing, but I need to play with the output and must be nvarchar to do that, then i want final output to be XML
					--also, my xml wasn't coming out correctly with both pricebook(s) under a single <pricebooks> element, so I had to take matters in to my own hands
			cast(replace(replace(replace(replace(cast(XML as nvarchar(max)), '<pricebooks>', ''), '</pricebooks>', ''), '<row>', ''), '</row>', '') as xml)
		from Stage2
		for xml path('pricebooks'), Type
	)
select 
	cast(replace(cast(XML as nvarchar(max)), '<pricebooks>', '<pricebooks xmlns="http://www.demandware.com/xml/impex/pricebook/2006-10-31">') as xml) as XMLData
from Stage3







WEB,vwPriceLists,create view WEB.vwPriceLists

as

With 
ItemsAllowedZeroSalePrice as
(
	select BABWProductID 
	from web.ProductCatalogMasterAttributes
	where left(HierarchyGroupCode, 5) in ('R-B-D', 'R-B-U')
	and substring(HierarchyGroupCode, 7,2) in ('46', '47', '60', '65', '75', '80')
	and BABWProductID in (select style_code from web.PricebookFact)
),
SalePrice as
(
	select
		Catalog,
		style_code,
		SalePrice
	from WEB.PricebookFact
	where SalePrice is NOT NULL
	and (
			(SalePrice > 0 OR style_code in (select BABWProductID from ItemsAllowedZeroSalePrice))
		)
),
ListPrice as
(
	select
		Catalog,
		style_code,
		CurrentPrice as ListPrice
	from WEB.PricebookFact
)
select 
	f.Catalog as SiteCountry,
	f.style_code,
	s.SalePrice,
	l.ListPrice
from WEB.PricebookFact f
left join SalePrice s 
	on f.Catalog = s.Catalog
	and f.style_code = s.style_code
left join ListPrice l 
	on f.Catalog = l.Catalog
	and f.style_code = l.style_code
```

