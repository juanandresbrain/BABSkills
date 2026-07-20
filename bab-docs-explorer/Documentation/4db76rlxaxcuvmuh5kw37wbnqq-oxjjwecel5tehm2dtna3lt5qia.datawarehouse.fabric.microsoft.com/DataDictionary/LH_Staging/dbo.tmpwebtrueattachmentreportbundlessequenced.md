# dbo.tmpwebtrueattachmentreportbundlessequenced

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sku | varchar | 8000 | 1 |  |  |  |
| QTY | int | 4 | 1 |  |  |  |
| ItemDescription | varchar | 8000 | 1 |  |  |  |
| Price | decimal | 9 | 1 |  |  |  |
| ParentItem | int | 4 | 1 |  |  |  |
| OrderNum | varchar | 8000 | 1 |  |  |  |
| OrderDate | datetime2 | 8 | 1 |  |  |  |
| OrderItemID | int | 4 | 1 |  |  |  |
| isParent | int | 4 | 1 |  |  |  |
| linkID | int | 4 | 1 |  |  |  |
| TransactionID | int | 4 | 1 |  |  |  |
| Rn_num | int | 4 | 1 |  |  |  |
