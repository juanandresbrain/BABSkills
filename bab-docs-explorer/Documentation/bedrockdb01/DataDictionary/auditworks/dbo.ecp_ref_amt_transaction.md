# dbo.ecp_ref_amt_transaction

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| reference_amount_type | smallint | 2 | 0 |  |  |  |
| ref_amt_datetime | datetime | 8 | 0 |  |  |  |
| ref_amt_interval_from_datetime | datetime | 8 | 1 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| selling_area_no | int | 4 | 0 |  |  |  |
| position_code | nvarchar | 8 | 0 |  |  |  |
| employee_no | int | 4 | 0 |  |  |  |
| reference_amount | money | 8 | 0 |  |  |  |
| if_entry_no | numeric | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| transaction_id | numeric | 9 | 0 |  |  |  |
| current_flag | tinyint | 1 | 0 |  |  |  |
| effective_from_datetime | datetime | 8 | 0 |  |  |  |
| ecp_reference_amt_id | numeric | 9 | 1 |  |  |  |
