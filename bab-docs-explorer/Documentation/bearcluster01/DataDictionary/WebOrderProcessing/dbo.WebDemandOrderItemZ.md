# dbo.WebDemandOrderItemZ

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

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
| ToName | varchar | 500 | 1 |  |  |  |
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
| SalesTotal | numeric | 9 | 1 |  |  |  |
| VAT | numeric | 9 | 1 |  |  |  |
| Tax | numeric | 9 | 1 |  |  |  |
| Total | numeric | 9 | 1 |  |  |  |
| Custom1 | nvarchar | 1000 | 1 |  |  |  |
| Custom2 | nvarchar | 1000 | 1 |  |  |  |
| Custom3 | nvarchar | 1000 | 1 |  |  |  |
| Custom4 | nvarchar | 1000 | 1 |  |  |  |
| Custom5 | nvarchar | 1000 | 1 |  |  |  |
| CustomExtendedAttributes | nvarchar | 8000 | 1 |  |  |  |
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
| OrderCampaignIds | varchar | 500 | 1 |  |  |  |
| OrderCoupons | varchar | 1000 | 1 |  |  |  |
| OrderPlacementDateUTC | datetime | 8 | 1 |  |  |  |
| ReturnNodeLocation | varchar | 50 | 1 |  |  |  |
| ReturnNodeCode | varchar | 50 | 1 |  |  |  |
| ReturnUser | varchar | 50 | 1 |  |  |  |
| FulfillmentNodeType | varchar | 50 | 1 |  |  |  |
| Brand | varchar | 50 | 1 |  |  |  |
| Cost | numeric | 9 | 1 |  |  |  |
| SiteCode | varchar | 2 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: dbo.spBabDynamics1_BuildDiscountStagingTable](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics1_BuildDiscountStagingTable.md)
- [WebOrderProcessing: dbo.spBabDynamics1_BuildDiscountStagingTable_BAK20240617](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics1_BuildDiscountStagingTable_BAK20240617.md)
- [WebOrderProcessing: dbo.spBabDynamics2_BuildHeaderStagingTable](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics2_BuildHeaderStagingTable.md)
- [WebOrderProcessing: dbo.spBabDynamics3_BuildSalesLineStagingTable](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics3_BuildSalesLineStagingTable.md)
- [WebOrderProcessing: dbo.spBabDynamics4_BuildTaxStagingTable](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics4_BuildTaxStagingTable.md)
- [WebOrderProcessing: dbo.spBabDynamics5_BuildTenderStagingTable](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics5_BuildTenderStagingTable.md)
- [WebOrderProcessing: dbo.spMergeWebDemandOrderItemz](../../StoredProcedures/WebOrderProcessing/dbo.spMergeWebDemandOrderItemz.md)

