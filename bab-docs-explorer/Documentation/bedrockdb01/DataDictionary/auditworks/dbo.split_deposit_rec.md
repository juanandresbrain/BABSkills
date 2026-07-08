# dbo.split_deposit_rec

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| deposit_destination | smallint | 2 | 1 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| deposit_category | smallint | 2 | 0 |  |  |  |
| deposit_source | smallint | 2 | 1 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| adj_drawn_from_deposit_date | smalldatetime | 4 | 0 |  |  |  |
| split_deposit_adjustment | money | 8 | 0 |  |  |  |
