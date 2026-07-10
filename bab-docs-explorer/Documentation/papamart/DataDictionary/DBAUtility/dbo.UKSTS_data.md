# dbo.UKSTS_data

**Database:** DBAUtility  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FileID | int | 4 | 0 |  |  |  |
| LineID | int | 4 | 0 |  |  |  |
| period_start_date | datetime | 8 | 1 |  |  |  |
| store_id | int | 4 | 1 |  |  |  |
| item_num | int | 4 | 1 |  |  |  |
| transaction_amount | money | 8 | 1 |  |  |  |
| exported_date | datetime | 8 | 1 |  |  |  |
