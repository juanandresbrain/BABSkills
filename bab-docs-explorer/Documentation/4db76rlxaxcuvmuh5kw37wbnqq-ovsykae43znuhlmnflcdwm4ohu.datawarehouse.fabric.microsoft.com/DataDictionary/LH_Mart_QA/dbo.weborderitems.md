# dbo.weborderitems

**Database:** LH_Mart_QA  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | int | 4 | 1 |  |  |  |
| OrderID | int | 4 | 1 |  |  |  |
| OrderItemID | int | 4 | 1 |  |  |  |
| SKU | varchar | 8000 | 1 |  |  |  |
| Qty | int | 4 | 1 |  |  |  |
| ItemDescription | varchar | 8000 | 1 |  |  |  |
| Price | decimal | 9 | 1 |  |  |  |
| DiscountedPrice | decimal | 9 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| TrackingNumber | varchar | 8000 | 1 |  |  |  |
| product_key | int | 4 | 1 |  |  |  |
