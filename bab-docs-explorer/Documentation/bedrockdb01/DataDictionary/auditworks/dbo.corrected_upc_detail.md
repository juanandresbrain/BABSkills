# dbo.corrected_upc_detail

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| date_reject_id | tinyint | 1 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| transaction_no | trno | 4 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| salesperson | int | 4 | 1 |  |  |  |
| before_upc_no | numeric | 9 | 1 |  |  |  |
| after_upc_no | numeric | 9 | 0 |  |  |  |
| ticket_price | line_amount_18_4 | 9 | 0 |  |  |  |
| sold_at_price | line_amount_18_4 | 9 | 0 |  |  |  |
| last_modified_date_time | smalldatetime | 4 | 0 |  |  |  |
| function_no | tinyint | 1 | 0 |  |  |  |
| pos_identifier | nvarchar | 60 | 1 |  |  |  |
| pos_identifier_type | tinyint | 1 | 1 |  |  |  |
| cashier_no | int | 4 | 1 |  |  |  |
| user_id | int | 4 | 1 |  |  |  |
