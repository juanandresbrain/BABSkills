# DOMO.vwFlashGaapByHour

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["DOMO.vwFlashGaapByHour"]
    dbo_FGSummary(["dbo.FGSummary"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.FGSummary |

## View Code

```sql
CREATE view [DOMO].[vwFlashGaapByHour]

as 

----==================================================================================================
----	Author			Date			Details
----	Dan Tweedie		12/14/2016		Shows POS sales by hour, TY vs LY comp% by day total and up to the hour 
--										Dependent on SSIS FlashGaap having pre-staged the data
----==================================================================================================

select 
	right((replicate('0', 4) + cast(StoreID as varchar)),4) as StoreKey,
	StoreName,
	BusinessDate,
	BusinessHour,
	TYTransCountByHour as TransactionCountThisHour,
	case when CompStatus = 1 
		then TYTransCountByHour 
		else 0 
	end as CompTransactionCountThisHour,
	TYTransCountByHourRunningTotal as TransactionCountRunningTotal,
	case when CompStatus = 1
		then TYTransCountByHourRunningTotal 
		else 0
	end as CompTransactionCountRunningTotal,
	TYGaapByHourNative as FlashGaapSalesThisHourLocal,
	TYGaapByHourUSD as FlashGaapSalesThisHourUSD,
	case when CompStatus = 1
		then TYGaapByHourNative
		else 0
	end as CompFlashGaapSalesThisHourLocal,
	case when CompStatus = 1
		then TYGaapByHourUSD
		else 0
	end as CompFlashGaapSalesThisHourUSD,
	TYGaapByHourRunningTotalNative as FlashGaapSalesRunningTotalLocal,
	TYGaapByHourRunningTotalUSD as FlashGaapSalesRunningTotalUSD,
	case when CompStatus = 1
		then TYGaapByHourRunningTotalNative
		else 0
	end as CompFlashGaapSalesRunningTotalLocal,
	case when CompStatus = 1
		then TYGaapByHourRunningTotalUSD
		else 0
	end as CompFlashGaapSalesRunningTotalUSD,
	
	LYGaapByHourNative as LYSalesThisHourLocal,
	LYGaapByHourUSD as LYSalesThisHourUSD,
	case when CompStatus = 1
		then LYGaapByHourNative
		else 0
	end as CompLYSalesThisHourLocal,
	case when CompStatus = 1
		then LYGaapByHourUSD
		else 0
	end as CompLYSalesThisHourUSD,

	LYDayTotalSalesNative as LYSalesDayTotalLocal,
	LYDayTotalSalesUSD as LYSalesDayTotalUSD,
	case when CompStatus = 1
		then LYDayTotalSalesNative
		else 0
	end as CompLYSalesDayTotalLocal,
	case when CompStatus = 1
		then LYDayTotalSalesUSD 
		else 0
	end as CompLYSalesDayTotalUSD,
	SalesPercentToLYRunningTotal as SalesPercentToHourLY,
	SalesPercentToLYDayTotal as SalesPercentToTotalLY,
	case when CompStatus = 1
		then SalesPercentToLYRunningTotal
		else 0
	end as CompSalesPercentToHourLY,
	case when CompStatus = 1
		then SalesPercentToLYDayTotal
		else 0
	end as CompSalesPercentToTotalLY,
	CompStatus,
	Jurisdiction,
	TradingGroup,
	DaySalesPlan
from dwstaging.dbo.FGSummary
```

