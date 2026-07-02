# ERP.vwItemFactoryCN

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["ERP.vwItemFactoryCN"]
    erp_PurchaseOrderHeader(["erp.PurchaseOrderHeader"]) --> VIEW
    erp_PurchaseOrderLines(["erp.PurchaseOrderLines"]) --> VIEW
    erp_VendorMaster(["erp.VendorMaster"]) --> VIEW
    erp_vwFactoryAddress(["erp.vwFactoryAddress"]) --> VIEW
    WMS_ItemMaster(["WMS.ItemMaster"]) --> VIEW
    WMS_ItemMasterProducts(["WMS.ItemMasterProducts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| erp.PurchaseOrderHeader |
| erp.PurchaseOrderLines |
| erp.VendorMaster |
| erp.vwFactoryAddress |
| WMS.ItemMaster |
| WMS.ItemMasterProducts |

## View Code

```sql
CREATE view [ERP].[vwItemFactoryCN] 

as


with 
PO as
	(
		select 
			ph.Entity, 
			max(ph.PurchaseOrderNumber) PurchaseOrderNumber,
			pl.ItemID
		from erp.PurchaseOrderHeader ph with(nolock)
		join erp.PurchaseOrderLines pl with(nolock) 
			on ph.entity = pl.entity 
			and ph.PurchaseOrderNumber = pl.PurchaseOrderNumber
		group by ph.Entity, pl.ItemID 
	),
VendorAccount as 
	(
		select distinct poh.ShipFromID as VendorAccountNumber, po.ItemID, poh.Entity 
		from erp.PurchaseOrderHeader poh with(nolock)
		join PO 
			on poh.Entity = PO.Entity 
			and poh.PurchaseOrderNumber = PO.PurchaseOrderNumber
	),
FactoryCountry as
	(
		select distinct	
			va.Entity, 
			p.ProductNumber,
			case 
				when fa.country = 'P.R. of China'
					then 'CN'
				when fa.country = 'Vietnam'
					then 'VN'
				when fa.country = 'Indonesia'
					then 'ID'
				else isnull(fa.country, 'CN')
			end as FactoryCountry
			,v.VendorAccountNumber 
		from VendorAccount va
		join erp.VendorMaster v with(nolock) 
			on va.entity = v.entity 
			and va.VendorAccountNumber = v.VendorAccountNumber
		join WMS.ItemMasterProducts p with(nolock) 
			on va.ItemID = p.PRODUCTNUMBER
		join WMS.ItemMaster i with(nolock)
			on va.ItemID = i.PRODUCTNUMBER
		left join erp.vwFactoryAddress fa 
			on v.entity = fa.Entity 
			and v.VendorAccountNumber = fa.VendorAccount 
		where left(p.ProductNumber, 1) in ('0','8','9')
		 and i.NecessaryProductionWorkingTimeSchedulingPropertyId = 'Merch'
	)
select 
	Entity,
	ProductNumber,
	VendorAccountNumber
from FactoryCountry
```

