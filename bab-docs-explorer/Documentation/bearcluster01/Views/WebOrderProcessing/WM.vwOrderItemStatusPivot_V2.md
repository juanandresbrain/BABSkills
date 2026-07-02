# WM.vwOrderItemStatusPivot_V2

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WM.vwOrderItemStatusPivot_V2"]
    WM_ItemStatus(["WM.ItemStatus"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WM.ItemStatus |

## View Code

```sql
CREATE view [WM].[vwOrderItemStatusPivot_V2]

---------------------------------------------------------------------------------------------------------------------------------------------
--- Dan Tweedie - 2017-09-12 - Created view - Returns OrderID, and a 1 or 0 (yes or no) for Item Status 
--											If order has ItemStatus record in a specified current status, the value is 1 for that status
---------------------------------------------------------------------------------------------------------------------------------------------

as

WITH
OrderStatusPivot as
	(
		select
			OrderID,
			IZGIFT,
			IWVP,
			Pending,
			[IN],
			IV,
			IZE,
			Shipped,
			Waved,
			IR,
			ISRP,
			IZDT,
			SAComplete,
			RYVTransferred,
			ShippedFromStore,
			OZ,
			OPPS,
			OPPU,
			ORPU,
			OPU,
			OIVNC,
			OIV,
			IZ,
			MP
		from
			(
				select 
					OrderID,
					Status as ItemStatus,
					count(*) RowsCount
				from WM.ItemStatus with (nolock)
				where CurrentStatus = 1
				group by OrderID, Status
			) as OrderItemStatusCounts
			PIVOT
			(
				Sum(RowsCount)
				for ItemStatus
				in 
					(
						IZGIFT,
						IWVP,
						Pending,
						[IN],
						IV,
						IZE,
						Shipped,
						Waved,
						IR,
						ISRP,
						IZDT,
						SAComplete,
						RYVTransferred,
						ShippedFromStore,
						OZ,
						OPPS,
						OPPU,
						ORPU,
						OPU,
						OIVNC,
						OIV,
						IZ,
						MP
					) 
			) as pivotTable
	)
select 
	OrderID,
	sum(case when isnull(IZGIFT,0) > 0
			then 1
			else 0
		end) as hasIZGIFT,
	sum(case when isnull(IWVP,0) > 0 
		then 1
		else 0
		end) as hasIWVP,
	sum(case when isnull(Pending,0) > 0 
		then 1
		else 0
		end) as hasPending,
	sum(case when isnull([IN],0) > 0 
		then 1
		else 0
		end) as hasIN,
	sum(case when isnull(IV,0) > 0
		then 1
		else 0
		end) as hasIV,
	sum(case when isnull(IZE,0) > 0
		then 1
		else 0
		end) as hasIZE,
	sum(case when isnull(Shipped,0) > 0 OR ISNULL(OZ, 0) > 0
		then 1
		else 0
		end) as hasShipped,
	sum(case when isnull(Waved,0) > 0 OR ISNULL(OPPS, 0) > 0
		then 1
		else 0
		end) as hasWaved,
	sum(case when isnull(IR,0) > 0
		then 1
		else 0
		end) as hasIR,
	sum(case when isnull(ISRP,0) > 0
		then 1
		else 0
		end) as hasISRP,
	sum(case when isnull(IZDT,0) > 0
		then 1
		else 0
		end) as hasIZDT,
	sum(case when isnull(SAComplete,0) > 0
		then 1
		else 0
		end) as hasSAComplete,
	sum(case when isnull(RYVTransferred,0) > 0
		then 1
		else 0
		end) as hasRYVTransferred,
	sum(case when isnull(ShippedFromStore,0) > 0
		then 1
		else 0
		end) as hasShippedFromStore,
	sum(case when isnull(OPPU,0) > 0
		then 1
		else 0
		end) as hasPickingForPickup,
	sum(case when isnull(ORPU,0) > 0
		then 1
		else 0
		end) as hasReadyForPickup,
	sum(case when isnull(OPU,0) > 0
		then 1
		else 0
		end) as hasPickedUp,
	sum(case when isnull(OIV,0) > 0
		then 1
		else 0
		end) as hasPickupCancelled,
	sum(case when isnull(OIVNC,0) > 0
		then 1
		else 0
		end) as hasPickupCancelledWithRefund,
	sum(case when isnull(IZ,0) > 0
		then 1
		else 0
		end) as hasIZ,
	sum(case when isnull(MP,0) > 0
		then 1
		else 0
		end) as hasMP
from OrderStatusPivot
group by OrderID
```

