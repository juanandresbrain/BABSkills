# WEB.vwPricebookListUSXML_Full

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WEB.vwPricebookListUSXML_Full"]
    WEB_PricebookFact(["WEB.PricebookFact"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WEB.PricebookFact |

## View Code

```sql
CREATE view [WEB].[vwPricebookListUSXML_Full]

as

--------------------------------------------------------------------------------------------------
-- vwPricebookListUSXML - Outputs XML for eCommerce Pricebook-list XML - Integrates with Salesforce
--- 2017-05-30 - Dan Tweedie - Created View
--- 2022-07-06 - Tim Callahan - Modified View to use Sale Price rather than Current Price and filters as related to JIRA Task BIB-402
--- 2022-07-06 - Tim Callahan - Modififed where clauses to capture newly created styles
--- 2023-08-23 - Tim Callahan - Created for Feedonomics Testing 
---------------------------------------------------------------------------------------------------


With 
XMLStage (XML) as
	(
		select
			(
				select
					'buildabear-usd-list-prices' as '@pricebook-id',
					'USD' as 'currency',
					'x-default' as 'display-name/@xml:lang',
					'List Prices' as 'display-name',
					'true' as 'online-flag'
				for xml path('header'), Type
			),
			(
				select 
					(
						select *
						from 
							(
								--select
								--	style_code as '@product-id',
								--	'delete' as '@mode', NULL xtra1,
								--	'1' as 'amount/@quantity',
								--	--CurrentPrice as 'amount',NULL xtra2
								--	 SalePrice as 'amount',NULL xtra2 -- Changed on 2022-07-06 
								--from WEB.PricebookFactArchive
								--where catalog = 'US'
								--and CurrentPrice is not NULL
								--and ChangeType in ('DELETE', 'UPDATE')
								--and CurrentBatch = 1
								--and style_code not in (select style_code from WEB.PricebookFact)
								--and (SalePrice is not null and SalePrice <> 0.00) -- 2022-07-06 
								--UNION
								select
									style_code as '@product-id',
									NULL as '@mode', NULL xtra1,
									'1' as 'amount/@quantity',
									--CurrentPrice as 'amount',NULL xtra2
									case when SalePrice is null 
										then CurrentPrice else 
									SalePrice end as 'amount',NULL xtra2 -- Changed on 2022-07-06 
								from WEB.PricebookFact								
								where catalog = 'US'
								--and (Exported is null and ExportDate is null) -- Added 2022-07-06 
								and (CurrentPrice <> 0.00 and isnull(SalePrice,0.01) <> 0.00)
							) x
						
						for xml path('price-table'), Type
					)
				for xml path('price-tables'), Type
			)
		for xml path('pricebook'), root('pricebooks'), Type
	)
select 
	XML as XMLData
from XMLStage
```

