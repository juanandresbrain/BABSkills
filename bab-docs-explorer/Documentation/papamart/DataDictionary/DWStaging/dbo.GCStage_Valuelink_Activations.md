# dbo.GCStage_Valuelink_Activations

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| activationDate | datetime | 8 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| terminal_id | int | 4 | 1 |  |  |  |
| terminal_transaction_number | bigint | 8 | 1 |  |  |  |
| account_number | varchar | 19 | 1 |  |  |  |
| transaction_amount | money | 8 | 1 |  |  |  |
| reversal_flag | char | 1 | 1 |  |  |  |
| LineID | int | 4 | 0 |  |  |  |
| merchant_id | varchar | 16 | 1 |  |  |  |
| postedPhase | int | 4 | 1 |  |  |  |
| gaRecID | int | 4 | 1 |  |  |  |
