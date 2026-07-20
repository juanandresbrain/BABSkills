# dbo.azure_web_oder_items

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

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
| InsertDate | date | 3 | 1 |  |  |  |
| UpdateDate | date | 3 | 1 |  |  |  |
| TrackingNumber | varchar | 8000 | 1 |  |  |  |
| product_key | int | 4 | 1 |  |  |  |
