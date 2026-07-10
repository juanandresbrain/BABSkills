# dbo.spMergeHR_StoreForcePosSalesFactFromDWDynamicsNEW20240328

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMergeHR_StoreForcePosSalesFactFromDWDynamicsNEW20240328"]
    date_dim(["date_dim"]) --> SP
    dbo_HR_StoreforceCustomerMetricsStage(["dbo.HR_StoreforceCustomerMetricsStage"]) --> SP
    HR_StoreForcePosSalesFact(["HR_StoreForcePosSalesFact"]) --> SP
    dbo_HR_StoreForcePosStoreListStage(["dbo.HR_StoreForcePosStoreListStage"]) --> SP
    product_dim(["product_dim"]) --> SP
    store_dim(["store_dim"]) --> SP
    time_dim(["time_dim"]) --> SP
    TransactionDetailFactsDynamics(["TransactionDetailFactsDynamics"]) --> SP
    TransactionFactsDynamics(["TransactionFactsDynamics"]) --> SP
    vwDW_Transactions_Cube_V3_Dynamics(["vwDW_Transactions_Cube_V3_Dynamics"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| date_dim |
| dbo.HR_StoreforceCustomerMetricsStage |
| HR_StoreForcePosSalesFact |
| dbo.HR_StoreForcePosStoreListStage |
| product_dim |
| store_dim |
| time_dim |
| TransactionDetailFactsDynamics |
| TransactionFactsDynamics |
| vwDW_Transactions_Cube_V3_Dynamics |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMergeHR_StoreForcePosSalesFactFromDWDynamicsNEW20240328]


as 

set nocount on


BEGIN

		IF (Object_ID('tempdb..#MergeStage') IS NOT null) DROP TABLE #MergeStage;

		with 
		AllTime (Slot) as
		(
					select '00:00'	UNION	select '00:30'	UNION	select '01:00'	UNION	select '01:30'	UNION	select '02:00'	UNION	select '02:30'	UNION	select '03:00'	UNION	select '03:30'
			UNION	select '04:00'	UNION	select '04:30'	UNION	select '05:00'	UNION	select '05:30'	UNION	select '06:00'	UNION	select '06:30'	UNION	select '07:00'	UNION	select '07:30'
			UNION	select '08:00'	UNION	select '08:30'	UNION	select '09:00'	UNION	select '09:30'	UNION	select '10:00'	UNION	select '10:30'	UNION	select '11:00'	UNION	select '11:30'
			UNION	select '12:00'	UNION	select '12:30'	UNION	select '13:00'	UNION	select '13:30'	UNION	select '14:00'	UNION	select '14:30'	UNION	select '15:00'  UNION	select '15:30'
			UNION	select '16:00'	UNION	select '16:30'	UNION	select '17:00'	UNION	select '17:30'	UNION	select '18:00'	UNION	select '18:30'	UNION	select '19:00'	UNION	select '19:30'
			UNION	select '20:00'	UNION	select '20:30'	UNION	select '21:00'	UNION	select '21:30'	UNION	select '22:00'	UNION	select '22:30'	UNION	select '23:00'	UNION	select '23:30'
		),
		DateTimes as
		(
			select distinct
				cast(dd.actual_date as date) as RawDate,
				convert(varchar, dd.actual_date, 103) as Date,
				alt.Slot
			from date_dim dd with (nolock) 
			cross join AllTime alt
			where datediff(dd, dd.actual_date,getdate()) =0 
			or (datepart(hh,getdate())<=2 and cast(dd.actual_date as date)=cast(getdate()-1 as date))
		),
		StoreDateTime as
		(
			select 
				dt.RawDate,
				dt.Date,
				sl.LocationCode as StoreCode,
				dt.Slot,
				sl.StoreID as StoreCodeRaw
			from dwStaging.dbo.HR_StoreForcePosStoreListStage sl
			cross join DateTimes dt
			where sl.StoreID in (2019, 2079, 2080, 2082, 2083)
		),
		PartyCounts as
			(
				select 
					ss.LocationCode as StoreCode,
					cast(dd.actual_date as date) as RawDate,
					convert(varchar, dd.actual_date, 103) as Date,
					right((cast('00' as varchar) + cast(td.hour as varchar)),2)
						+ ':' + case when td.Minute < 30 then '00' else '30' end as Slot,
					count(distinct tf.party_key) as PartyCount
				from TransactionFactsDynamics tf with (nolock)
				join store_dim sd with (nolock) on tf.store_key=sd.store_key
				join dwStaging.dbo.HR_StoreForcePosStoreListStage ss on sd.store_id=ss.StoreID
				join date_dim dd with (nolock) on tf.date_key=dd.date_key
				join time_dim td with (nolock) on tf.time_key=td.time_key
				where 1=1
				and tf.party_key <> 0
				and (datediff(dd, dd.actual_date,getdate()) =0 
						or (datepart(hh,getdate())<=2 and cast(dd.actual_date as date)=cast(getdate()-1 as date))
					)
				and sd.store_id in (2019, 2079, 2080, 2082, 2083)
				group by 
					ss.LocationCode,
					cast(dd.actual_date as date),
					convert(varchar, dd.actual_date, 103),
					right((cast('00' as varchar) + cast(td.hour as varchar)),2)
						+ ':' + case when td.Minute < 30 then '00' else '30' end 
			),
		Backpacks as
			(
				select 
					ss.LocationCode as StoreCode,
					cast(dd.actual_date as date) as RawDate,
					convert(varchar, dd.actual_date, 103) as Date,
					right((cast('00' as varchar) + cast(td.hour as varchar)),2)
						+ ':' + case when td.Minute < 30 then '00' else '30' end as Slot,
					count(distinct tdf.transaction_id) as BackPackTransactions,
					sum(tdf.units) as BackpackUnits
				from TransactionDetailFactsDynamics tdf with (nolock)
				join product_dim pd with (nolock) on tdf.product_key=pd.product_key
				join store_dim sd with (nolock) on tdf.store_key=sd.store_key
				join dwStaging.dbo.HR_StoreForcePosStoreListStage ss on sd.store_id=ss.StoreID
				join date_dim dd with (nolock) on tdf.date_key=dd.date_key
				join time_dim td with (nolock) on tdf.time_key=td.time_key
				where 1=1
					and (datediff(dd, dd.actual_date,getdate()) =0 
							or (datepart(hh,getdate())<=2 and cast(dd.actual_date as date)=cast(getdate()-1 as date))
						)
					and pd.style_code in ('427634','427582','427152','426821','426749','426378','426369','426286','426259','426219','426132','425617','425354','425152','424965','424685','424443','424286','424244','422963','422962','422824','422823','422049','421816','421815','420551','420550','415836','127634','127582','127152','126821','126749','126378','126286','126132','125617','125354','125152','124965','124685','124443','124244','122824','122823','122049','121816','121815','120551','120550','027634','027582','027217','027152','026980','026838','026821','026749','026603','026378','026369','026286','026166','026132','025617','025354','025152','024965','024685','024443','024290','024286','024244','023842','023834','022889','022888','022887','022886','022831','022830','022829','022828','022824','022823','022141','022049','021816','021815','020559','020558','020557','020556','020555','020554','020553','020552','020551','020550','018194','017295','015833','015831','015830','015281','014258','031829','027765','026378','025617','030306','031696','031659','028925','028552','025354','028895','022831','022830','022888','030394','027217','026603','022829','030418','028855','022886','026166','031977','022887','031451','031510','031408','031059','026915','024290','030174','028741','032063','028559','029984','026749','022824','028403','026980','027910','024244','021815','022141','032078','032096','032008','028473','027582','028405','027893','027634','029842','024965','026838','030548','131829','127765','126378','125617','130306','131696','131659','128925','128552','125354','128895','130394','130418','131977','131451','131408','131059','130174','128741','132063','129984','126749','122824','128403','127910','124244','121815','132078','132008','128473','127582','128405','127893','127634','129842','124965','130548','431829','427765','426378','425617','430306','431696','431659','428925','428552','425354','428895','430394','430418','431977','431451','431408','431059','430174','428741','432063','429984','426749','422824','428403','427910','424244','421815','432078','432008','428473','427582','428405','427893','427634','429842','424965','430548','426369','422963','422962','432067')
				and sd.store_id in (2019, 2079, 2080, 2082, 2083)
				group by 
					ss.LocationCode,
					cast(dd.actual_date as date),
					convert(varchar, dd.actual_date, 103),
					right((cast('00' as varchar) + cast(td.hour as varchar)),2)
						+ ':' + case when td.Minute < 30 then '00' else '30' end 
			),
		DataStage as
			(
				select 
					ss.LocationCode as StoreCode,
					cast(dd.actual_date as date) as DateRaw,
					convert(varchar, dd.actual_date, 103) as Date,
					right((cast('00' as varchar) + cast(td.hour as varchar)),2)
						+ ':' + case when td.Minute < 30 then '00' else '30' end as Slot,
					case 
						when cast(dd.actual_date as date) >='2023-04-30'
							then 
								case 
									when (tf.isCurbside + tf.isPickUpFromStore + tf.isShipFromStore + tf.SameDayShiptAmount) >0
									then 0
									else sum(tf.Store_transaction_flag) 
								end 
							else sum(tf.Store_transaction_flag) 
					end as SaleTrans,
					case 
						when cast(dd.actual_date as date) >='2023-04-30'
							then 
								case 
									when (tf.isCurbside + tf.isPickUpFromStore + tf.isShipFromStore + tf.SameDayShiptAmount) >0
									then 0
									else sum(tf.store_sales_amount) 
								end 
							else sum(tf.store_sales_amount) 
					end as SaleValue,
					case 
						when cast(dd.actual_date as date) >='2023-04-30'
							then 
								case 
									when (tf.isCurbside + tf.isPickUpFromStore + tf.isShipFromStore + tf.SameDayShiptAmount) >0
									then 0
									else sum(tf.store_units) 
								end 
							else sum(cast(tf.store_units as int)) 
					end as SaleUnits,
					sum(case when tf.returns_UGA = 0 then 0 else 1 end) as RefundTrans,
					sum(tf.returns_UGA) as RefundValue,
					sum(cast(isnull(tff.ReturnUnits,0) as int)) as RefundUnits,
					sum(case when tf.party_flag = 1 then tf.store_sales_amount else 0 end) as PartySaleValue,
					sum(tf.party_master) as PartyTrans,
					sum(isnull(pc.PartyCount,0)) as PartyCount,
					sum(isnull(bp.BackPackTransactions,0)) as BackpackTrans,
					sum(isnull(bp.BackpackUnits,0)) as BackpackUnits,
					sum(case when tf.SFS_TRN_TYP_CD = 0 then 0 else 1 end) as BonusClubTrans,	
					sum(tf.giftcard_UGA) as GiftCardValue,	
					sum(tf.giftcard_units) as GiftCardUnits,	
					sum(tf.enterprise_selling_amount) as EnterpriseSellingValue,	
					sum(tf.enterprise_selling_transaction_count) as EnterpriseSellingTrans,	
					sum(tf.enterprise_selling_units) as EnterpriseSellingUnits,

					sum(tf.ShipFromStoreAmount+tf.SameDayShiptAmount) as ShipFromStoreAmount,
					sum(tf.isShipFromStore+tf.isSameDayShipt) as ShipFromStoreTransactions,
					sum(tf.ShipFromStoreUnits+tf.SameDayShiptUnits) as ShipFromStoreUnits,
					sum(tf.PickupFromStoreAmount) as PickupFromStoreAmount,
					sum(tf.isPickupFromStore) as PickupFromStoreTransactions,
					sum(tf.PickupFromStoreUnits) as PickupFromStoreUnits,
					sum(tf.CurbsideAmount) as CurbsideAmount,
					sum(tf.isCurbside) as CurbsideTransactions,
					sum(tf.CurbsideUnits) as CurbsideUnits,
					sum(crm.MobileCaptureCount) as    MobileCaptureCount,
					sum(crm.MobileEmailOptInCount) as MobileEmailOptInCount
				from vwDW_Transactions_Cube_V3_Dynamics tf 
				join store_dim sd with (nolock) on tf.store_key=sd.store_key
				join dwStaging.dbo.HR_StoreForcePosStoreListStage ss on sd.store_id=ss.StoreID
				join date_dim dd with (nolock) on tf.date_key=dd.date_key
				join time_dim td with (nolock) on tf.time_key=td.time_key
				join TransactionFactsDynamics tff with (nolock) on tf.transaction_id = tff.transaction_id
				left join PartyCounts pc 
					on ss.LocationCode=pc.StoreCode
					and cast(dd.actual_date as date)=pc.RawDate
					and right((cast('00' as varchar) + cast(td.hour as varchar)),2)
						+ ':' + case when td.Minute < 30 then '00' else '30' end = pc.slot

				left join Backpacks bp 
					on ss.LocationCode=bp.StoreCode
					and cast(dd.actual_date as date)=bp.RawDate
					and right((cast('00' as varchar) + cast(td.hour as varchar)),2)
						+ ':' + case when td.Minute < 30 then '00' else '30' end = bp.slot

				left join dwstaging.dbo.HR_StoreforceCustomerMetricsStage crm
					on ss.LocationCode=crm.StoreCode
					and cast(dd.actual_date as date)=crm.TransactionDateRaw
					and right((cast('00' as varchar) + cast(td.hour as varchar)),2)
						+ ':' + case when td.Minute < 30 then '00' else '30' end = crm.slot
				where 
					(datediff(dd, dd.actual_date, getdate())=0
						or 
						(datepart(hh,getdate())<=2 and cast(dd.actual_date as date)=cast(getdate()-1 as date))
					)
					and sd.store_id in (2019, 2079, 2080, 2082, 2083)
				group by 
					ss.LocationCode,
					cast(dd.actual_date as date),
					convert(varchar, dd.actual_date, 103),
					right((cast('00' as varchar) + cast(td.hour as varchar)),2)
						+ ':' + case when td.Minute < 30 then '00' else '30' end,
					tf.isCurbside,
					tf.isPickUpFromStore,
					tf.isShipFromStore,
					tf.SameDayShiptAmount
			)
		select
			sdt.StoreCode,
			sdt.Date,
			sdt.Slot,
			case when sum(isnull(d.SaleTrans,0)) < 0 then 0 else sum(isnull(d.SaleTrans,0)) end SaleTrans,	
			case when sum(isnull(d.SaleValue,0)) < 0 then 0 else sum(isnull(d.SaleValue,0)) end SaleValue,	
			case when sum(isnull(d.SaleUnits,0)) < 0 then 0 else sum(isnull(d.SaleUnits,0)) end SaleUnits,	
			sum(isnull(abs(d.RefundTrans),0)) RefundTrans,
			sum(isnull(abs(d.RefundValue),0)) RefundValue,	
			sum(isnull(abs(d.RefundUnits),0)) RefundUnits,
			sum(isnull(d.PartySaleValue,0)) PartySaleValue,	
			sum(isnull(d.PartyTrans,0)) PartyTrans,	
			sum(isnull(d.PartyCount,0)) PartyCount,	
			sum(isnull(d.BackpackTrans,0)) as BackpackTrans,
			sum(isnull(d.BackpackUnits,0)) as BackpackUnits,
			sum(isnull(d.BonusClubTrans,0)) BonusClubTrans,	
			sum(isnull(d.GiftCardValue,0)) GiftCardValue,	
			sum(isnull(d.GiftCardUnits,0)) GiftCardUnits,	
			sum(isnull(d.EnterpriseSellingValue,0))			EnterpriseSellingValue,	
			sum(isnull(d.EnterpriseSellingTrans,0))			EnterpriseSellingTrans,	
			sum(isnull(d.EnterpriseSellingUnits,0))			EnterpriseSellingUnits,
			sum(isnull(d.ShipFromStoreAmount,0))			ShipFromStoreSales,
			sum(isnull(d.ShipFromStoreTransactions,0))		ShipFromStoreTransactions,
			sum(isnull(d.ShipFromStoreUnits,0))				ShipFromStoreUnits,
			sum(isnull(d.PickupFromStoreAmount,0))			PickupFromStoreSales,
			sum(isnull(d.PickupFromStoreTransactions,0))	PickupFromStoreTransactions,
			sum(isnull(d.PickupFromStoreUnits,0))			PickupFromStoreUnits,
			sum(isnull(d.CurbsideAmount,0))					CurbsideSales,
			sum(isnull(d.CurbsideTransactions,0))			CurbsideTransactions,
			sum(isnull(d.CurbsideUnits,0))					CurbsideUnits,
			sum(isnull(d.MobileCaptureCount,0)) as			MobileCaptureCount,
			sum(isnull(d.MobileEmailOptInCount,0)) as	MobileEmailOptInCount,
			sdt.StoreCodeRaw,
			sdt.RawDate as TransactionDateRaw
		into #MergeStage
		from StoreDateTime sdt
		left join DataStage d 
			on sdt.StoreCode=d.StoreCode
			and sdt.Date=d.Date
			and sdt.Slot=d.Slot
		where sdt.RawDate = cast(getdate() as date)
		group by 
			sdt.StoreCode,
			sdt.Date,
			sdt.Slot,
			sdt.StoreCodeRaw,
			sdt.RawDate

		------
		;

		

		merge into HR_StoreForcePosSalesFact as target
		using #MergeStage as source
		on 
			(
				target.StoreCode=source.StoreCode
				and
				target.Date=source.Date
				and
				target.Slot=source.Slot
			)
		when matched and
			isnull(target.SaleTrans,0)<>isnull(source.SaleTrans,0)
			OR
			isnull(target.SaleValue,0)<>isnull(source.SaleValue,0)
			OR
			isnull(target.SaleUnits,0)<>isnull(source.SaleUnits,0)
			OR
			--isnull(target.RefundTrans,0)<>isnull(source.RefundTrans,0)
			--OR
			--isnull(target.RefundValue,0)<>isnull(source.RefundValue,0)
			--OR
			--isnull(target.RefundUnits,0)<>isnull(source.RefundUnits,0)
			--OR
			isnull(target.PartySaleValue,0)<>isnull(source.PartySaleValue,0)
			OR
			isnull(target.PartyTrans,0)<>isnull(source.PartyTrans,0)
			OR
			isnull(target.PartyCount,0)<>isnull(source.PartyCount,0)
			OR
			isnull(target.BackpackTrans,0)<>isnull(source.BackpackTrans,0)
			OR
			isnull(target.BackpackUnits,0)<>isnull(source.BackpackUnits,0)
			OR
			isnull(target.BonusClubTrans,0)<>isnull(source.BonusClubTrans,0)
			OR
			isnull(target.GiftCardValue,0)<>isnull(source.GiftCardValue,0)
			OR
			isnull(target.GiftCardUnits,0)<>isnull(source.GiftCardUnits,0)
			OR
			isnull(target.EnterpriseSellingValue,0)<>isnull(source.EnterpriseSellingValue,0)
			OR
			isnull(target.EnterpriseSellingTrans,0)<>isnull(source.EnterpriseSellingTrans,0)
			OR
			isnull(target.EnterpriseSellingUnits,0)<>isnull(source.EnterpriseSellingUnits,0)
			or
			isnull(target.ShipFromStoreSales,0)<>isnull(source.ShipFromStoreSales,0)
			or
			isnull(target.ShipFromStoreTransactions,0)<>isnull(source.ShipFromStoreTransactions,0)
			or
			isnull(target.ShipFromStoreUnits,0)<>isnull(source.ShipFromStoreUnits,0)
			or
			isnull(target.PickupFromStoreSales,0)<>isnull(source.PickupFromStoreSales,0)
			or
			isnull(target.PickupFromStoreTransactions,0)<>isnull(source.PickupFromStoreTransactions,0)
			or
			isnull(target.PickupFromStoreUnits,0)<>isnull(source.PickupFromStoreUnits,0)
			or
			isnull(target.CurbsideSales,0)<>isnull(source.CurbsideSales,0)
			or
			isnull(target.CurbsideTransactions,0)<>isnull(source.CurbsideTransactions,0)
			or
			isnull(target.CurbsideUnits,0)<>isnull(source.CurbsideUnits,0)
			or
			isnull(target.MobileCaptureCount,0)<>isnull(source.MobileCaptureCount,0)
			or
			isnull(target.MobileEmailOptInCount,0)<>isnull(source.MobileEmailOptInCount,0)
		then update
			set
				target.SaleTrans=source.SaleTrans,	
				target.SaleValue=source.SaleValue,	
				target.SaleUnits=source.SaleUnits,
			
				target.PartySaleValue=source.PartySaleValue,
				target.PartyTrans=source.PartyTrans,
				target.PartyCount=source.PartyCount,
				target.BackpackTrans=source.BackpackTrans,
				target.BackpackUnits=source.BackpackUnits,
				target.BonusClubTrans=source.BonusClubTrans, 				
				target.GiftCardValue=source.GiftCardValue,
				target.GiftCardUnits=source.GiftCardUnits,
				target.EnterpriseSellingValue=source.EnterpriseSellingValue,
				target.EnterpriseSellingTrans=source.EnterpriseSellingTrans,
				target.EnterpriseSellingUnits=source.EnterpriseSellingUnits,
				target.ShipFromStoreSales=source.ShipFromStoreSales,
				target.ShipFromStoreTransactions=source.ShipFromStoreTransactions,
				target.ShipFromStoreUnits=source.ShipFromStoreUnits,
				target.PickupFromStoreSales=source.PickupFromStoreSales,
				target.PickupFromStoreTransactions=source.PickupFromStoreTransactions,
				target.PickupFromStoreUnits=source.PickupFromStoreUnits,
				target.CurbsideSales=source.CurbsideSales,
				target.CurbsideTransactions=source.CurbsideTransactions,
				target.CurbsideUnits=source.CurbsideUnits,
				target.MobileCaptureCount=source.MobileCaptureCount,
				target.MobileEmailOptInCount=source.MobileEmailOptInCount,
				target.UpdateDate=getdate()
		when not matched by target
			then insert
			(
				StoreCode,
				Date,
				Slot,
				SaleTrans,
				SaleValue,
				SaleUnits,
				RefundTrans,
				RefundValue,
				RefundUnits,
				PartySaleValue,
				PartyTrans,
				PartyBookings,
				PartyCount,
				StufferTrans,
				SkinsTrans,
				StuffersUnits,
				SkinsUnits,
				BackpackTrans,
				BackpackUnits,
				BonusClubTrans,
				GiftCardValue,
				GiftCardUnits,
				EnterpriseSellingValue,
				EnterpriseSellingTrans,
				EnterpriseSellingUnits,
				ShipFromStoreSales,
				ShipFromStoreTransactions,
				ShipFromStoreUnits,
				PickupFromStoreSales,
				PickupFromStoreTransactions,
				PickupFromStoreUnits,
				CurbsideSales,
				CurbsideTransactions,
				CurbsideUnits,
				MobileCaptureCount,
				MobileEmailOptInCount,
				StoreIDRaw,
				DateRaw,
				InsertDate
			)
				values
					(
						source.StoreCode,
						source.Date,
						source.Slot,
						source.SaleTrans,
						source.SaleValue,
						source.SaleUnits,
						source.RefundTrans,
						source.RefundValue,
						source.RefundUnits,
						source.PartySaleValue,
						source.PartyTrans,
						0, --PartyBookings,
						source.PartyCount,
						0, --StufferTrans,
						0,--SkinsTrans,
						0, --StuffersUnits,
						0, --SkinsUnits,
						source.BackpackTrans,
						source.BackpackUnits,
						source.BonusClubTrans,
						source.GiftCardValue,
						source.GiftCardUnits,
						source.EnterpriseSellingValue,
						source.EnterpriseSellingTrans,
						source.EnterpriseSellingUnits,
						source.ShipFromStoreSales,
						source.ShipFromStoreTransactions,
						source.ShipFromStoreUnits,
						source.PickupFromStoreSales,
						source.PickupFromStoreTransactions,
						source.PickupFromStoreUnits,
						source.CurbsideSales,
						source.CurbsideTransactions,
						source.CurbsideUnits,
						source.MobileCaptureCount,
						source.MobileEmailOptInCount,
						source.StoreCodeRaw,
						source.TransactionDateRaw,
						getdate()
					)


		;

END
```

