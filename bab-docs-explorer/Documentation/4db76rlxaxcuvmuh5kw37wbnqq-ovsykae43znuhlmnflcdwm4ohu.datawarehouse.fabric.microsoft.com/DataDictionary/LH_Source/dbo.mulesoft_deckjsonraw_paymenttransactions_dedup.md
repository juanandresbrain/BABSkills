# dbo.mulesoft_deckjsonraw_paymenttransactions_dedup

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| _RowIndex | bigint | 8 | 1 |  |  |  |
| _ParentKeyField | bigint | 8 | 1 |  |  |  |
| PaymentTransactionID | bigint | 8 | 1 |  |  |  |
| OrderPaymentId | bigint | 8 | 1 |  |  |  |
| PaymentTransactionTypeId | bigint | 8 | 1 |  |  |  |
| Amount | real | 4 | 1 |  |  |  |
| EarlyCaptureAmount | real | 4 | 1 |  |  |  |
| Generic1 | varchar | 8000 | 1 |  |  |  |
| Generic2 | varchar | 8000 | 1 |  |  |  |
| Generic3 | varchar | 8000 | 1 |  |  |  |
| Generic4 | varchar | 8000 | 1 |  |  |  |
| Generic5 | varchar | 8000 | 1 |  |  |  |
| TransactionDateUTC | datetime2 | 8 | 1 |  |  |  |
| IsDecline | bit | 1 | 1 |  |  |  |
| PaymentResponseCodeGroup | bigint | 8 | 1 |  |  |  |
| ParentTransactionID | varchar | 8000 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| JSONDate | datetime2 | 8 | 1 |  |  |  |
