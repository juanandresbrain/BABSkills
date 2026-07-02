# WMS.vwPurchaseOrderDynamicsPOtoAptosPOWithItemNumber

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WMS.vwPurchaseOrderDynamicsPOtoAptosPOWithItemNumber"]
    erp_VendorMaster(["erp.VendorMaster"]) --> VIEW
    WMS_DynamicsAPILog(["WMS.DynamicsAPILog"]) --> VIEW
    WMS_PurchaseOrderMerchToDynamics(["WMS.PurchaseOrderMerchToDynamics"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| erp.VendorMaster |
| WMS.DynamicsAPILog |
| WMS.PurchaseOrderMerchToDynamics |

## View Code

```sql
CREATE view [WMS].[vwPurchaseOrderDynamicsPOtoAptosPOWithItemNumber]
as 
select 
	e.PONumber as AptosPONumber, 
	case 
		when substring(api.ResponseBody, charindex('Purchase order PO', api.ResponseBody, 1)+15, 11) like 'PO%'
			then substring(api.ResponseBody, charindex('Purchase order PO', api.ResponseBody, 1)+15, 11)
		else NULL
	end as DynamicsPO,
	e.VendorCode,
	e.FactoryCode,
	vm.VendorAccountNumber,
	max(cast(ExportedToDynamicsDate as date)) as LastExportDate,
	e.ItemNumber
from WMS.PurchaseOrderMerchToDynamics e with (nolock)
join erp.VendorMaster vm with (nolock) 
	on vm.Entity = e.company
	and cast(e.VendorCode as nvarchar) =
		case 
			when vm.OrganizationPhoneticName like '%-%' 
			then substring(vm.OrganizationPhoneticName, 1, charindex('-',vm.OrganizationPhoneticName)-1) 
			else vm.OrganizationPhoneticName 
		end
	and e.FactoryCode =
		case 
			when vm.OrganizationPhoneticName like '%-%' 
			then substring(vm.OrganizationPhoneticName, charindex('-',vm.OrganizationPhoneticName)+1, 20) 
			else e.FactoryCode
		end
join WMS.DynamicsAPILog api with (nolock)
	on api.IntegrationName='WMS_PurchaseOrderToDynamics'
	and e.BatchID=api.BatchID
	and e.PONumber=api.AptosDocumentNumber 
	and vm.VendorAccountNumber=api.PO_OrderAccountNumber
where api.ResponseBody NOT like '%hasErrors":true%'
group by 
	e.PONumber, 
	case 
		when substring(api.ResponseBody, charindex('Purchase order PO', api.ResponseBody, 1)+15, 11) like 'PO%'
			then substring(api.ResponseBody, charindex('Purchase order PO', api.ResponseBody, 1)+15, 11)
		else NULL
	end,
	e.VendorCode,
	e.FactoryCode,
	vm.VendorAccountNumber,
	e.ItemNumber
```

