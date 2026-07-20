# dbo.weborderprocessing_wm_itemstatus

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderItemStatusId | int | 4 | 1 |  |  |  |
| OrderItemID | int | 4 | 1 |  |  |  |
| Status | varchar | 8000 | 1 |  |  |  |
| StatusDate | datetime2 | 8 | 1 |  |  |  |
| CurrentStatus | bit | 1 | 1 |  |  |  |
| OrderID | int | 4 | 1 |  |  |  |
| OrderTransactionIdentifier | int | 4 | 1 |  |  |  |
| QTY | int | 4 | 1 |  |  |  |
| Price | decimal | 9 | 1 |  |  |  |
| DiscountedPrice | decimal | 9 | 1 |  |  |  |
