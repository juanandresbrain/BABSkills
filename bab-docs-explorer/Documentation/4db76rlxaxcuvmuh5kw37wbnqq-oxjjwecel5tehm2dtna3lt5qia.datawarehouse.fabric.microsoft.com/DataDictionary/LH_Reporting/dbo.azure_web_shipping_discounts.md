# dbo.azure_web_shipping_discounts

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ShippingDiscountID | int | 4 | 1 |  |  |  |
| OrderID | int | 4 | 1 |  |  |  |
| PromoCode | varchar | 8000 | 1 |  |  |  |
| DiscountAmount | decimal | 9 | 1 |  |  |  |
| DiscountName | varchar | 8000 | 1 |  |  |  |
| InsertDate | date | 3 | 1 |  |  |  |
| UpdateDate | date | 3 | 1 |  |  |  |
