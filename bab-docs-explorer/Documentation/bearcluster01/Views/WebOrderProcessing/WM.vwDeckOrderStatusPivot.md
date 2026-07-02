# WM.vwDeckOrderStatusPivot

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WM.vwDeckOrderStatusPivot"]
    wm_OMSCustomOrderExport(["wm.OMSCustomOrderExport"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| wm.OMSCustomOrderExport |

## View Code

```sql
CREATE view [WM].[vwDeckOrderStatusPivot] 

as

select 
	SiteCode,
	OrderNumber,
	OrderDate,
	[Manual Review] as ManualReview,
	[New],
	[Pending],
	[Completed],
	[Cancelled],
	[Review],
	[Fraud],
	[Confirmed Fraud] as ConfirmedFraud,
	[Exception],
	[Delayed Auto-Process] as DelayedAutoProcess
from 
	(
		select 
			SiteCode,
			OrderNumber,
			cast(OrderDateUTC as date) as OrderDate,
			OrderStatus,
			min(OrderItemStatusChangeDateUTC) StatusDateTime
		from wm.OMSCustomOrderExport with (nolock)
		group by 
			SiteCode,
			OrderNumber,
			cast(OrderDateUTC as date),
			OrderStatus
	) as OrderStatuses
pivot
	(
		min(StatusDateTime)
		for OrderStatus in 
			(
				[Manual Review],
				[New],
				[Pending],
				[Completed],
				[Cancelled],
				[Review],
				[Fraud],
				[Confirmed Fraud],
				[Exception],
				[Delayed Auto-Process]
			)
	) as PivotStatus
```

