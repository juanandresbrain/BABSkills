# ERP.vwShipmentInvoiceStage_Bak20230414

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["ERP.vwShipmentInvoiceStage_Bak20230414"]
    ERP_DistributionDetail(["ERP.DistributionDetail"]) --> VIEW
    erp_DistributionHeader(["erp.DistributionHeader"]) --> VIEW
    erp_ShipmentInvoicePreStage(["erp.ShipmentInvoicePreStage"]) --> VIEW
    ERP_vwWarehouseIDToLocationCode(["ERP.vwWarehouseIDToLocationCode"]) --> VIEW
    wms_ItemMaster(["wms.ItemMaster"]) --> VIEW
    wms_ItemMasterProducts(["wms.ItemMasterProducts"]) --> VIEW
    wms_ItemsUOM(["wms.ItemsUOM"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| ERP.DistributionDetail |
| erp.DistributionHeader |
| erp.ShipmentInvoicePreStage |
| ERP.vwWarehouseIDToLocationCode |
| wms.ItemMaster |
| wms.ItemMasterProducts |
| wms.ItemsUOM |

## View Code

```sql
CREATE view [ERP].[vwShipmentInvoiceStage_Bak20230414] 

as 

with 
ShipmentSource as
	(
		select 
			s.DlvMode,
			s.InventLocationID,
			cast(s.ItemID as varchar(7)) as ItemID,
			s.OrderRef,
			s.CartonNumber,
			s.PalletID,
			case 
				when s.InventLocationID = '9970' 
				then s.QTY * -1
				else s.Qty
			end as Qty,
			s.ShipDate,
			s.ShipTo,
			cast(s.RecType as varchar(8)) as RecType,
			s.Entity 
		from erp.ShipmentInvoicePreStage s 
		where s.InventLocationID NOT in ('1001','1002','1102','1105','1167','1183','1212','1221','1278','1286','1415','1521','1534') -- Pilot Group 1 of Retail Inventory Project
		
	)
select 
	--s.DivMode,
--	isnull(h.MODEOFDELIVERY,1) as DivMode, --I THINK I'LL USE THIS ONE INSTEAD SO IT ALWAYS USES SAME DLVMODE FROM THE HEADER
	h.MODEOFDELIVERY as DivMode,
	s.InventLocationID,
	s.ItemID,
	s.OrderRef,
	s.ShipDate,
	s.CartonNumber,
	s.PalletID,
	cast(s.Qty / isnull(uom.Factor,1) as int) as QTY, --CORRECT
	--s.QTY, --TEMPORARY IF I MANUALLY STAGED INTO PRESTAGE TABLE 
	s.Qty as WhseUnitQty,
	cast(uom.Factor as int) as Factor,
	s.ShipTo,
	s.RecType,
	cast(s.Entity as nvarchar(10)) as Entity,
	case when left(OrderRef,2) = 'SO'
		then d.Warehouse 
		else NULL
	end as UDALocation,
	d.Warehouse
from ShipmentSource s
join erp.DistributionHeader h with (nolock)
	on s.OrderRef = h.OrderID 
	and s.Entity = h.Entity 
join ERP.DistributionDetail d with (nolock) 
	on h.OrderID = d.OrderID 
	and h.PickListID = d.PickListID 
	and h.Entity = d.Entity 
	and s.ItemID = d.ITEMNUMBER 
join wms.ItemMaster im with (nolock) 
	on d.ItemNumber = im.ProductNumber 
	and d.Entity = im.Entity  
join wms.ItemMasterProducts p with (nolock) on d.ItemNumber = p.ProductNumber
left join wms.ItemsUOM uom with (nolock) 
	on d.ItemNumber = uom.ProductNumber
	and d.UOM = uom.FromUnitSymbol
	and d.Entity = uom.Entity
	and uom.ToUnitSymbol = 'wmea'
left join ERP.vwWarehouseIDToLocationCode lc1 with (nolock) on 
			case when left(h.OrderType,8) = 'Transfer'
				then h.FROMWAREHOUSE
				else d.Warehouse 
			 end = lc1.WarehouseID
			 and s.Entity = lc1.Entity 
group by 	
h.MODEOFDELIVERY,
s.InventLocationID,
s.ItemID,
s.OrderRef,
s.ShipDate,
s.CartonNumber,
s.PalletID,
cast(s.Qty / isnull(uom.Factor,1) as int) , --CORRECT
--s.QTY, --TEMPORARY IF I MANUALLY STAGED INTO PRESTAGE TABLE 
s.Qty,
cast(uom.Factor as int),
s.ShipTo,
s.RecType,
cast(s.Entity as nvarchar(10)),
case when left(OrderRef,2) = 'SO'
	then d.Warehouse 
	else NULL
end,
d.Warehouse			

ERP,vwStageDistributionSplit,create view ERP.vwStageDistributionSplit

as

------------------------------------------------------------------------------------------------------------------------------------------------
---- 2017-08-21 -- Dan Tweedie	--	Created view to capture data to stage for distribution split. Data has been pre-staged from Dynamics365 XML
------------------------------------------------------------------------------------------------------------------------------------------------


select 
	h.FromWarehouse as sourceid,
	h.ToWarehouse as destid,
	d.ItemNumber as style_code,
	d.Quantity as quantity,
	h.ModeOfDelivery as rec_type,
	row_number() over(order by h.OrderID, h.ToWarehouse, d.ItemNumber, h.ModeOfDelivery) as sequencenbr,
	h.OrderID as distribution_number,
	row_number() over(order by h.OrderID, d.ItemNumber, h.CustomerRequisitionID) as ref_field_1,
	cast(getdate() as smalldatetime) as release_date,
	0 as active_pick_flag
from ERP.DistributionsFromD365HeaderStage h
join ERP.DistributionsFromD365DetailStage d 
	on h.PickListID = d.PickListID 
	and h.OrderID = d.OrderID
```

