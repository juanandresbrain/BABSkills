# dbo.work_rec_float_load

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| store_no | int | 4 | 1 |  |  |  |
| register_no | smallint | 2 | 1 |  |  |  |
| bank_no | smallint | 2 | 1 |  |  |  |
| till_no | smallint | 2 | 1 |  |  |  |
| cashier_no | int | 4 | 1 |  |  |  |
| initial_float_amount | money | 8 | 1 |  |  |  |
| work_tb_entry_date_time | datetime | 8 | 1 |  |  |  |
