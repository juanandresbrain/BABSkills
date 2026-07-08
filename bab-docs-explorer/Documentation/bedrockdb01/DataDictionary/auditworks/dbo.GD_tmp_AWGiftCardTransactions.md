# dbo.GD_tmp_AWGiftCardTransactions

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | numeric | 9 | 1 |  |  |  |
| store_no | int | 4 | 1 |  |  |  |
| register_no | smallint | 2 | 1 |  |  |  |
| transaction_date | smalldatetime | 4 | 1 |  |  |  |
| date_reject_id | tinyint | 1 | 1 |  |  |  |
| transaction_series | char | 1 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| entry_date_time | datetime | 8 | 1 |  |  |  |
| cashier_no | int | 4 | 1 |  |  |  |
| transaction_category | tinyint | 1 | 1 |  |  |  |
| tender_total | money | 8 | 1 |  |  |  |
| transaction_void_flag | smallint | 2 | 1 |  |  |  |
| customer_info_exists | tinyint | 1 | 1 |  |  |  |
| exception_flag | tinyint | 1 | 1 |  |  |  |
| sa_rejection_flag | tinyint | 1 | 1 |  |  |  |
| if_rejection_flag | tinyint | 1 | 1 |  |  |  |
| deposit_declaration_flag | tinyint | 1 | 1 |  |  |  |
| closeout_flag | tinyint | 1 | 1 |  |  |  |
| media_count_flag | tinyint | 1 | 1 |  |  |  |
| customer_modified_flag | tinyint | 1 | 1 |  |  |  |
| tax_override_flag | tinyint | 1 | 1 |  |  |  |
| pos_tax_jurisdiction | char | 5 | 1 |  |  |  |
| edit_progress_flag | tinyint | 1 | 1 |  |  |  |
| employee_no | int | 4 | 1 |  |  |  |
| transaction_remark | varchar | 1000 | 1 |  |  |  |
| copy_transaction_id | numeric | 9 | 1 |  |  |  |
| last_modified_date_time | smalldatetime | 4 | 1 |  |  |  |
| in_use_timestamp | smalldatetime | 4 | 1 |  |  |  |
| updated_by_user_name | varchar | 25 | 1 |  |  |  |
| till_no | smallint | 2 | 1 |  |  |  |
| line_id | numeric | 5 | 1 |  |  |  |
| line_sequence | numeric | 5 | 1 |  |  |  |
| line_object_type | tinyint | 1 | 1 |  |  |  |
| line_object | smallint | 2 | 1 |  |  |  |
| line_action | tinyint | 1 | 1 |  |  |  |
| gross_line_amount | numeric | 9 | 1 |  |  |  |
| pos_discount_amount | numeric | 9 | 1 |  |  |  |
| db_cr_none | smallint | 2 | 1 |  |  |  |
| attachment_qty | tinyint | 1 | 1 |  |  |  |
| interface_rejection_flag | tinyint | 1 | 1 |  |  |  |
| line_void_flag | tinyint | 1 | 1 |  |  |  |
| voiding_reversal_flag | smallint | 2 | 1 |  |  |  |
| reference_type | tinyint | 1 | 1 |  |  |  |
| reference_no | varchar | 80 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| actual_date | datetime | 8 | 1 |  |  |  |
| fiscal_year | int | 4 | 1 |  |  |  |
| season | varchar | 20 | 1 |  |  |  |
| fiscal_quarter | int | 4 | 1 |  |  |  |
| fiscal_period | int | 4 | 1 |  |  |  |
| fiscal_week | int | 4 | 1 |  |  |  |
| month | int | 4 | 1 |  |  |  |
| year | int | 4 | 1 |  |  |  |
| month_name | varchar | 20 | 1 |  |  |  |
| day_of_month | int | 4 | 1 |  |  |  |
| day_of_year | int | 4 | 1 |  |  |  |
| day_name | varchar | 20 | 1 |  |  |  |
| weekend_y_n | varchar | 20 | 1 |  |  |  |
| day_of_week | int | 4 | 1 |  |  |  |
| week_of_period | int | 4 | 1 |  |  |  |
| week_of_quarter | int | 4 | 1 |  |  |  |
| period_of_quarter | int | 4 | 1 |  |  |  |
| day_id | int | 4 | 1 |  |  |  |
| holiday_period_code | varchar | 20 | 1 |  |  |  |
| week_id | int | 4 | 1 |  |  |  |
| period_id | int | 4 | 1 |  |  |  |
| quarter_id | int | 4 | 1 |  |  |  |
| org_fiscal_quarter | int | 4 | 1 |  |  |  |
| org_fiscal_period | int | 4 | 1 |  |  |  |
| org_fiscal_week | int | 4 | 1 |  |  |  |
| org_week_of_period | int | 4 | 1 |  |  |  |
| org_week_of_quarter | int | 4 | 1 |  |  |  |
| org_period_of_quarter | int | 4 | 1 |  |  |  |
