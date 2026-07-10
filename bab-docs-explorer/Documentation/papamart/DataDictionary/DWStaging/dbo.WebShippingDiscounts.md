# dbo.WebShippingDiscounts

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ShippingDiscountID | int | 4 | 1 |  |  |  |
| OrderID | int | 4 | 1 |  |  |  |
| PromoCode | varchar | 40 | 1 |  |  |  |
| DiscountAmount | money | 8 | 1 |  |  |  |
| DiscountName | varchar | 50 | 1 |  |  |  |
