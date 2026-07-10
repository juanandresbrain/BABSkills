# dbo.DynamicsTransactionUpdateLog

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DynamicsTransactionUpdateLogId | int | 4 | 0 | YES |  |  |
| TableName | varchar | 50 | 1 |  |  |  |
| RecordId | int | 4 | 1 |  |  |  |
| RetailReceiptId | varchar | 18 | 1 |  |  |  |
| UpdateProcessed | datetime | 8 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| BatchID | nvarchar | 200 | 1 |  |  |  |
