# ERP.vwDistributionsReleased

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["ERP.vwDistributionsReleased"]
    ERP_DistributionAddressDim(["ERP.DistributionAddressDim"]) --> VIEW
    ERP_DistributionDetail(["ERP.DistributionDetail"]) --> VIEW
    ERP_DistributionHeader(["ERP.DistributionHeader"]) --> VIEW
    ERP_DistributionRectype(["ERP.DistributionRectype"]) --> VIEW
    ERP_FranchiseeLocationMap(["ERP.FranchiseeLocationMap"]) --> VIEW
    ERP_vwWarehouseIDToLocationCode(["ERP.vwWarehouseIDToLocationCode"]) --> VIEW
    WMS_ItemMaster(["WMS.ItemMaster"]) --> VIEW
    WMS_ItemMasterProducts(["WMS.ItemMasterProducts"]) --> VIEW
    WMS_ItemsUOM(["WMS.ItemsUOM"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| ERP.DistributionAddressDim |
| ERP.DistributionDetail |
| ERP.DistributionHeader |
| ERP.DistributionRectype |
| ERP.FranchiseeLocationMap |
| ERP.vwWarehouseIDToLocationCode |
| WMS.ItemMaster |
| WMS.ItemMasterProducts |
| WMS.ItemsUOM |

## View Code

```sql
CREATE view [ERP].[vwDistributionsReleased]

as

------------------------------------------------------------------------------------------------------------------------------------------------

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
				--case when left(d.ITEMNUMBER,1) = 'S' then 'Supply' else 'Merch' end as MerchOrSupply,
				case when im.NecessaryProductionWorkingTimeSchedulingPropertyId  = 'Supplies' then 'Supply'else 'Merch' end as MerchOrSupply,
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
				--case 
				--	when left(im.ProductNumber,1) = 'M'
				--	then 1
				--	else cast(uom.Factor as int)
				--end as DistributionMultiple 
				case 
					--when left(im.ProductNumber,1) = 'M'
					--when it.ItemType = 'Merch' -- Remarked out on 2/5/2020
					when im.NecessaryProductionWorkingTimeSchedulingPropertyId  = 'Merch'
					then 1
					else cast(uom.Factor as int)
				end as DistributionMultiple 
			from 
				ERP.DistributionHeader h with (nolock)
			join ERP.DistributionDetail d with (nolock) on h.OrderID = d.OrderID and h.PickListID = d.PickListID and h.entity = d.entity 
			left join ERP.DistributionRectype rt with (nolock) on rt.RecType = case when isnumeric(isnull(h.ModeOfDelivery,1)) = 0 then 1 else isnull(h.ModeOfDelivery,1) end
			join WMS.ItemMaster im with (nolock) on d.ItemNumber = im.ProductNumber and d.Entity = im.Entity  
				and im.NecessaryProductionWorkingTimeSchedulingPropertyId in ('Merch','Supplies')
			join WMS.ItemMasterProducts p with (nolock) on d.ItemNumber = p.ProductNumber
			left join WMS.ItemsUOM uom with (nolock) 
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
			left join ERP.FranchiseeLocationMap f with (nolock) on h.SHIPTONAME = f.FranchiseeName and h.entity = f.entity 
			where 1=1
			and d.QUANTITY > 0
			and d.ReleaseDate is NOT NULL
			and 
				(
					(left(h.OrderType,8) = 'Transfer' and h.TOWAREHOUSE is not null)
					OR
					(left(h.OrderType,4) = 'Sale' and h.TOWAREHOUSE is null)
				)
			and left(isnull(h.FromWarehouse,666),2) not in ('92','93','94') --excludes various hubs, pool points, etc 
			and isnull(h.FromWarehouse,666) <> '8010' --Keenpac - uk 
			--and h.OrderID = 'TO0000013765' 
	)

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
	row_number() over(partition by OrderID order by OrderID, PicklistID, ToWarehouse, ItemNumber, ModeOfDelivery) as SequenceNumber,
	row_number() over(partition by OrderID order by OrderID, PicklistID, ItemNumber, CustomerRequisitionID) as ref_field_1,
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
```

