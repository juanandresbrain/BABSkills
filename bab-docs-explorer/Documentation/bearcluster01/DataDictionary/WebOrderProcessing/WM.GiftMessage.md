# WM.GiftMessage

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| GiftMessageId | int | 4 | 0 | YES |  |  |
| GiftMessageToken | uniqueidentifier | 16 | 0 | YES |  |  |
| GiftMessage | nvarchar | 702 | 0 |  |  |  |
| StyleCode | varchar | 50 | 0 |  |  |  |
| OrderItemID | int | 4 | 1 |  |  |  |
| CreatedOn | datetime | 8 | 0 |  |  |  |
| CreatedBy | varchar | 255 | 0 |  |  |  |
| UpdatedOn | datetime | 8 | 1 |  |  |  |
| UpdatedBy | varchar | 255 | 1 |  |  |  |

