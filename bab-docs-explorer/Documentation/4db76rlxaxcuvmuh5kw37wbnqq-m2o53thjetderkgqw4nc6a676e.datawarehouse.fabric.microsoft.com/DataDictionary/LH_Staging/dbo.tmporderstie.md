# dbo.tmporderstie

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RetailTransactionId | varchar | 8000 | 1 |  |  |  |
| RetailReceiptId | varchar | 8000 | 1 |  |  |  |
| TransDate | date | 3 | 1 |  |  |  |
| Entity | varchar | 8000 | 1 |  |  |  |
| GrossAmount | decimal | 9 | 1 |  |  |  |
| PaymentTotal | decimal | 9 | 1 |  |  |  |
| Variance | decimal | 9 | 1 |  |  |  |
