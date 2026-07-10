# dbo.Ld_POS_Audits

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | numeric | 9 | 1 |  |  |  |
| modified_date | datetime | 8 | 1 |  |  |  |
| entry_date | datetime | 8 | 1 |  |  |  |
| transaction_date | datetime | 8 | 1 |  |  |  |
| store_id | int | 4 | 1 |  |  |  |
| register_no | int | 4 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| dm_deleted_y_n | char | 1 | 1 |  |  |  |
| dm_deleted_date | datetime | 8 | 1 |  |  |  |
| seqno | int | 4 | 0 | YES |  |  |
