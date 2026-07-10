# dbo.WebDemandOrderItemsUSStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderNumber | varchar | 50 | 1 |  |  |  |
| UPC | varchar | 50 | 1 |  |  |  |
| ItemStatus | varchar | 50 | 1 |  |  |  |
| OrderItemTypeName | varchar | 50 | 1 |  |  |  |
| OrderDiscount | numeric | 9 | 1 |  |  |  |
| ItemDiscount | numeric | 9 | 1 |  |  |  |
| GiftCardNumber | varchar | 50 | 1 |  |  |  |
| ToName | varchar | 50 | 1 |  |  |  |
| ToEmail | varchar | 50 | 1 |  |  |  |
| FromName | varchar | 100 | 1 |  |  |  |
| FromEmail | varchar | 50 | 1 |  |  |  |
| Message | nvarchar | 8000 | 1 |  |  |  |
| OrderLineNumber | varchar | 50 | 1 |  |  |  |
| LastUpdateDateUTC | datetime | 8 | 1 |  |  |  |
| SKU | varchar | 50 | 1 |  |  |  |
| Quantity | varchar | 50 | 1 |  |  |  |
| Price | numeric | 9 | 1 |  |  |  |
| SubTotal | numeric | 9 | 1 |  |  |  |
| USSalesTotal | numeric | 9 | 1 |  |  |  |
| Tax | numeric | 9 | 1 |  |  |  |
| Total | numeric | 9 | 1 |  |  |  |
| Custom1 | nvarchar | 1000 | 1 |  |  |  |
| Custom2 | nvarchar | 1000 | 1 |  |  |  |
| Custom3 | nvarchar | 1000 | 1 |  |  |  |
| Custom4 | nvarchar | 1000 | 1 |  |  |  |
| Custom5 | nvarchar | 1000 | 1 |  |  |  |
| CustomExtendedAttributes | nvarchar | 1000 | 1 |  |  |  |
| OrderShipmentID | varchar | 50 | 1 |  |  |  |
| EstimatedShipDateUTC | datetime | 8 | 1 |  |  |  |
| EndEstimatedShipDateUTC | datetime | 8 | 1 |  |  |  |
| ShippingMethod | varchar | 50 | 1 |  |  |  |
| ShippingMethodCode | varchar | 50 | 1 |  |  |  |
| ShippedDateUTC | datetime | 8 | 1 |  |  |  |
| OrderReturnID | varchar | 50 | 1 |  |  |  |
| DateReturnedUTC | datetime | 8 | 1 |  |  |  |
| ReturnReason | varchar | 50 | 1 |  |  |  |
| ReturnType | varchar | 50 | 1 |  |  |  |
| ItemStatusCode | varchar | 50 | 1 |  |  |  |
| GiftCardType | varchar | 50 | 1 |  |  |  |
| Balance | numeric | 9 | 1 |  |  |  |
| DeliveryType | varchar | 50 | 1 |  |  |  |
| WarehouseCode | varchar | 50 | 1 |  |  |  |
| WarehouseLocation | varchar | 50 | 1 |  |  |  |
| ShippingErrorID | varchar | 50 | 1 |  |  |  |
| OrderPaymentID | varchar | 50 | 1 |  |  |  |
| OrderItemPromotionIds | varchar | 100 | 1 |  |  |  |
| OrderItemCampaignIds | varchar | 100 | 1 |  |  |  |
| OrderItemCoupons | varchar | 50 | 1 |  |  |  |
| OrderPromotionIds | varchar | 1000 | 1 |  |  |  |
| OrderCampaignIds | varchar | 50 | 1 |  |  |  |
| OrderCoupons | varchar | 1000 | 1 |  |  |  |
| OrderPlacementDateUTC | datetime | 8 | 1 |  |  |  |
| ReturnNodeLocation | varchar | 50 | 1 |  |  |  |
| ReturnNodeCode | varchar | 50 | 1 |  |  |  |
| ReturnUser | varchar | 50 | 1 |  |  |  |
| FulfillmentNodeType | varchar | 50 | 1 |  |  |  |
| Brand | varchar | 50 | 1 |  |  |  |
| Cost | numeric | 9 | 1 |  |  |  |
| FileName | nvarchar | 1000 | 1 |  |  |  |
| SiteCode | varchar | 2 | 1 |  |  |  |
