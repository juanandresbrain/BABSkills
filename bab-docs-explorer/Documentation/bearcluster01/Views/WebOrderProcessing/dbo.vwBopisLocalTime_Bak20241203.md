# dbo.vwBopisLocalTime_Bak20241203

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwBopisLocalTime_Bak20241203"]
    dbo_vwDWOpenStores(["dbo.vwDWOpenStores"]) --> VIEW
    dbo_WebDemandOrderItemz(["dbo.WebDemandOrderItemz"]) --> VIEW
    dbo_WebDemandOrderz(["dbo.WebDemandOrderz"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.vwDWOpenStores |
| dbo.WebDemandOrderItemz |
| dbo.WebDemandOrderz |

## View Code

```sql
CREATE view [dbo].[vwBopisLocalTime_Bak20241203]

as


select 
	o.OrderNumber, 
	o.LastUpdateDateUTC,
	dateadd(hh, s.GMT_Offset, o.LastUpdateDateUTC) LastUpdateDateLocal,
	concat(left(convert(varchar, o.LastUpdateDateUTC, 108), 3)
				, case when right(convert(varchar, o.LastUpdateDateUTC, 108), 2) < 30 
					then '00' else '30' end
			) as UTCTimeSlot,
	concat(left(convert(varchar, dateadd(hh, s.GMT_Offset, o.LastUpdateDateUTC), 108), 3)
				, case when right(convert(varchar, dateadd(hh, s.GMT_Offset, o.LastUpdateDateUTC), 108), 2) < 30 
					then '00' else '30' end
			) as LocalTimeSlot,
	case when cast(oi.WarehouseCode as int) < 2000 then 1000 + cast(oi.WarehouseCode as int) else cast(oi.WarehouseCode as int) end as StoreCode,
	oi.DeliveryType
from WebDemandOrderz o 
join WebDemandOrderItemz oi on o.OrderNumber=oi.OrderNumber   
join kodiak.BABWMstrData.dbo.vwDWOpenStores s 
	on cast(oi.WarehouseCode as int)=s.StoreID
	and s.StoreID not in (13,2013)
where oi.ItemStatus in 
	(
		'Store Shipped',
		--'Gift Card Devalued',
		'Return',
		--'Pending Sound',
		--'Cancel Pickup',
		'Shipped',
		'Picked Up',
		--'Gift Card Processed',
		--'Donation Processed',
		'Delivered'
		--'Cancel Pickup - No Credit',
		--'Resend e-Gift Card Email',
		--'Cancel Record Your Voice',
		--'Cancelled',
	)
group by 
	o.OrderNumber, 
	o.LastUpdateDateUTC,
	 dateadd(hh, s.GMT_Offset, o.LastUpdateDateUTC),
	 concat(left(convert(varchar, o.LastUpdateDateUTC, 108), 3)
				, case when right(convert(varchar, o.LastUpdateDateUTC, 108), 2) < 30 
					then '00' else '30' end
			) ,
	 concat(left(convert(varchar, dateadd(hh, s.GMT_Offset, o.LastUpdateDateUTC), 108), 3)
				, case when right(convert(varchar, dateadd(hh, s.GMT_Offset, o.LastUpdateDateUTC), 108), 2) < 30 
					then '00' else '30' end
			),
	cast(oi.WarehouseCode as int),
	oi.DeliveryType
```

