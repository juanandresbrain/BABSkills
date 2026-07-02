# WMS.vwStoreShipmentsToDynamicsTOBAK20220801

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WMS.vwStoreShipmentsToDynamicsTOBAK20220801"]
    WMS_StoreShipmentExport(["WMS.StoreShipmentExport"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WMS.StoreShipmentExport |

## View Code

```sql
CREATE view [WMS].[vwStoreShipmentsToDynamicsTOBAK20220801]

as
--------------------------------------------------------------------------------------------------------------------------
--	Dan Tweedie	- 2019-08-02	Used in SSIS as data source to push staged distros to Dynamics WMS for US locations. 
--------------------------------------------------------------------------------------------------------------------------

select 
	convert(varchar(10), ShipDate,101) as ShipDate,
	convert(varchar(10), ReceiptDate,101) as ReceiptDate,
	AptosShipmentNumber	as BABAptosShipmentNumber,
	DeliveryTerms,
	ModeOfDelivery,	
	ToWarehouse,
	FromWarehouse,
	ItemNumber,	
	AptosDistroNumber as BABAptosDistroNumber,
	AptosDistroLineNumber as BABAptosDistroLineNumber,
	quantity,	
	UnitOfMeasure as UOM,	
	InventoryStatus,
	case 
		when FromWarehouse in ('9980','9960','8175') then '1100'
		when FromWarehouse in ('2970') then '2110'
	end as Company

from WMS.StoreShipmentExport 
where 1=1
and CountryCode = 'US'
and ExportDate is null
--and datediff(dd, InsertDate, getdate()) = 0
```

