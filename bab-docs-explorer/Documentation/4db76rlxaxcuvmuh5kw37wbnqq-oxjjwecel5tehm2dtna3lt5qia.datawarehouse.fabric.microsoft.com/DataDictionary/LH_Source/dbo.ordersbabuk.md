# dbo.ordersbabuk

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderNumber | varchar | 8000 | 1 |  |  |  |
| OrderDateUTC | datetime2 | 8 | 1 |  |  |  |
| LastUpdateDateUTC | datetime2 | 8 | 1 |  |  |  |
| CustomerID | int | 4 | 1 |  |  |  |
| OrderStatus | varchar | 8000 | 1 |  |  |  |
| OrderStatusCode | varchar | 8000 | 1 |  |  |  |
| BillingFirstName | varchar | 8000 | 1 |  |  |  |
| BillingLastName | varchar | 8000 | 1 |  |  |  |
| BillingAddress1 | varchar | 8000 | 1 |  |  |  |
| BillingAddress2 | varchar | 8000 | 1 |  |  |  |
| BillingAddress3 | varchar | 8000 | 1 |  |  |  |
| BillingCity | varchar | 8000 | 1 |  |  |  |
| BillingProvince | varchar | 8000 | 1 |  |  |  |
| BillingPostalCode | varchar | 8000 | 1 |  |  |  |
| BillingCountry | varchar | 8000 | 1 |  |  |  |
| BillingEmail | varchar | 8000 | 1 |  |  |  |
| BillingPhone | bigint | 8 | 1 |  |  |  |
| BillingMobilePhone | varchar | 8000 | 1 |  |  |  |
| BillingCompanyName | varchar | 8000 | 1 |  |  |  |
| ShippingFirstName | varchar | 8000 | 1 |  |  |  |
| ShippingLastName | varchar | 8000 | 1 |  |  |  |
| ShippingAddress1 | varchar | 8000 | 1 |  |  |  |
| ShippingAddress2 | varchar | 8000 | 1 |  |  |  |
| ShippingAddress3 | varchar | 8000 | 1 |  |  |  |
| ShippingCity | varchar | 8000 | 1 |  |  |  |
| ShippingProvince | varchar | 8000 | 1 |  |  |  |
| ShippingPostalCode | varchar | 8000 | 1 |  |  |  |
| ShippingCountry | varchar | 8000 | 1 |  |  |  |
| ShippingEmail | varchar | 8000 | 1 |  |  |  |
| ShippingPhone | bigint | 8 | 1 |  |  |  |
| ShippingMobilePhone | varchar | 8000 | 1 |  |  |  |
| ShippingCompanyName | varchar | 8000 | 1 |  |  |  |
| SubTotal | float | 8 | 1 |  |  |  |
| VAT | float | 8 | 1 |  |  |  |
| VATShipping | float | 8 | 1 |  |  |  |
| TotalTax | float | 8 | 1 |  |  |  |
| ShippingTax | float | 8 | 1 |  |  |  |
| OriginalShipping | float | 8 | 1 |  |  |  |
| Shipping | float | 8 | 1 |  |  |  |
| ShippingMethod | varchar | 8000 | 1 |  |  |  |
| ShippingMethodCode | varchar | 8000 | 1 |  |  |  |
| OrderDiscount | float | 8 | 1 |  |  |  |
| ShippingDiscount | float | 8 | 1 |  |  |  |
| OrderGrossTotal | float | 8 | 1 |  |  |  |
| IP | varchar | 8000 | 1 |  |  |  |
| GiftReceipt | bit | 1 | 1 |  |  |  |
| GiftWrap | bit | 1 | 1 |  |  |  |
| OrderSource | varchar | 8000 | 1 |  |  |  |
| Source1 | varchar | 8000 | 1 |  |  |  |
| Source2 | varchar | 8000 | 1 |  |  |  |
| Source3 | varchar | 8000 | 1 |  |  |  |
| Custom1 | varchar | 8000 | 1 |  |  |  |
| Custom2 | varchar | 8000 | 1 |  |  |  |
| Custom3 | bigint | 8 | 1 |  |  |  |
| Custom4 | bit | 1 | 1 |  |  |  |
| Custom5 | bit | 1 | 1 |  |  |  |
| CustomOrderAttributes | varchar | 8000 | 1 |  |  |  |
| SiteCode | varchar | 8000 | 1 |  |  |  |
| ChannelName | varchar | 8000 | 1 |  |  |  |
| OrderPromotionIDs | varchar | 8000 | 1 |  |  |  |
| OrderCampaignIDs | varchar | 8000 | 1 |  |  |  |
| OrderCoupons | varchar | 8000 | 1 |  |  |  |
| FileName | varchar | 8000 | 1 |  |  |  |
