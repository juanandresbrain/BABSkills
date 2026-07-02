# ERP.vwDistributionsReadyToReleaseDevTest

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["ERP.vwDistributionsReadyToReleaseDevTest"]
    dbo_distribution_split(["dbo.distribution_split"]) --> VIEW
    ERP_DistributionAddressDim(["ERP.DistributionAddressDim"]) --> VIEW
    ERP_DistributionDetail(["ERP.DistributionDetail"]) --> VIEW
    ERP_DistributionHeader(["ERP.DistributionHeader"]) --> VIEW
    ERP_DistributionRectype(["ERP.DistributionRectype"]) --> VIEW
    ERP_FranchiseeLocationMap(["ERP.FranchiseeLocationMap"]) --> VIEW
    ERP_ItemMaster(["ERP.ItemMaster"]) --> VIEW
    ERP_ItemMasterProducts(["ERP.ItemMasterProducts"]) --> VIEW
    ERP_ItemsUOM(["ERP.ItemsUOM"]) --> VIEW
    ERP_vwWarehouseIDToLocationCode(["ERP.vwWarehouseIDToLocationCode"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.distribution_split |
| ERP.DistributionAddressDim |
| ERP.DistributionDetail |
| ERP.DistributionHeader |
| ERP.DistributionRectype |
| ERP.FranchiseeLocationMap |
| ERP.ItemMaster |
| ERP.ItemMasterProducts |
| ERP.ItemsUOM |
| ERP.vwWarehouseIDToLocationCode |

## View Code

```sql
CREATE view [ERP].[vwDistributionsReadyToReleaseDevTest]

as

------------------------------------------------------------------------------------------------------------------------------------------------
---- 2017-08-21 -- Dan Tweedie	--	Created view to capture data to stage for distribution split. Data has been pre-staged from Dynamics365 XML
--	2018-10-12 -- Dan Tweedie	-- Updated view to exclude rows where the count of rows returned would exceed the count of rows staged, which would be caused by duplicate dimension data causing the joins to return additional rows than intended

------------------------------------------------------------------------------------------------------------------------------------------------
With 
DistroData as 
	(
			select DISTINCT 
				h.Entity,
				h.PICKLISTID,
				h.CUSTOMERREQUISITIONID,
				h.DELIVERYTERM,
				cast(lc1.OperationalSiteCode as varchar(10)) as FROMWAREHOUSE,
				case when isnumeric(isnull(h.ModeOfDelivery,1)) = 0 then 1 else isnull(h.ModeOfDelivery,1) end as MODEOFDELIVERY,
				CAST(h.ORDERID as varchar(12)) AS ORDERID,
				h.ORDERTYPE,
				h.SHIPTONAME,
				
				CASE 
					WHEN h.ORDERTYPE = 'Sales' and f.LocationCode is not null  ---SALES ORDER FOR FRANCHISEE LOCATION THAT IS MAPPED IN ERP.FranchiseeLocationMap, CAME FROM RON TO TELL US LOCATION CODES FOR FRANCHISEES AS THEY ARE NOT IN DYNAMICS AS WAREHOUSE/SITE
						THEN f.LocationCode
					else 
							----ORIGNAL CASE STATEMENT
							cast(
									case when lc4.OperationalSiteCode is not null
										then cast(lc4.OperationalSiteCode as varchar)
										else
											case 
												when lc2.OperationalSiteCode is not null 
													then cast(lc2.OperationalSiteCode as varchar)
													else isnull(cast(a.location_code as varchar), cast(a.AddressID as varchar) )
											end
									 end 
								 as varchar(10))
				END as TOWAREHOUSE,
				h.TRANSACTIONDATETIME,
				d.ITEMDESCRIPTION,
				case when left(d.ITEMNUMBER,1) = 'S' then 'Supply' else 'Merch' end as MerchOrSupply,
				cast(right(d.ITEMNUMBER,6) as varchar(20)) as ITEMNUMBER,
				D.QUANTITY,
				cast( isnull(uom.Factor,1) * d.Quantity as int) as ConvertedQuantity,
				d.QUANTITYUNITOFMEASURE,
				d.SALESPRICE,
				isnull(rt.RecType,1) as RecType,
				rt.ReasonCode,
				rt.Priority,
				upper(datename(dw,getdate())) as current_day,
				a.AddressID OrderAddressID,
				a.location_code OrderLocationCode,
				case when lc4.WarehouseID is null 
					then 0
					else 1
				end as SaleToStore,
				---next 4 fields are for use in the 3pl files
				cast(right(d.ITEMNUMBER,6) as varchar(6)) as VendorStyle,
				'00' as ColorCode,
				cast(p.PRODUCTDESCRIPTION as varchar(52)) as ShortDesription,
				case 
					when left(im.ProductNumber,1) = 'M'
					then 1
					else cast(uom.Factor as int)
				end as DistributionMultiple 
			from 
				ERP.DistributionHeader h
			join ERP.DistributionDetail d on h.OrderID = d.OrderID and h.PickListID = d.PickListID and h.entity = d.entity 
			left join ERP.DistributionRectype rt on rt.RecType = case when isnumeric(isnull(h.ModeOfDelivery,1)) = 0 then 1 else isnull(h.ModeOfDelivery,1) end
			join ERP.ItemMaster im with (nolock)  on d.ItemNumber = im.ProductNumber and d.Entity = im.Entity  
			join ERP.ItemMasterProducts p with (nolock) on d.ItemNumber = p.ProductNumber
			left join ERP.ItemsUOM uom with (nolock) 
				on d.ItemNumber = uom.ProductNumber
				and d.UOM = uom.FromUnitSymbol
				and d.Entity = uom.Entity
				and uom.ToUnitSymbol = 'wmea'
			left join ERP.vwWarehouseIDToLocationCode lc1 with (nolock) on 
						case when left(h.OrderType,8) = 'Transfer'
							then h.FROMWAREHOUSE
							else d.Warehouse 
						 end = lc1.WarehouseID
						 and h.Entity = lc1.Entity 
			left join ERP.vwWarehouseIDToLocationCode lc2 with (nolock) on 
						case when left(h.OrderType,8) = 'Transfer'
							then cast(h.ToWAREHOUSE as varchar(5))
							else cast(d.Location as varchar(5))
						 end = cast(lc2.WarehouseID as varchar(5))
						 and h.Entity = lc2.Entity 
			left join ERP.DistributionAddressDim a with (nolock) on h.SHIPTONAME = a.SHIPTONAME
			left join ERP.vwWarehouseIDToLocationCode lc3 with (nolock) on lc2.LocationCode = replace(lc3.WarehouseID, '-','') and h.Entity = lc3.Entity 
			left join ERP.vwWarehouseIDToLocationCode lc4 with (nolock) on h.ShipToName = lc4.PrimaryAddressDescription and left(h.OrderType,5) = 'Sales' and h.Entity = lc4.Entity -- SALES ORDERS TO CANADA STORES..
			left join ERP.FranchiseeLocationMap f on h.SHIPTONAME = f.FranchiseeName and h.entity = f.entity 
			where 1=1
			and d.QUANTITY > 0
			and h.ReleaseDate is NULL
			and left(im.ItemNumber, 1) in ('M', 'S')
			and 
				(
					(left(h.OrderType,8) = 'Transfer' and h.TOWAREHOUSE is not null)
					OR
					(left(h.OrderType,4) = 'Sale' and h.TOWAREHOUSE is null)
				)
			and left(isnull(h.FromWarehouse,666),2) not in ('92','93','94') --excludes various hubs, pool points, etc 
			and isnull(h.FromWarehouse,666) <> '8010' --Keenpac - uk 
			--and h.OrderID = 'TO0000013765' 
	),
DistroRawCounts as
	(
		select h.Entity, h.OrderID, count(*) Rowz
		from 
			ERP.DistributionHeader h
		join ERP.DistributionDetail d on h.OrderID = d.OrderID and h.PickListID = d.PickListID and h.entity = d.entity 
		where 1=1
			and d.QUANTITY > 0
			and d.ReleaseDate is NULL
			and 
				(
					(left(h.OrderType,8) = 'Transfer' and h.TOWAREHOUSE is not null)
					OR
					(left(h.OrderType,4) = 'Sale' and h.TOWAREHOUSE is null)
				)
			and left(isnull(h.FromWarehouse,666),2) not in ('92','93','94') --excludes various hubs, pool points, etc 
			and isnull(h.FromWarehouse,666) <> '8010' --Keenpac - uk 
			and h.OrderID in (select OrderID from DistroData)
		group by h.Entity, h.OrderID 
	),
DistroDataCounts as
	(
		select Entity, OrderID, count(*) Rowz
		from DistroData 
		group by Entity, OrderID

	),
CountExceptions as
	(
		select r.Entity, r.OrderID, r.Rowz RawCount, dd.Rowz ExportCount
		from DistroRawCounts r 
		join DistroDataCounts dd 
			on r.entity =dd.entity 
			and r.OrderID = dd.OrderID 
			and r.Rowz <> dd.Rowz
	),
DistroStage as
	(
		select  
			Entity,
			PICKLISTID,
			CUSTOMERREQUISITIONID,
			DELIVERYTERM,
			FROMWAREHOUSE,
			MODEOFDELIVERY,
			ORDERID,
			ORDERTYPE,
			SHIPTONAME,
			TOWAREHOUSE,
			TRANSACTIONDATETIME,
			ITEMDESCRIPTION,
			MerchOrSupply,
			ITEMNUMBER,
			QUANTITY,
			ConvertedQuantity,
			QUANTITYUNITOFMEASURE,
			SALESPRICE,
			RecType as RecType,
			ReasonCode,
			Priority,
			row_number() over(order by OrderID, PicklistID, ToWarehouse, ItemNumber, ModeOfDelivery) as SequenceNumber,
			row_number() over(order by OrderID, PicklistID, ItemNumber, CustomerRequisitionID) as ref_field_1,
			current_day,
			OrderAddressID,
			OrderLocationCode,
			SaleToStore,
			VendorStyle,
			ColorCode,
			ShortDesription,
			DistributionMultiple 
		from DistroData
		where TOWAREHOUSE is NOT NULL
		AND isnull(TOWAREHOUSE,'x') <> isnull(FROMWAREHOUSE,'x')
		AND
						(
							(isnull(RecType,1) >= 50 or (left(OrderType,4) = 'Sale' AND SaleToStore = 0)) --EITHER RECTYPE >= 50 OR IS A SALE THAT IS NOT TO CANADIAN STORE
							or		
							(
								isnull(RecType,1) < 50 
								and 
								datepart(hh,getdate()) >= case when FROMWAREHOUSE = '3970' then 15 else 18 end
							)
							--OR OrderID in ('TO0000016280','TO0000016279')
						)
		),
MaxSequence as
	(
		select 
			cast(case 
				when sourceid in ('0980', '0960') then 1100
				when sourceid in ('2970') then 2100
				when sourceid in ('3970', '8502') then 3001
			end as nvarchar(4)) as Entity, 
			distribution_number, 
			max(sequencenbr) MaxSequence
		from bedrockdb02.me_01.dbo.distribution_split with (nolock)
		where distribution_number in (select OrderID from DistroStage)
		group by 
			case 
				when sourceid in ('0980', '0960') then 1100
				when sourceid in ('2970') then 2100
				when sourceid in ('3970', '8502') then 3001
			end, 
			distribution_number
	)
select 
	ds.Entity,
	ds.PICKLISTID,
	ds.CUSTOMERREQUISITIONID,
	ds.DELIVERYTERM,
	ds.FROMWAREHOUSE,
	ds.MODEOFDELIVERY,
	ds.ORDERID,
	ds.ORDERTYPE,
	ds.SHIPTONAME,
	ds.TOWAREHOUSE,
	ds.TRANSACTIONDATETIME,
	ds.ITEMDESCRIPTION,
	ds.MerchOrSupply,
	ds.ITEMNUMBER,
	sum(ds.QUANTITY) QUANTITY,
	SUM(ds.ConvertedQuantity) ConvertedQuantity,
	ds.QUANTITYUNITOFMEASURE,
	ds.SALESPRICE,
	ds.RecType,
	ds.ReasonCode,
	ds.Priority,
	case 
		when ms.MaxSequence is NOT NULL 
			then ms.MaxSequence + ds.SequenceNumber
		else ds.SequenceNumber
	end as SequenceNumber,
	ds.ref_field_1,
	ds.current_day,
	ds.OrderAddressID,
	ds.OrderLocationCode,
	ds.SaleToStore,
	ds.VendorStyle,
	ds.ColorCode,
	ds.ShortDesription,
	ds.DistributionMultiple 
from DistroStage ds
left join MaxSequence ms 
	on ds.Entity = ms.Entity
	and ds.OrderID = ms.distribution_number  
group by 
	ds.Entity,
	ds.PICKLISTID,
	ds.CUSTOMERREQUISITIONID,
	ds.DELIVERYTERM,
	ds.FROMWAREHOUSE,
	ds.MODEOFDELIVERY,
	ds.ORDERID,
	ds.ORDERTYPE,
	ds.SHIPTONAME,
	ds.TOWAREHOUSE,
	ds.TRANSACTIONDATETIME,
	ds.ITEMDESCRIPTION,
	ds.MerchOrSupply,
	ds.ITEMNUMBER,
	ds.QUANTITYUNITOFMEASURE,
	ds.SALESPRICE,
	ds.RecType,
	ds.ReasonCode,
	ds.Priority,
	case 
		when ms.MaxSequence is NOT NULL 
			then ms.MaxSequence + ds.SequenceNumber
		else ds.SequenceNumber
	end,
	ds.ref_field_1,
	ds.current_day,
	ds.OrderAddressID,
	ds.OrderLocationCode,
	ds.SaleToStore,
	ds.VendorStyle,
	ds.ColorCode,
	ds.ShortDesription,
	ds.DistributionMultiple
```

