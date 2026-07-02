# WM.vwDeckOrderItemStatusPivot

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WM.vwDeckOrderItemStatusPivot"]
    wm_OMSCustomOrderExport(["wm.OMSCustomOrderExport"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| wm.OMSCustomOrderExport |

## View Code

```sql
CREATE view [WM].[vwDeckOrderItemStatusPivot]

as

with 
MaxStatusDate as
	(
		select 
			OrderNumber,
			max(OrderItemStatusChangeDateUTC) OrderItemStatusChangeDateUTC
		from wm.OMSCustomOrderExport
		where 1=1
		and isnull(OrderItemTypeName,'x') <> 'eGift' 
		and isnull(OrderItemCustom1,'x') <> 'Build-A-Bear Donation'
		group by 
			OrderNumber
	),
MaxStatus as
	(
		select 
			e.OrderNumber,
			e.OrderStatus,
			e.ItemStatus
		from wm.OMSCustomOrderExport e
		join MaxStatusDate m 
			on e.OrderNumber=m.OrderNumber
			and e.OrderItemStatusChangeDateUTC=m.OrderItemStatusChangeDateUTC
		where 1=1
		and isnull(OrderItemTypeName,'x') <> 'eGift' 
		and isnull(OrderItemCustom1,'x') <> 'Build-A-Bear Donation'
		group by 
			e.OrderNumber,
			e.OrderStatus,
			e.ItemStatus
	),
MaxUpdate as
	(
		select 
			OrderNumber,
			OrderStatus,
			ItemStatus,
			max(OrderItemStatusChangeDateUTC) OrderItemStatusChangeDateUTC
		from wm.OMSCustomOrderExport
		where 1=1
		and isnull(OrderItemTypeName,'x') <> 'eGift' 
		and isnull(OrderItemCustom1,'x') <> 'Build-A-Bear Donation'
		group by 
			OrderNumber,
			OrderStatus,
			ItemStatus
	),
Statuses as
	(
		select
			e.SiteCode,
			e.OrderNumber,
			cast(e.OrderDateUTC as date) OrderDate,
			e.OrderItemStatusChangeDateUTC StatusDateTime,
			e.OrderStatus,
			e.ItemStatus
		from wm.OMSCustomOrderExport e with (nolock)
		join MaxUpdate m 
			on e.OrderNumber=m.OrderNumber 
			and e.OrderStatus=m.OrderStatus
			and e.ItemStatus=m.ItemStatus
			and e.OrderItemStatusChangeDateUTC=m.OrderItemStatusChangeDateUTC
		where 1=1
		and isnull(e.OrderItemTypeName,'x') <> 'eGift' 
		and isnull(e.OrderItemCustom1,'x') <> 'Build-A-Bear Donation'
		group by 
			e.SiteCode,
			e.OrderNumber,
			cast(e.OrderDateUTC as date),
			e.OrderItemStatusChangeDateUTC,
			e.OrderStatus,
			e.ItemStatus
	),
Pivoted as 
	(
		select 
			SiteCode,
			OrderNumber,
			OrderDate,
			min([New]) as New,
			min([Cancelled]) as Cancelled,
			min([Gift Card Processed]) as GiftCardProcessed,
			min([Donation Processed]) as DonationProcessed,
			min([Gift Card Devalued]) as GiftCardDevalued,
			min([Need Warehouse]) as NeedWarehouse,
			min([Not Available]) as NotAvailable,
			min([Pending Sound]) as PendingSound,
			min([Sound Recorded]) as SoundRecorded,
			min([Pending Wave]) as PendingWave,
			min([Waved]) as Waved,
			min([Store Pending Ship]) as StorePendingShip,
			min([Picking for Shipping]) as PickingForShipping,
			min([Store Shipped]) as StoreShipped,
			min([Resend e-Gift Card Email]) as ResendEGiftCardEmail,
			min([Shipping Error]) as ShippingError,
			min([Shipped]) as Shipped,
			min([Return]) as Returned,
			min([Return (no credit)]) as ReturnNoCredit
		from Statuses 
			pivot
				(
					min(StatusDateTime)
					for ItemStatus in 
						(
							[New],
							[Cancelled],
							[Gift Card Processed],
							[Donation Processed],
							[Gift Card Devalued],
							[Need Warehouse],
							[Not Available],
							[Pending Sound],
							[Sound Recorded],
							[Pending Wave],
							[Waved],
							[Store Pending Ship],
							[Picking for Shipping],
							[Store Shipped],
							[Resend e-Gift Card Email],
							[Shipping Error],
							[Shipped],
							[Return],
							[Return (no credit)]
						)
				) as pivoted
		group by 
			SiteCode,
			OrderNumber,
			OrderDate
	)
select 
	p.SiteCode,	
	p.OrderNumber,	
	p.OrderDate,	
	p.New,	
	p.Cancelled,	
	p.GiftCardProcessed,	
	p.DonationProcessed,	
	p.GiftCardDevalued,	
	p.NeedWarehouse,	
	p.NotAvailable,	
	p.PendingSound,	
	p.SoundRecorded,	
	p.PendingWave,	
	p.Waved,	
	p.StorePendingShip,	
	p.PickingForShipping,
	p.StoreShipped,	
	p.ResendEGiftCardEmail,	
	p.ShippingError,	
	p.Shipped,	
	p.Returned,	
	p.ReturnNoCredit,	
	m.OrderStatus as CurrentOrderStatus,
	m.ItemStatus as CurrentItemStatus
from Pivoted p
join MaxStatus m on p.OrderNumber=m.OrderNumber
```

