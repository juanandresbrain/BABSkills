# WM.OMSCustomOrderExportNew

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CustomOrderExportID | int | 4 | 0 |  |  |  |
| OrderNumber | varchar | 50 | 1 |  |  |  |
| OrderDateUTC | varchar | 50 | 1 |  |  |  |
| LastUpdateDateUTC | varchar | 50 | 1 |  |  |  |
| CustomerID | varchar | 50 | 1 |  |  |  |
| OrderStatus | varchar | 50 | 1 |  |  |  |
| OrderStatusCode | varchar | 50 | 1 |  |  |  |
| ShippingCountry | varchar | 50 | 1 |  |  |  |
| ShippingCompanyName | varchar | 50 | 1 |  |  |  |
| SubTotal | varchar | 50 | 1 |  |  |  |
| VAT | varchar | 50 | 1 |  |  |  |
| VAT Shipping | varchar | 50 | 1 |  |  |  |
| TotalTax | varchar | 50 | 1 |  |  |  |
| ShippingTax | varchar | 50 | 1 |  |  |  |
| OriginalShipping | varchar | 50 | 1 |  |  |  |
| Shipping | varchar | 50 | 1 |  |  |  |
| ShippingMethod | varchar | 50 | 1 |  |  |  |
| ShippingMethodCode | varchar | 50 | 1 |  |  |  |
| OrderDiscount | varchar | 50 | 1 |  |  |  |
| ShippingDiscount | varchar | 50 | 1 |  |  |  |
| OrderGrossTotal | varchar | 50 | 1 |  |  |  |
| IP | varchar | 50 | 1 |  |  |  |
| GiftReceipt | varchar | 50 | 1 |  |  |  |
| GiftWrap | varchar | 50 | 1 |  |  |  |
| OrderSource | varchar | 50 | 1 |  |  |  |
| Source1 | varchar | 50 | 1 |  |  |  |
| Source2 | varchar | 50 | 1 |  |  |  |
| Source3 | varchar | 50 | 1 |  |  |  |
| Custom1 | varchar | 50 | 1 |  |  |  |
| Custom2 | varchar | 50 | 1 |  |  |  |
| Custom3 | varchar | 50 | 1 |  |  |  |
| Custom4 | varchar | 50 | 1 |  |  |  |
| Custom5 | varchar | 50 | 1 |  |  |  |
| CustomOrderAttributes | varchar | 500 | 1 |  |  |  |
| Flat File Source.SiteCode | varchar | 50 | 1 |  |  |  |
| ChannelName | varchar | 50 | 1 |  |  |  |
| OrderPromotionIDs | varchar | 500 | 1 |  |  |  |
| OrderCampaignIDs | varchar | 500 | 1 |  |  |  |
| OrderCoupons | varchar | 500 | 1 |  |  |  |
| OMSFileName | nvarchar | 800 | 1 |  |  |  |
| DC - Fix Column Data.SiteCode | varchar | 2 | 1 |  |  |  |
| TransactionID | int | 4 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |

