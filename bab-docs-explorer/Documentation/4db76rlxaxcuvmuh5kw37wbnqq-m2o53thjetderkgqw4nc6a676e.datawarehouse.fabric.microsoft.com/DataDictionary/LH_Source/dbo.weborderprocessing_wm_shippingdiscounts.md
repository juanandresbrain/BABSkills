# dbo.weborderprocessing_wm_shippingdiscounts

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ShippingDiscountID | int | 4 | 1 |  |  |  |
| OrderId | int | 4 | 1 |  |  |  |
| PromoCode | varchar | 8000 | 1 |  |  |  |
| DiscountAmount | decimal | 9 | 1 |  |  |  |
| DiscountName | varchar | 8000 | 1 |  |  |  |
| OrderNum | varchar | 8000 | 1 |  |  |  |
