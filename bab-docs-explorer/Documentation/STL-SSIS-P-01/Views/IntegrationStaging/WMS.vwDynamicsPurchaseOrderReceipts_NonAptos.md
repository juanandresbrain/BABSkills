# WMS.vwDynamicsPurchaseOrderReceipts_NonAptos

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WMS.vwDynamicsPurchaseOrderReceipts_NonAptos"]
    WMS_DynamicsProductReceiptHeaderStage(["WMS.DynamicsProductReceiptHeaderStage"]) --> VIEW
    WMS_DynamicsProductReceiptLineStage(["WMS.DynamicsProductReceiptLineStage"]) --> VIEW
    wms_ItemMaster(["wms.ItemMaster"]) --> VIEW
    wms_ItemMasterProducts(["wms.ItemMasterProducts"]) --> VIEW
    WMS_vwPurchaseOrderDynamicsPOtoAptosPO(["WMS.vwPurchaseOrderDynamicsPOtoAptosPO"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WMS.DynamicsProductReceiptHeaderStage |
| WMS.DynamicsProductReceiptLineStage |
| wms.ItemMaster |
| wms.ItemMasterProducts |
| WMS.vwPurchaseOrderDynamicsPOtoAptosPO |

## View Code

```sql
CREATE view [WMS].[vwDynamicsPurchaseOrderReceipts_NonAptos]

as 

with POMap as
	(
		select 
			AptosPONumber,
			Dynamics1100PO,
			VendorAccountNumber
		from WMS.vwPurchaseOrderDynamicsPOtoAptosPO
		group by 
			AptosPONumber,
			Dynamics1100PO,
			VendorAccountNumber
	)
select 
	prh.PurchaseOrderNumber,	
	pom.AptosPONumber,
	cast(prh.ProductReceiptDate as date) as ProductReceiptDate,
	prl.LineNumber,	
	prl.PurchaseOrderLineNumber AptosPOShipmentLineNumber,
	prl.ItemNumber,	
	imp.ProductDescription,
	prl.OrderedPurchaseQuantity,		
	prl.ReceivedPurchaseQuantity,
	prl.RemainingPurchaseQuantity,
	prl.PurchaseUnitSymbol,	
	prl.ReceivedInventoryQuantity,	
	prl.ReceivedInventoryStatusId,	
	prl.RemainingInventoryQuantity,	
	prh.RecordId,
	prl.ReceivingSiteId,	
	prl.ReceivingWarehouseId,
	prh.dataAreaId,	
	prh.ProductReceiptNumber,	
	prh.OrderVendorAccountNumber
from WMS.DynamicsProductReceiptHeaderStage prh with (nolock)
join WMS.DynamicsProductReceiptLineStage prl with (nolock) 
	on prh.RecordID=prl.ProductReceiptHeaderRecordID
	and prh.dataAreaId=prl.dataAreaId
	and prh.ProductReceiptNumber=prl.ProductReceiptNumber
	and prh.PurchaseOrderNumber=prl.PurchaseOrderNumber
join wms.ItemMaster im with (nolock)
	on prh.dataAreaId=im.Entity
	and prl.ItemNumber=im.ProductNumber 
	and im.NecessaryProductionWorkingTimeSchedulingPropertyId = 'Merch'
join wms.ItemMasterProducts imp with (nolock) on im.ItemNumber=imp.ProductNumber
left join POMap pom 
	on prh.PurchaseOrderNumber=pom.Dynamics1100PO
	and prh.OrderVendorAccountNumber=pom.VendorAccountNumber
where prh.dataAreaId='1100'
and prl.ReceivingWarehouseId='9980'
and pom.AptosPONumber is null
```

