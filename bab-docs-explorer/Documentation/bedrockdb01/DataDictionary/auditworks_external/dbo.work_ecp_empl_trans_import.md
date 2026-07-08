# dbo.work_ecp_empl_trans_import

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | numeric | 9 | 0 |  |  |  |
| if_entry_no | numeric | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| calendar_level | smallint | 2 | 0 |  |  |  |
| period_end_datetime | datetime | 8 | 0 |  |  |  |
| pay_period_end_datetime | datetime | 8 | 0 |  |  |  |
| calendar_level_seq | smallint | 2 | 0 |  |  |  |
| employee_no | int | 4 | 0 |  |  |  |
| employee_transaction_role | nvarchar | 40 | 0 |  |  |  |
| primary_position | nvarchar | 8 | 1 |  |  |  |
| primary_selling_area_no | int | 4 | 1 |  |  |  |
| employee_commission_code | nvarchar | 40 | 1 |  |  |  |
| transaction_store_no | int | 4 | 0 |  |  |  |
| transaction_commission_code | nvarchar | 40 | 0 |  |  |  |
| transaction_net_amount | money | 8 | 0 |  |  |  |
| transaction_discount_amount | money | 8 | 0 |  |  |  |
| transaction_units | numeric | 9 | 0 |  |  |  |
| store_commission_code | nvarchar | 40 | 1 |  |  |  |
| item_commission_code | nvarchar | 40 | 1 |  |  |  |
| interface_control_flag | numeric | 9 | 0 |  |  |  |
| commission_rate | numeric | 5 | 0 |  |  |  |
| commission_amount_per_item | money | 8 | 0 |  |  |  |
| employee_ecp_rate_id | numeric | 9 | 1 |  |  |  |
| tier_accumulation_basis | smallint | 2 | 1 |  |  |  |
| tier_id | numeric | 5 | 0 |  |  |  |
| max_serial_no | numeric | 9 | 0 |  |  |  |
| empl_trans_summary_id | numeric | 9 | 1 |  |  |  |
| new_flag | tinyint | 1 | 1 |  |  |  |
| source_allocation_type | nvarchar | 40 | 1 |  |  |  |
| source_empl_trans_summary_id | numeric | 9 | 1 |  |  |  |
| commission_amount | money | 8 | 1 |  |  |  |
| merch_serv_flag | nvarchar | 40 | 0 |  |  |  |
| home_store_no | int | 4 | 1 |  |  |  |
| relationship_set_id | numeric | 9 | 1 |  |  |  |
| copy_transaction_quantity | money | 8 | 1 |  |  |  |
| copy_transaction_quantity_adj | money | 8 | 1 |  |  |  |
| copy_transaction_qty_adj_mdsfe | money | 8 | 1 |  |  |  |
