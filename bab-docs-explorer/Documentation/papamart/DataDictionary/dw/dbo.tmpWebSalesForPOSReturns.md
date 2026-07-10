# dbo.tmpWebSalesForPOSReturns

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LocationCode | varchar | 4 | 0 |  |  |  |
| OrderNumber | varchar | 10 | 1 |  |  |  |
| OrderDate | datetime | 8 | 0 |  |  |  |
| PaymentMethod | varchar | 50 | 1 |  |  |  |
| CustomerNumber | varchar | 20 | 1 |  |  |  |
| sku | varchar | 50 | 0 |  |  |  |
| ItemDescription | varchar | 100 | 1 |  |  |  |
| qty | int | 4 | 0 |  |  |  |
| PricePer | money | 8 | 1 |  |  |  |
| DiscountedPrice | money | 8 | 1 |  |  |  |
| Tax | decimal | 5 | 1 |  |  |  |
| ItemLevelTax | numeric | 5 | 1 |  |  |  |
| Tender | numeric | 13 | 1 |  |  |  |
| currency_code | varchar | 3 | 1 |  |  |  |
