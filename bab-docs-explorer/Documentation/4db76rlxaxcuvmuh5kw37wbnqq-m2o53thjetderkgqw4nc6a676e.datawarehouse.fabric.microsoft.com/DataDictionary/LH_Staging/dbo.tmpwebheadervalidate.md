# dbo.tmpwebheadervalidate

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderNumber | varchar | 8000 | 1 |  |  |  |
| OrderDate | datetime2 | 8 | 1 |  |  |  |
| OrderStatus | varchar | 8000 | 1 |  |  |  |
| Channel | varchar | 8000 | 1 |  |  |  |
| SubTotal | decimal | 9 | 1 |  |  |  |
| TotalTax | decimal | 9 | 1 |  |  |  |
| ShippingTax | decimal | 9 | 1 |  |  |  |
| OriginalShipping | decimal | 9 | 1 |  |  |  |
| Shipping | decimal | 9 | 1 |  |  |  |
| ShippingMethod | varchar | 8000 | 1 |  |  |  |
| OrderDiscount | decimal | 9 | 1 |  |  |  |
| ShippingDiscount | decimal | 9 | 1 |  |  |  |
| OrderGrossTotal | decimal | 9 | 1 |  |  |  |
| SiteCode | varchar | 8000 | 1 |  |  |  |
