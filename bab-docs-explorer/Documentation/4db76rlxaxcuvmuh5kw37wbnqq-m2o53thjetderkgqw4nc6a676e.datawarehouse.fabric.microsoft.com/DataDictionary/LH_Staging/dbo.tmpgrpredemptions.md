# dbo.tmpgrpredemptions

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| account_number | varchar | 8000 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| terminal_id | int | 4 | 1 |  |  |  |
| terminal_transaction_number | bigint | 8 | 1 |  |  |  |
| lineID | int | 4 | 1 |  |  |  |
| postedPhase | int | 4 | 1 |  |  |  |
| transaction_amount | decimal | 17 | 1 |  |  |  |
| grRecID | int | 4 | 1 |  |  |  |
