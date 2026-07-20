# dbo.auditworks_av_transaction_header

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| av_transaction_id | decimal | 9 | 1 |  |  |  |
| store_no | int | 4 | 1 |  |  |  |
| register_no | int | 4 | 1 |  |  |  |
| transaction_date | datetime2 | 8 | 1 |  |  |  |
| date_reject_id | int | 4 | 1 |  |  |  |
| transaction_series | varchar | 8000 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| entry_date_time | datetime2 | 8 | 1 |  |  |  |
| cashier_no | int | 4 | 1 |  |  |  |
| transaction_category | int | 4 | 1 |  |  |  |
| tender_total | decimal | 9 | 1 |  |  |  |
| transaction_void_flag | int | 4 | 1 |  |  |  |
| customer_info_exists | int | 4 | 1 |  |  |  |
| exception_flag | int | 4 | 1 |  |  |  |
| sa_rejection_flag | int | 4 | 1 |  |  |  |
| if_rejection_flag | int | 4 | 1 |  |  |  |
| deposit_declaration_flag | int | 4 | 1 |  |  |  |
| closeout_flag | int | 4 | 1 |  |  |  |
| media_count_flag | int | 4 | 1 |  |  |  |
| customer_modified_flag | int | 4 | 1 |  |  |  |
| tax_override_flag | int | 4 | 1 |  |  |  |
| pos_tax_jurisdiction | varchar | 8000 | 1 |  |  |  |
| edit_progress_flag | int | 4 | 1 |  |  |  |
| edit_timestamp | float | 8 | 1 |  |  |  |
| employee_no | int | 4 | 1 |  |  |  |
| transaction_remark | varchar | 8000 | 1 |  |  |  |
| copy_transaction_id | decimal | 9 | 1 |  |  |  |
| last_modified_date_time | datetime2 | 8 | 1 |  |  |  |
| in_use_timestamp | datetime2 | 8 | 1 |  |  |  |
| till_no | int | 4 | 1 |  |  |  |
| updated_by_user_id | int | 4 | 1 |  |  |  |
