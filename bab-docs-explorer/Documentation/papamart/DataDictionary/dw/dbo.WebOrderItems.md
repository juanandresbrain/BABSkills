# dbo.WebOrderItems

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | int | 4 | 1 |  |  |  |
| OrderID | int | 4 | 1 |  |  |  |
| OrderItemID | int | 4 | 1 |  |  |  |
| SKU | varchar | 6 | 1 |  |  |  |
| Qty | int | 4 | 1 |  |  |  |
| ItemDescription | varchar | 100 | 1 |  |  |  |
| Price | money | 8 | 1 |  |  |  |
| DiscountedPrice | money | 8 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| TrackingNumber | varchar | 30 | 1 |  |  |  |
| product_key | int | 4 | 1 |  |  |  |
