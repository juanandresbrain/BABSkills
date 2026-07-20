# dbo.tmpsummaryredemptions

**Database:** LH_Staging_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| account_number | varchar | 8000 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| terminal_id | int | 4 | 1 |  |  |  |
| terminal_transaction_number | bigint | 8 | 1 |  |  |  |
| transaction_amount | decimal | 17 | 1 |  |  |  |
| LineID | int | 4 | 1 |  |  |  |
| gaRecID | int | 4 | 1 |  |  |  |
| postedPhase | int | 4 | 1 |  |  |  |
