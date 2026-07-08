# dbo.basic_mdse_interface

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| upc_lookup_division | char | 2 | 0 |  |  |  |
| store_no | char | 3 | 0 |  |  |  |
| register_no | char | 5 | 0 |  |  |  |
| transaction_date | char | 8 | 0 |  |  |  |
| transaction_no | char | 4 | 0 |  |  |  |
| upc_no | char | 14 | 0 |  |  |  |
| units | int | 4 | 0 |  |  |  |
| gross_sales_amount | int | 4 | 0 |  |  |  |
| pos_discount_amount | int | 4 | 0 |  |  |  |
| employee_discount_amount | int | 4 | 0 |  |  |  |
| salesperson | char | 9 | 0 |  |  |  |
| if_entry_no | if_entry_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
