# dbo.spMergeWebDemandOrderItemsUK

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMergeWebDemandOrderItemsUK"]
    dbo_WebDemandOrderItemsUK(["dbo.WebDemandOrderItemsUK"]) --> SP
    WebDemandOrderItemsUKStage(["WebDemandOrderItemsUKStage"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.WebDemandOrderItemsUK |
| WebDemandOrderItemsUKStage |

## Stored Procedure Code

```sql
create proc [dbo].[spMergeWebDemandOrderItemsUK]

as 

set nocount on
;
with
Files as
(
	select distinct FileName 
	from WebDemandOrderItemsUKStage
)
delete t
from dw.dbo.WebDemandOrderItemsUK t
join Files f on f.FileName=t.FileName
;

merge into dw.dbo.WebDemandOrderItemsUK as target
using WebDemandOrderItemsUKStage as source
on 
	target.FileName=source.FileName
--when matched 
--	then delete
when not matched by target
	then insert
		(
			OrderNumber,	
			UPC,	
			ItemStatus,	
			OrderItemTypeName,	
			OrderDiscount,	
			ItemDiscount,	
			GiftCardNumber,	
			ToName,	
			ToEmail,	
			FromName,	
			FromEmail,	
			Message,	
			OrderLineNumber,	
			LastUpdateDateUTC,	
			SKU,	
			Quantity,	
			Price,	
			SubTotal,	
			VAT,	
			Tax,	
			Total,	
			Custom1,	
			Custom2,	
			Custom3,	
			Custom4,	
			Custom5,	
			CustomExtendedAttributes,	
			OrderShipmentID,	
			EstimatedShipDateUTC,	
			EndEstimatedShipDateUTC,	
			ShippingMethod,	
			ShippingMethodCode,	
			ShippedDateUTC,	
			OrderReturnID,	
			DateReturnedUTC,	
			ReturnReason,	
			ReturnType,	
			ItemStatusCode,	
			GiftCardType,	
			Balance,	
			DeliveryType,	
			WarehouseCode,	
			WarehouseLocation,	
			ShippingErrorID,	
			OrderPaymentID,	
			OrderItemPromotionIds,	
			OrderItemCampaignIds,	
			OrderItemCoupons,	
			OrderPromotionIds,	
			OrderCampaignIds,	
			OrderCoupons,	
			OrderPlacementDateUTC,	
			ReturnNodeLocation,	
			ReturnNodeCode,	
			ReturnUser,	
			FulfillmentNodeType,	
			Brand,	
			Cost,	
			FileName,	
			SiteCode,
			InsertDate
		)
	values
		(
			source.OrderNumber,	
			source.UPC,	
			source.ItemStatus,	
			source.OrderItemTypeName,	
			source.OrderDiscount,	
			source.ItemDiscount,	
			source.GiftCardNumber,	
			source.ToName,	
			source.ToEmail,	
			source.FromName,	
			source.FromEmail,	
			source.Message,	
			source.OrderLineNumber,	
			source.LastUpdateDateUTC,	
			source.SKU,	
			source.Quantity,	
			source.Price,	
			source.SubTotal,	
			source.VAT,	
			source.Tax,	
			source.Total,	
			source.Custom1,	
			source.Custom2,	
			source.Custom3,	
			source.Custom4,	
			source.Custom5,	
			source.CustomExtendedAttributes,	
			source.OrderShipmentID,	
			source.EstimatedShipDateUTC,	
			source.EndEstimatedShipDateUTC,	
			source.ShippingMethod,	
			source.ShippingMethodCode,	
			source.ShippedDateUTC,	
			source.OrderReturnID,	
			source.DateReturnedUTC,	
			source.ReturnReason,	
			source.ReturnType,	
			source.ItemStatusCode,	
			source.GiftCardType,	
			source.Balance,	
			source.DeliveryType,	
			source.WarehouseCode,	
			source.WarehouseLocation,	
			source.ShippingErrorID,	
			source.OrderPaymentID,	
			source.OrderItemPromotionIds,	
			source.OrderItemCampaignIds,	
			source.OrderItemCoupons,	
			source.OrderPromotionIds,	
			source.OrderCampaignIds,	
			source.OrderCoupons,	
			source.OrderPlacementDateUTC,	
			source.ReturnNodeLocation,	
			source.ReturnNodeCode,	
			source.ReturnUser,	
			source.FulfillmentNodeType,	
			source.Brand,	
			source.Cost,	
			source.FileName,	
			source.SiteCode,
			getdate()
		)
;
```

