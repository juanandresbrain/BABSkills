# dbo.webdemandorderitemsusstage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.webdemandorderitemsusstage"]
    dbo_webdemandorderitemsusstage(["dbo.webdemandorderitemsusstage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.webdemandorderitemsusstage |

## View Code

```sql
;
CREATE   VIEW [dbo].[webdemandorderitemsusstage]
AS
    SELECT [OrderNumber] COLLATE Latin1_General_CI_AS AS [OrderNumber], [UPC] COLLATE Latin1_General_CI_AS AS [UPC], [ItemStatus] COLLATE Latin1_General_CI_AS AS [ItemStatus], [OrderItemTypeName] COLLATE Latin1_General_CI_AS AS [OrderItemTypeName], [OrderDiscount], [ItemDiscount], [GiftCardNumber] COLLATE Latin1_General_CI_AS AS [GiftCardNumber], [ToName] COLLATE Latin1_General_CI_AS AS [ToName], [ToEmail] COLLATE Latin1_General_CI_AS AS [ToEmail], [FromName] COLLATE Latin1_General_CI_AS AS [FromName], [FromEmail] COLLATE Latin1_General_CI_AS AS [FromEmail], [Message] COLLATE Latin1_General_CI_AS AS [Message], [OrderLineNumber] COLLATE Latin1_General_CI_AS AS [OrderLineNumber], [LastUpdateDateUTC], [SKU] COLLATE Latin1_General_CI_AS AS [SKU], [Quantity] COLLATE Latin1_General_CI_AS AS [Quantity], [Price], [SubTotal], [USSalesTotal], [Tax], [Total], [Custom1] COLLATE Latin1_General_CI_AS AS [Custom1], [Custom2] COLLATE Latin1_General_CI_AS AS [Custom2], [Custom3] COLLATE Latin1_General_CI_AS AS [Custom3], [Custom4] COLLATE Latin1_General_CI_AS AS [Custom4], [Custom5] COLLATE Latin1_General_CI_AS AS [Custom5], [CustomExtendedAttributes] COLLATE Latin1_General_CI_AS AS [CustomExtendedAttributes], [OrderShipmentID] COLLATE Latin1_General_CI_AS AS [OrderShipmentID], [EstimatedShipDateUTC], [EndEstimatedShipDateUTC], [ShippingMethod] COLLATE Latin1_General_CI_AS AS [ShippingMethod], [ShippingMethodCode] COLLATE Latin1_General_CI_AS AS [ShippingMethodCode], [ShippedDateUTC], [OrderReturnID] COLLATE Latin1_General_CI_AS AS [OrderReturnID], [DateReturnedUTC], [ReturnReason] COLLATE Latin1_General_CI_AS AS [ReturnReason], [ReturnType] COLLATE Latin1_General_CI_AS AS [ReturnType], [ItemStatusCode] COLLATE Latin1_General_CI_AS AS [ItemStatusCode], [GiftCardType] COLLATE Latin1_General_CI_AS AS [GiftCardType], [Balance], [DeliveryType] COLLATE Latin1_General_CI_AS AS [DeliveryType], [WarehouseCode] COLLATE Latin1_General_CI_AS AS [WarehouseCode], [WarehouseLocation] COLLATE Latin1_General_CI_AS AS [WarehouseLocation], [ShippingErrorID] COLLATE Latin1_General_CI_AS AS [ShippingErrorID], [OrderPaymentID] COLLATE Latin1_General_CI_AS AS [OrderPaymentID], [OrderItemPromotionIds] COLLATE Latin1_General_CI_AS AS [OrderItemPromotionIds], [OrderItemCampaignIds] COLLATE Latin1_General_CI_AS AS [OrderItemCampaignIds], [OrderItemCoupons] COLLATE Latin1_General_CI_AS AS [OrderItemCoupons], [OrderPromotionIds] COLLATE Latin1_General_CI_AS AS [OrderPromotionIds], [OrderCampaignIds] COLLATE Latin1_General_CI_AS AS [OrderCampaignIds], [OrderCoupons] COLLATE Latin1_General_CI_AS AS [OrderCoupons], [OrderPlacementDateUTC], [ReturnNodeLocation] COLLATE Latin1_General_CI_AS AS [ReturnNodeLocation], [ReturnNodeCode] COLLATE Latin1_General_CI_AS AS [ReturnNodeCode], [ReturnUser] COLLATE Latin1_General_CI_AS AS [ReturnUser], [FulfillmentNodeType] COLLATE Latin1_General_CI_AS AS [FulfillmentNodeType], [Brand] COLLATE Latin1_General_CI_AS AS [Brand], [Cost], [FileName] COLLATE Latin1_General_CI_AS AS [FileName], [SiteCode] COLLATE Latin1_General_CI_AS AS [SiteCode]
    FROM LH_Staging.[dbo].[webdemandorderitemsusstage]
```

