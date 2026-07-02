# dbo.WebDemandOrdersUKStage

**Database:** master  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderNumber | varchar | 50 | 1 |  |  |  |
| OrderDateUTC | datetime | 8 | 1 |  |  |  |
| LastUpdateDateUTC | datetime | 8 | 1 |  |  |  |
| CustomerID | varchar | 50 | 1 |  |  |  |
| OrderStatus | varchar | 50 | 1 |  |  |  |
| OrderStatusCode | varchar | 50 | 1 |  |  |  |
| BillingProvince | varchar | 50 | 1 |  |  |  |
| BillingPostalCode | varchar | 50 | 1 |  |  |  |
| BillingCountry | varchar | 50 | 1 |  |  |  |
| ShippingProvince | varchar | 50 | 1 |  |  |  |
| ShippingPostalCode | varchar | 50 | 1 |  |  |  |
| ShippingCountry | varchar | 50 | 1 |  |  |  |
| SubTotal | numeric | 9 | 1 |  |  |  |
| VAT | numeric | 9 | 1 |  |  |  |
| VATShipping | numeric | 9 | 1 |  |  |  |
| TotalTax | numeric | 9 | 1 |  |  |  |
| ShippingTax | numeric | 9 | 1 |  |  |  |
| OriginalShipping | numeric | 9 | 1 |  |  |  |
| Shipping | numeric | 9 | 1 |  |  |  |
| ShippingMethod | varchar | 50 | 1 |  |  |  |
| ShippingMethodCode | varchar | 50 | 1 |  |  |  |
| OrderDiscount | numeric | 9 | 1 |  |  |  |
| ShippingDiscount | numeric | 9 | 1 |  |  |  |
| OrderGrossTotal | numeric | 9 | 1 |  |  |  |
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
| CustomOrderAttributes | nvarchar | 1000 | 1 |  |  |  |
| ChannelName | varchar | 50 | 1 |  |  |  |
| OrderPromotionIDs | varchar | 1000 | 1 |  |  |  |
| OrderCampaignIDs | varchar | 500 | 1 |  |  |  |
| OrderCoupons | varchar | 1000 | 1 |  |  |  |
| FileName | nvarchar | 1000 | 1 |  |  |  |
| SiteCode | varchar | 2 | 1 |  |  |  |

