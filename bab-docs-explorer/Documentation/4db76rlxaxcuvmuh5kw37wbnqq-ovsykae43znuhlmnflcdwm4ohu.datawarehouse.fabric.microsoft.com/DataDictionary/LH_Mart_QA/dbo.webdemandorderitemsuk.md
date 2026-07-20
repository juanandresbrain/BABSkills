# dbo.webdemandorderitemsuk

**Database:** LH_Mart_QA  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderNumber | varchar | 8000 | 1 |  |  |  |
| UPC | varchar | 8000 | 1 |  |  |  |
| ItemStatus | varchar | 8000 | 1 |  |  |  |
| OrderItemTypeName | varchar | 8000 | 1 |  |  |  |
| OrderDiscount | decimal | 9 | 1 |  |  |  |
| ItemDiscount | decimal | 9 | 1 |  |  |  |
| GiftCardNumber | varchar | 8000 | 1 |  |  |  |
| ToName | varchar | 8000 | 1 |  |  |  |
| ToEmail | varchar | 8000 | 1 |  |  |  |
| FromName | varchar | 8000 | 1 |  |  |  |
| FromEmail | varchar | 8000 | 1 |  |  |  |
| Message | varchar | 8000 | 1 |  |  |  |
| OrderLineNumber | varchar | 8000 | 1 |  |  |  |
| LastUpdateDateUTC | datetime2 | 8 | 1 |  |  |  |
| SKU | varchar | 8000 | 1 |  |  |  |
| Quantity | varchar | 8000 | 1 |  |  |  |
| Price | decimal | 9 | 1 |  |  |  |
| SubTotal | decimal | 9 | 1 |  |  |  |
| VAT | decimal | 9 | 1 |  |  |  |
| Tax | decimal | 9 | 1 |  |  |  |
| Total | decimal | 9 | 1 |  |  |  |
| Custom1 | varchar | 8000 | 1 |  |  |  |
| Custom2 | varchar | 8000 | 1 |  |  |  |
| Custom3 | varchar | 8000 | 1 |  |  |  |
| Custom4 | varchar | 8000 | 1 |  |  |  |
| Custom5 | varchar | 8000 | 1 |  |  |  |
| CustomExtendedAttributes | varchar | 8000 | 1 |  |  |  |
| OrderShipmentID | varchar | 8000 | 1 |  |  |  |
| EstimatedShipDateUTC | datetime2 | 8 | 1 |  |  |  |
| EndEstimatedShipDateUTC | datetime2 | 8 | 1 |  |  |  |
| ShippingMethod | varchar | 8000 | 1 |  |  |  |
| ShippingMethodCode | varchar | 8000 | 1 |  |  |  |
| ShippedDateUTC | datetime2 | 8 | 1 |  |  |  |
| OrderReturnID | varchar | 8000 | 1 |  |  |  |
| DateReturnedUTC | datetime2 | 8 | 1 |  |  |  |
| ReturnReason | varchar | 8000 | 1 |  |  |  |
| ReturnType | varchar | 8000 | 1 |  |  |  |
| ItemStatusCode | varchar | 8000 | 1 |  |  |  |
| GiftCardType | varchar | 8000 | 1 |  |  |  |
| Balance | decimal | 9 | 1 |  |  |  |
| DeliveryType | varchar | 8000 | 1 |  |  |  |
| WarehouseCode | varchar | 8000 | 1 |  |  |  |
| WarehouseLocation | varchar | 8000 | 1 |  |  |  |
| ShippingErrorID | varchar | 8000 | 1 |  |  |  |
| OrderPaymentID | varchar | 8000 | 1 |  |  |  |
| OrderItemPromotionIds | varchar | 8000 | 1 |  |  |  |
| OrderItemCampaignIds | varchar | 8000 | 1 |  |  |  |
| OrderItemCoupons | varchar | 8000 | 1 |  |  |  |
| OrderPromotionIds | varchar | 8000 | 1 |  |  |  |
| OrderCampaignIds | varchar | 8000 | 1 |  |  |  |
| OrderCoupons | varchar | 8000 | 1 |  |  |  |
| OrderPlacementDateUTC | datetime2 | 8 | 1 |  |  |  |
| ReturnNodeLocation | varchar | 8000 | 1 |  |  |  |
| ReturnNodeCode | varchar | 8000 | 1 |  |  |  |
| ReturnUser | varchar | 8000 | 1 |  |  |  |
| FulfillmentNodeType | varchar | 8000 | 1 |  |  |  |
| Brand | varchar | 8000 | 1 |  |  |  |
| Cost | decimal | 9 | 1 |  |  |  |
| FileName | varchar | 8000 | 1 |  |  |  |
| SiteCode | varchar | 8000 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
