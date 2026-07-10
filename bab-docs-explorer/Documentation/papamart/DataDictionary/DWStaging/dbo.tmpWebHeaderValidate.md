# dbo.tmpWebHeaderValidate

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderNumber | varchar | 50 | 1 |  |  |  |
| OrderDate | datetime | 8 | 1 |  |  |  |
| OrderStatus | varchar | 50 | 1 |  |  |  |
| Channel | varchar | 50 | 1 |  |  |  |
| SubTotal | decimal | 9 | 1 |  |  |  |
| TotalTax | decimal | 9 | 1 |  |  |  |
| ShippingTax | decimal | 9 | 1 |  |  |  |
| OriginalShipping | decimal | 9 | 1 |  |  |  |
| Shipping | decimal | 9 | 1 |  |  |  |
| ShippingMethod | varchar | 50 | 1 |  |  |  |
| OrderDiscount | decimal | 9 | 1 |  |  |  |
| ShippingDiscount | decimal | 9 | 1 |  |  |  |
| OrderGrossTotal | decimal | 9 | 1 |  |  |  |
| SiteCode | varchar | 50 | 1 |  |  |  |
