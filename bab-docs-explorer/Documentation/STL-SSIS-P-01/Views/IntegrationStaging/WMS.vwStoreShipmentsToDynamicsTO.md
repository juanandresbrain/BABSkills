# WMS.vwStoreShipmentsToDynamicsTO

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WMS.vwStoreShipmentsToDynamicsTO"]
    WMS_StoreShipmentExport(["WMS.StoreShipmentExport"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WMS.StoreShipmentExport |

## View Code

```sql
CREATE view [WMS].[vwStoreShipmentsToDynamicsTO]

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
	Company
from WMS.StoreShipmentExport 
where 1=1
and OrderType='TransferOrder'
and ExportDate is null
--and datediff(dd, ExportDate, getdate()) = 0
```

