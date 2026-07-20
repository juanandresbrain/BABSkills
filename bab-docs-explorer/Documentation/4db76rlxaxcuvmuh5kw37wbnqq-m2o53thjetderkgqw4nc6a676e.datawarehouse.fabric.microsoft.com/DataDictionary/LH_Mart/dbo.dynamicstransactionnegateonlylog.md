# dbo.dynamicstransactionnegateonlylog

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DynamicsTransactionUpdateLogId | int | 4 | 1 |  |  |  |
| TableName | varchar | 8000 | 1 |  |  |  |
| RecordId | int | 4 | 1 |  |  |  |
| RetailReceiptId | varchar | 8000 | 1 |  |  |  |
| UpdateProcessed | datetime2 | 8 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| BatchID | varchar | 8000 | 1 |  |  |  |
