# WMS.spMergePurchaseOrderReceiptFromDynamicsReceiptHeaderAndLineBAK20220801

**Database:** IntegrationStaging  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WMS.spMergePurchaseOrderReceiptFromDynamicsReceiptHeaderAndLineBAK20220801"]
    erp_vwWarehouseIDToLocationCode(["erp.vwWarehouseIDToLocationCode"]) --> SP
    WMS_PurchaseOrderReceipt(["WMS.PurchaseOrderReceipt"]) --> SP
    wms_vwDynamicsPurchaseOrderReceipts(["wms.vwDynamicsPurchaseOrderReceipts"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| erp.vwWarehouseIDToLocationCode |
| WMS.PurchaseOrderReceipt |
| wms.vwDynamicsPurchaseOrderReceipts |

## Stored Procedure Code

```sql
create proc [WMS].[spMergePurchaseOrderReceiptFromDynamicsReceiptHeaderAndLineBAK20220801]

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--	Dan Tweedie	2019-07-02	Created proc to merge new WMS PO Receipt messages from Azure Service Bus so we can post to Aptos / Merch system
--							Updated messages are not allowed, only new messages based on the AptosPONumber, POLineNumber, ItemID, MessageID, MessageSequence, MessageRowIndex
--							Data will be pushed to Aptos / Merch via a different process 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

as 

set nocount on 


select 
	pr.AptosPOnumber,
	pr.AptosPOShipmentLineNumber as POLineNumber,
	pr.ItemNumber as ItemID,
	sum(pr.ReceivedPurchaseQuantity) as ReceivedQty,
	0 as CanceledQty,
	w.LocationCode as Warehouse,
	--pr.ReceivingWarehouseID as Warehouse,
	isnull(pr.ProductReceiptNumber, 'NO ASN') as ASN,
	cast(pr.ProductReceiptDate as datetime) as MessageQueueDateUTC,
	NULL as MessageID,
	NULL as MessageSequence,
	NULL as MessageRowIndex
into #tmp
from wms.vwDynamicsPurchaseOrderReceipts pr
join erp.vwWarehouseIDToLocationCode w on pr.ReceivingWarehouseID=w.WarehouseID
where pr.ReceivingWarehouseID='9980'
and pr.AptosPOnumber is not null
and cast(pr.ProductReceiptDate as date) > '2022-06-22' --controlled start date
group by 
	pr.AptosPONumber,
	pr.AptosPOShipmentLineNumber,
	pr.ItemNumber,
	w.LocationCode,
	pr.ReceivingWarehouseID,
	pr.ProductReceiptNumber,
	cast(pr.ProductReceiptDate as datetime)



merge into WMS.PurchaseOrderReceipt as target 
using #tmp as source
	on 
		target.AptosPONumber=source.AptosPONumber
		and
		target.POLineNumber=source.POLineNumber
		and 
		target.ItemID=source.ItemID
		and 
		isnull(target.ASN,'NO ASN')=isnull(source.ASN, 'NO ASN')
		
when not matched by target
then
	insert
		(
			AptosPONumber,
			POLineNumber,
			ItemID,
			ReceivedQty,
			CanceledQty,
			Warehouse,
			ASN,
			MessageQueueDateUTC,
			--MessageID,
			--MessageSequence,
			--MessageRowIndex,
			InsertDate
		)
	values
		(
			source.AptosPONumber,
			source.POLineNumber,
			source.ItemID,
			source.ReceivedQty,
			source.CanceledQty,
			source.Warehouse,
			isnull(source.ASN, 'NO ASN'),
			source.MessageQueueDateUTC,
			--source.MessageID,
			--source.MessageSequence,
			--source.MessageRowIndex,
			getdate()
		)
when matched
and 
	isnull(target.ReceivedQty,0)<>isnull(source.ReceivedQty,0)
then update
	set
		target.ReceivedQty=source.ReceivedQty
;
```

