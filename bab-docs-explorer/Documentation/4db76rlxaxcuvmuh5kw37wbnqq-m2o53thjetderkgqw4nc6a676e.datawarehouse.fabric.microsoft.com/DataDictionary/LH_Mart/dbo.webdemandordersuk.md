# dbo.webdemandordersuk

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderNumber | varchar | 8000 | 1 |  |  |  |
| OrderDateUTC | datetime2 | 8 | 1 |  |  |  |
| LastUpdateDateUTC | datetime2 | 8 | 1 |  |  |  |
| CustomerID | varchar | 8000 | 1 |  |  |  |
| OrderStatus | varchar | 8000 | 1 |  |  |  |
| OrderStatusCode | varchar | 8000 | 1 |  |  |  |
| BillingProvince | varchar | 8000 | 1 |  |  |  |
| BillingPostalCode | varchar | 8000 | 1 |  |  |  |
| BillingCountry | varchar | 8000 | 1 |  |  |  |
| ShippingProvince | varchar | 8000 | 1 |  |  |  |
| ShippingPostalCode | varchar | 8000 | 1 |  |  |  |
| ShippingCountry | varchar | 8000 | 1 |  |  |  |
| SubTotal | decimal | 9 | 1 |  |  |  |
| VAT | decimal | 9 | 1 |  |  |  |
| VATShipping | decimal | 9 | 1 |  |  |  |
| TotalTax | decimal | 9 | 1 |  |  |  |
| ShippingTax | decimal | 9 | 1 |  |  |  |
| OriginalShipping | decimal | 9 | 1 |  |  |  |
| Shipping | decimal | 9 | 1 |  |  |  |
| ShippingMethod | varchar | 8000 | 1 |  |  |  |
| ShippingMethodCode | varchar | 8000 | 1 |  |  |  |
| OrderDiscount | decimal | 9 | 1 |  |  |  |
| ShippingDiscount | decimal | 9 | 1 |  |  |  |
| OrderGrossTotal | decimal | 9 | 1 |  |  |  |
| GiftReceipt | varchar | 8000 | 1 |  |  |  |
| GiftWrap | varchar | 8000 | 1 |  |  |  |
| OrderSource | varchar | 8000 | 1 |  |  |  |
| Source1 | varchar | 8000 | 1 |  |  |  |
| Source2 | varchar | 8000 | 1 |  |  |  |
| Source3 | varchar | 8000 | 1 |  |  |  |
| Custom1 | varchar | 8000 | 1 |  |  |  |
| Custom2 | varchar | 8000 | 1 |  |  |  |
| Custom3 | varchar | 8000 | 1 |  |  |  |
| Custom4 | varchar | 8000 | 1 |  |  |  |
| Custom5 | varchar | 8000 | 1 |  |  |  |
| CustomOrderAttributes | varchar | 8000 | 1 |  |  |  |
| ChannelName | varchar | 8000 | 1 |  |  |  |
| OrderPromotionIDs | varchar | 8000 | 1 |  |  |  |
| OrderCampaignIDs | varchar | 8000 | 1 |  |  |  |
| OrderCoupons | varchar | 8000 | 1 |  |  |  |
| FileName | varchar | 8000 | 1 |  |  |  |
| SiteCode | varchar | 8000 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
