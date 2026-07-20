# dbo.gcstage_valuelink_activations

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| activationDate | datetime2 | 8 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| terminal_id | int | 4 | 1 |  |  |  |
| terminal_transaction_number | bigint | 8 | 1 |  |  |  |
| account_number | varchar | 8000 | 1 |  |  |  |
| transaction_amount | decimal | 9 | 1 |  |  |  |
| reversal_flag | varchar | 8000 | 1 |  |  |  |
| LineID | int | 4 | 1 |  |  |  |
| merchant_id | varchar | 8000 | 1 |  |  |  |
| postedPhase | int | 4 | 1 |  |  |  |
| gaRecID | int | 4 | 1 |  |  |  |
