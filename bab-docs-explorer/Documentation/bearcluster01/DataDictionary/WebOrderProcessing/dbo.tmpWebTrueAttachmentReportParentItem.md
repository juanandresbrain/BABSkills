# dbo.tmpWebTrueAttachmentReportParentItem

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sku | varchar | 50 | 1 |  |  |  |
| QTY | int | 4 | 1 |  |  |  |
| ItemDescription | varchar | 100 | 1 |  |  |  |
| Price | money | 8 | 1 |  |  |  |
| ParentItem | int | 4 | 1 |  |  |  |
| OrderNum | varchar | 10 | 1 |  |  |  |
| OrderDate | datetime | 8 | 1 |  |  |  |
| OrderItemID | int | 4 | 1 |  |  |  |
| isParent | int | 4 | 1 |  |  |  |
| linkID | int | 4 | 1 |  |  |  |
| TransactionID | int | 4 | 1 |  |  |  |

