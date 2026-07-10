# dbo.spMergeWebProductionOrderSummary

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMergeWebProductionOrderSummary"]
    dbo_WebProductionOrderSummary(["dbo.WebProductionOrderSummary"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.WebProductionOrderSummary |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMergeWebProductionOrderSummary]

as

set nocount on

Merge into DW.dbo.WebProductionOrderSummary as target
Using dwstaging.dbo.WebProductionOrderSummary as source
On (
		isnull(target.ProductionOrderID, 0) = isnull(source.ProductionOrderID, 0)
	)
when matched 
	and 
		(
			 isnull(target.ProductionOrderSubTotal,0)<>isnull(source.ProductionOrderSubTotal,0)   
			OR isnull(target.ProductionOrderNumber,'xx')<>isnull(source.ProductionOrderNumber,'xx') 
			or isnull(target.ProductionOrderShippingAndHandling,0)<>isnull(source.ProductionOrderShippingAndHandling,0)  
			or isnull(target.ProductionOrderPromoDiscount,0)<>isnull(source.ProductionOrderPromoDiscount,0)   
			or isnull(target.ProductionOrderTotal,0)<>isnull(source.ProductionOrderTotal,0)   
			or isnull(target.ProductionOrderDateTimeCreated,'3030-12-31')<>isnull(source.ProductionOrderDateTimeCreated,0)  
			or isnull(target.ProductionOrderShippingMethod,0)<>isnull(source.ProductionOrderShippingMethod,0) 
			or isnull(target.ProductionOrderTrackingNumber,0)<>isnull(source.ProductionOrderTrackingNumber,0)  
			or isnull(target.ProductionOrderBillingStateProvince,0)<>isnull(source.ProductionOrderBillingStateProvince,0)  
			or isnull(target.ProductionOrderBillingZipPostalCode,0)<>isnull(source.ProductionOrderBillingZipPostalCode,0) 
			or isnull(target.ProductionOrderBillingCountry,0)<>isnull(source.ProductionOrderBillingCountry,0)  
			or isnull(target.ProductionOrderShippingStateProvince,0)<>isnull(source.ProductionOrderShippingStateProvince,0) 
			or isnull(target.ProductionOrderShippingZipPostalCode,0)<>isnull(source.ProductionOrderShippingZipPostalCode,0) 
			or isnull(target.ProductionOrderShippingCountry,0)<>isnull(source.ProductionOrderShippingCountry,0)  
			or isnull(target.ProductionOrderWebOrderStatus,0)<>isnull(source.ProductionOrderWebOrderStatus,0) 
			or isnull(target.ProductionOrderCatalogName,0)<>isnull(source.ProductionOrderCatalogName,0) 
			or isnull(target.ProductionOrderNumberOfPackages,0)<>isnull(source.ProductionOrderNumberOfPackages,0)  
			or isnull(target.ProductionOrderWebCartOrderId,0)<>isnull(source.ProductionOrderWebCartOrderId,0)  
			or isnull(target.ProductionOrderWebCartUpdateMsgSent,0)<>isnull(source.ProductionOrderWebCartUpdateMsgSent,0)  
			or isnull(target.ProductionOrderSiteCode,0)<>isnull(source.ProductionOrderSiteCode,0) 
			or isnull(target.ProductionOrderBearBuilderId,0)<>isnull(source.ProductionOrderBearBuilderId,0) 
			or isnull(target.ProductionOrderBuyStuffStamps,0)<>isnull(source.ProductionOrderBuyStuffStamps,0)  
			or isnull(target.ProductionOrderActuallShippingCost,0)<>isnull(source.ProductionOrderActuallShippingCost,0)   
			or isnull(target.ProductionOrderHasShippableProducts,0)<>isnull(source.ProductionOrderHasShippableProducts,0)
			or isnull(target.ProductionOrderWH_version,0)<>isnull(source.ProductionOrderWH_version,0)  
			or isnull(target.ProductionOrderReceiptCode,0)<>isnull(source.ProductionOrderReceiptCode,0) 
			or isnull(target.ProductionOrderServerName,0)<>isnull(source.ProductionOrderServerName,0) 
			or isnull(target.ProductionOrderStatusID,0)<>isnull(source.ProductionOrderStatusID,0)  
			or isnull(target.StatusDate,'3030-12-31')<>isnull(source.StatusDate,'3030-12-31') 
			or isnull(target.ESReferenceNbr, 'x')<>isnull(source.ESReferenceNbr,'x')
		)
	THEN UPDATE
		SET 
			target.ProductionOrderNumber=source.ProductionOrderNumber,
			target.ProductionOrderSubTotal=source.ProductionOrderSubTotal,
			target.ProductionOrderShippingAndHandling=source.ProductionOrderShippingAndHandling,
			target.ProductionOrderPromoDiscount=source.ProductionOrderPromoDiscount,   
			target.ProductionOrderTotal=source.ProductionOrderTotal,   
			target.ProductionOrderDateTimeCreated=source.ProductionOrderDateTimeCreated,  
			target.ProductionOrderShippingMethod=source.ProductionOrderShippingMethod, 
			target.ProductionOrderTrackingNumber=source.ProductionOrderTrackingNumber,  
			target.ProductionOrderBillingStateProvince=source.ProductionOrderBillingStateProvince,  
			target.ProductionOrderBillingZipPostalCode=source.ProductionOrderBillingZipPostalCode, 
			target.ProductionOrderBillingCountry=source.ProductionOrderBillingCountry,  
			target.ProductionOrderShippingStateProvince=source.ProductionOrderShippingStateProvince, 
			target.ProductionOrderShippingZipPostalCode=source.ProductionOrderShippingZipPostalCode, 
			target.ProductionOrderShippingCountry=source.ProductionOrderShippingCountry,  
			target.ProductionOrderWebOrderStatus=source.ProductionOrderWebOrderStatus, 
			target.ProductionOrderCatalogName=source.ProductionOrderCatalogName, 
			target.ProductionOrderNumberOfPackages=source.ProductionOrderNumberOfPackages,  
			target.ProductionOrderWebCartOrderId=source.ProductionOrderWebCartOrderId,  
			target.ProductionOrderWebCartUpdateMsgSent=source.ProductionOrderWebCartUpdateMsgSent,  
			target.ProductionOrderSiteCode=source.ProductionOrderSiteCode, 
			target.ProductionOrderBearBuilderId=source.ProductionOrderBearBuilderId, 
			target.ProductionOrderBuyStuffStamps=source.ProductionOrderBuyStuffStamps,  
			target.ProductionOrderActuallShippingCost=source.ProductionOrderActuallShippingCost,   
			target.ProductionOrderHasShippableProducts=source.ProductionOrderHasShippableProducts,
			target.ProductionOrderWH_version=source.ProductionOrderWH_version,  
			target.ProductionOrderReceiptCode=source.ProductionOrderReceiptCode,  
			target.ProductionOrderServerName=source.ProductionOrderServerName, 
			target.ProductionOrderStatusID=source.ProductionOrderStatusID, 
			target.StatusDate=source.StatusDate,
			target.ESReferenceNbr=source.ESReferenceNbr,
			target.UpdateDate = getdate() 

when not matched by target
	then insert 
			(
				ProductionOrderID,
				ProductionOrderNumber, 
				ProductionOrderSubTotal,   
				ProductionOrderShippingAndHandling,
				ProductionOrderPromoDiscount,   
				ProductionOrderTotal,   
				ProductionOrderDateTimeCreated,  
				ProductionOrderShippingMethod, 
				ProductionOrderTrackingNumber,  
				ProductionOrderBillingStateProvince,  
				ProductionOrderBillingZipPostalCode, 
				ProductionOrderBillingCountry,  
				ProductionOrderShippingStateProvince, 
				ProductionOrderShippingZipPostalCode, 
				ProductionOrderShippingCountry,  
				ProductionOrderWebOrderStatus, 
				ProductionOrderCatalogName, 
				ProductionOrderNumberOfPackages,  
				ProductionOrderWebCartOrderId, 
				ProductionOrderWebCartUpdateMsgSent,
				ProductionOrderSiteCode, 
				ProductionOrderBearBuilderId, 
				ProductionOrderBuyStuffStamps,  
				ProductionOrderActuallShippingCost,   
				ProductionOrderHasShippableProducts,
				ProductionOrderWH_version,  
				ProductionOrderReceiptCode,  
				ProductionOrderServerName, 
				ProductionOrderStatusID,  
				StatusDate,
				ESReferenceNbr,
				InsertDate
		)
	values
		(
				source.ProductionOrderID,
				source.ProductionOrderNumber,
				source.ProductionOrderSubTotal,   
				source.ProductionOrderShippingAndHandling,   
				source.ProductionOrderPromoDiscount,   
				source.ProductionOrderTotal,   
				source.ProductionOrderDateTimeCreated,  
				source.ProductionOrderShippingMethod, 
				source.ProductionOrderTrackingNumber,  
				source.ProductionOrderBillingStateProvince,  
				source.ProductionOrderBillingZipPostalCode, 
				source.ProductionOrderBillingCountry,  
				source.ProductionOrderShippingStateProvince, 
				source.ProductionOrderShippingZipPostalCode, 
				source.ProductionOrderShippingCountry,  
				source.ProductionOrderWebOrderStatus, 
				source.ProductionOrderCatalogName, 
				source.ProductionOrderNumberOfPackages,  
				source.ProductionOrderWebCartOrderId,  
				source.ProductionOrderWebCartUpdateMsgSent,  
				source.ProductionOrderSiteCode, 
				source.ProductionOrderBearBuilderId, 
				source.ProductionOrderBuyStuffStamps,  
				source.ProductionOrderActuallShippingCost,   
				source.ProductionOrderHasShippableProducts,
				source.ProductionOrderWH_version,  
				source.ProductionOrderReceiptCode,  
				source.ProductionOrderServerName, 
				source.ProductionOrderStatusID,  
				source.StatusDate, 
				source.ESReferenceNbr,
				getdate()
		)
;
```

