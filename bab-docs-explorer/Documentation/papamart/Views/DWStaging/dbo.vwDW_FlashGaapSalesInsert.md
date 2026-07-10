# dbo.vwDW_FlashGaapSalesInsert

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_FlashGaapSalesInsert"]
    dbo_FlashGaapSalesStage(["dbo.FlashGaapSalesStage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.FlashGaapSalesStage |

## View Code

```sql
CREATE view [dbo].[vwDW_FlashGaapSalesInsert]

as 

-- =====================================================================================================
-- Name: vwDW_FlashGaapSalesInsert
--
--Description: Inserts from dwstaging.dbo.FlashGaapSalesStage into dw.dbo.FlashGaapSales
--				
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		10/10/2016		Created proc.	
--		Dan Tweedie		2022-06-27		updated to exclude VAT for UK and Ireland
-- =====================================================================================================


select 
	store_key,
	local_date_key,
	local_time_key,
	case when local_hour between 0 and 2
			then local_date_key -1
			else local_date_key 
	end as business_date_key,
	case 
		when Jurisdiction='United Kingdom' 
			then sum(flash_gaap_sales) / 1.2
		when Jurisdiction='Ireland'
			then sum(flash_gaap_sales) / 1.23
		else sum(flash_gaap_sales) 
	end as flash_gaap_sales,
	TransactionCount,
	NetUnits,
	source,
	Jurisdiction,
	CurrencyCode,
	TradingGroup,
	insert_datetime,
	ETLLogID
from dwstaging.dbo.FlashGaapSalesStage 
group by 
	store_key,
	local_date_key,
	local_time_key,
	case when local_hour between 0 and 2
			then local_date_key -1
			else local_date_key 
	end,
	TransactionCount,
	NetUnits,
	source,
	Jurisdiction,
	CurrencyCode,
	TradingGroup,
	insert_datetime,
	ETLLogID
```

