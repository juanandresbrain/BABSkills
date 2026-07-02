# WMS.spMergeInboundShipmentLoad_Bak20231030

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WMS.spMergeInboundShipmentLoad_Bak20231030"]
    WMS_InboundShipmentLoad(["WMS.InboundShipmentLoad"]) --> SP
    wms_InboundShipmentLoadStage(["wms.InboundShipmentLoadStage"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WMS.InboundShipmentLoad |
| wms.InboundShipmentLoadStage |

## Stored Procedure Code

```sql
CREATE proc [WMS].[spMergeInboundShipmentLoad_Bak20231030]

as

------------------------------------------------------------------------------------------------------------------------------------------------------------
----	Tim Callahan	-2022-06-03	- Created Proc - Merges Warehouse Shipment Invoice data from WMS.InboundShipmentLoadStage to WMS.InboundShipmentLoad
----	Tim Callahan	-2022-11-21	- Updated Proce - Updated Source as we need to include a new field per JIRA BIB-474
------------------------------------------------------------------------------------------------------------------------------------------------------------

--set nocount on

Merge into WMS.InboundShipmentLoad as target
--using WMS.InboundShipmentLoadStage  as source
using
(
	select ShipDate, 
	--ExpectedReceiptDate, 
	isnull(ExpectedReceiptDate, cast (getdate()+7 as date)) as ExpectedReceiptDate,
	DeliveryTerms, 
	ItemNumber, 
	TransferQuantity, 
	UOM, 
	BABAptosDistroNumber, 
	InventoryStatus, 
	LicensePlate, 
	ContainerID, 
	[3PLDocumentNumber], 
	OrderCreateSource, 
	Entity, 
	FromWarehouse, 
	ToWarehouse, 
	AptosShipmentNumber, 
	ModeOfDelivery, 
	OrderId, 
	BABAptosDistroLineNumber, 
	case when FromWarehouse = '9960' and Entity = '1100'
		then 'SWC'+[OrderId]
		when FromWarehouse = '9970' and Entity = '2110'
			then 'SUK' +[OrderId]
		else null 
		end as ParentLicensePlate

	from wms.InboundShipmentLoadStage
	group by ShipDate, 
	--ExpectedReceiptDate, 
	isnull(ExpectedReceiptDate, cast (getdate()+7 as date)),
	DeliveryTerms, 
	ItemNumber, 
	TransferQuantity, 
	UOM, 
	BABAptosDistroNumber, 
	InventoryStatus, 
	LicensePlate, 
	ContainerID, 
	[3PLDocumentNumber], 
	OrderCreateSource, 
	Entity, 
	FromWarehouse, 
	ToWarehouse, 
	AptosShipmentNumber, 
	ModeOfDelivery, 
	OrderId, 
	BABAptosDistroLineNumber

) as source 
on 
	(
		isnull(target.ToWarehouse,'x') = isnull(source.ToWarehouse,'x')
		and
		isnull(target.OrderId,'x') = isnull(source.OrderId,'x')
		and
		isnull(target.LicensePlate,'x') = isnull(source.LicensePlate,'x')
		and
		isnull(target.ItemNumber,'x') = isnull(source.ItemNumber,'x')
		and 
		isnull(target.Entity,'x') = isnull(source.Entity,'x')
		and 
		isnull(target.ContainerId,'x')=isnull(source.ContainerId,'x')

	)
when NOT MATCHED by Target
	then
		Insert
			(
				ShipDate, 
				ExpectedReceiptDate, 
				AptosShipmentNumber, 
				DeliveryTerms, 
				ModeOfDelivery, 
				ToWarehouse, 
				FromWarehouse, 
				Entity, 
				OrderId, 
				ItemNumber, 
				TransferQuantity, 
				UOM, 
				BABAptosDistroNumber, 
				BABAptosDistroLineNumber, 
				InventoryStatus, 
				LicensePlate, 
				ContainerId, 
				InsertDate, 
				[3PLDocumentNumber],
				OrderCreateSource, 
				ParentLicensePlate

			)
		values
			(
				source.ShipDate, 
				source.ExpectedReceiptDate, 
				source.AptosShipmentNumber, 
				source.DeliveryTerms, 
				source.ModeOfDelivery, 
				source.ToWarehouse, 
				source.FromWarehouse, 
				source.Entity, 
				source.OrderId, 
				source.ItemNumber, 
				source.TransferQuantity, 
				source.UOM, 
				source.BABAptosDistroNumber, 
				source.BABAptosDistroLineNumber, 
				source.InventoryStatus, 
				source.LicensePlate, 
				source.ContainerId,
				getdate(), 
				source.[3PLDocumentNumber],
				source.OrderCreateSource, 
				source.ParentLicensePlate
				
				)


;
```

