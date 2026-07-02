# WMS.vwASNtoDynamicsAPI_BAK_20230411

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WMS.vwASNtoDynamicsAPI_BAK_20230411"]
    erp_PurchaseOrderHeader(["erp.PurchaseOrderHeader"]) --> VIEW
    erp_VendorMaster(["erp.VendorMaster"]) --> VIEW
    ERP_vwItemMasterUOM(["ERP.vwItemMasterUOM"]) --> VIEW
    WMS_ASN_TPMToDynamics(["WMS.ASN_TPMToDynamics"]) --> VIEW
    WMS_PurchaseOrderMerchToDynamics(["WMS.PurchaseOrderMerchToDynamics"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| erp.PurchaseOrderHeader |
| erp.VendorMaster |
| ERP.vwItemMasterUOM |
| WMS.ASN_TPMToDynamics |
| WMS.PurchaseOrderMerchToDynamics |

## View Code

```sql
CREATE view [WMS].[vwASNtoDynamicsAPI_BAK_20230411] 

as


with 
POVendorAccount as
	(
		select 
			po.PONumber,
			po.POLineNumber,
			vm.VendorAccountNumber,
			vm.InvoiceVendorAccountNumber
		from WMS.PurchaseOrderMerchToDynamics po with (nolock)
		join erp.VendorMaster vm with (nolock) 
--			on vm.Entity = --1200
			on vm.Entity = 
				case when exists 
					(
						select d.PONumber 
						from WMS.PurchaseOrderMerchToDynamics d with (nolock)
						where cast(d.InsertDate as date) < '2021-06-28'--- FIRST DAY OF ECO -- 
						and d.PONumber = po.PONumber
						and d.POLineNumber=po.POLineNumber
						--and d.PONumber not in  ('1077701') -- Only use for Ad Hoc Exporting
					) then 1200
				else po.Company
			end
			and cast(po.VendorCode as nvarchar) =
				case 
					when vm.OrganizationPhoneticName like '%-%' 
					then substring(vm.OrganizationPhoneticName, 1, charindex('-',vm.OrganizationPhoneticName)-1) 
					else vm.OrganizationPhoneticName 
				end
			and po.FactoryCode =
				case 
					when vm.OrganizationPhoneticName like '%-%' 
					then substring(vm.OrganizationPhoneticName, charindex('-',vm.OrganizationPhoneticName)+1, 20) 
					else po.FactoryCode
				end
	),
VendorAccountForDynamicsPO as
	(
		select 
			h.PurchaseOrderNumber as PONumber,
			h.shipfromid as VendorAccountNumber
		from erp.PurchaseOrderHeader h with (nolock)
	),
Summary as
	(
		select 
			a.shipment,	
			a.lpn,	
			a.ItemId,	
			a.PO_nbr,	
			cast(a.Po_Shipment_Line_nbr as int) as Po_Shipment_Line_nbr,	
			cast(a.Qty as int) as Qty,
			cast(a.Unit as nvarchar(10)) as Unit,	
			v.VendorAccountNumber,
			NULL as DynamicsPORefNum,
			concat(a.shipment, '_', v.VendorAccountNumber) as ShipmentVendor
		from WMS.ASN_TPMToDynamics a
		join POVendorAccount v 
			on a.po_nbr=v.PONumber
			and a.Po_Shipment_Line_nbr=v.POLineNumber
		where 1=1
		and a.SentTo365 is NULL
		--and a.lpn <> '0023373541'
		--and Shipment = 'SH0000033929'
		UNION
		select 
			a.shipment,	
			a.lpn,	
			a.ItemId,	
			Null as PO_nbr,	
			cast(a.Po_Shipment_Line_nbr as int) as Po_Shipment_Line_nbr,	
			(cast(a.Qty as int) / iUOM.PurchaseMultiple) as Qty,
			cast(iuom.PurchaseUnitSymbol as nvarchar(10)) as Unit,	
			NULL as VendorAccountNumber,
			a.PO_nbr as DynamicsPORefNum,
			concat(a.shipment, '_') as ShipmentVendor
		from WMS.ASN_TPMToDynamics a
		join VendorAccountForDynamicsPO v 
			on a.po_nbr=v.PONumber
		join ERP.vwItemMasterUOM iUOM with (nolock) on a.ItemID = iUOM.ProductNumber and iUOM.Entity=1100
		where 1=1
		and a.SentTo365 is NULL
		--and a.lpn <> '0023373541'
		--and Shipment = 'SH0000033929'
	)
select s.*
from Summary s
```

