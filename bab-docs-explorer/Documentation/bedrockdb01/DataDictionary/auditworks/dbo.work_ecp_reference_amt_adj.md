# dbo.work_ecp_reference_amt_adj

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ecp_reference_amt_batch_id | binary | 16 | 0 |  |  |  |
| reference_amount_type | smallint | 2 | 0 |  |  |  |
| effective_from_datetime | datetime | 8 | 0 |  |  |  |
| period_end_datetime | datetime | 8 | 1 |  |  |  |
| adjustment_amount | money | 8 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| employee_no | int | 4 | 0 |  |  |  |
| selling_area_no | int | 4 | 0 |  |  |  |
| position_code | nvarchar | 8 | 0 |  |  |  |
| entry_id | numeric | 9 | 0 | YES |  |  |
