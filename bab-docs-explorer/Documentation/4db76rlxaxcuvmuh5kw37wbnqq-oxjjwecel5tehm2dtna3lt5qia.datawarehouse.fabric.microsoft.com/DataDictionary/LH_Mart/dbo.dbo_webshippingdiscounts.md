# dbo.dbo_webshippingdiscounts

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ShippingDiscountID | int | 4 | 1 |  |  |  |
| OrderID | int | 4 | 1 |  |  |  |
| PromoCode | varchar | 8000 | 1 |  |  |  |
| DiscountAmount | decimal | 9 | 1 |  |  |  |
| DiscountName | varchar | 8000 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
