# dbo.media_reconciliation

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| cashier_no | int | 4 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| acceptable_short_limit | money | 8 | 0 |  |  |  |
| media_not_counted | tinyint | 1 | 0 |  |  |  |
| variance_is_short | tinyint | 1 | 0 |  |  |  |
| variance_is_lost_doc | tinyint | 1 | 0 |  |  |  |
| media_rec_verified | tinyint | 1 | 0 |  |  |  |
| deposit_category | smallint | 2 | 0 |  |  |  |
| deposit_destination | smallint | 2 | 0 |  |  |  |
| deposit_source | smallint | 2 | 0 |  |  |  |
| edit_timestamp | float | 8 | 0 |  |  |  |
| expected_media_amount | money | 8 | 0 |  |  |  |
| expected_exchange_amount | money | 8 | 0 |  |  |  |
| counted_media_amount | money | 8 | 0 |  |  |  |
| pickup_loan_amount | money | 8 | 0 |  |  |  |
| declared_deposit_amount | money | 8 | 0 |  |  |  |
| tender_short | money | 8 | 0 |  |  |  |
| remark | nvarchar | 510 | 1 |  |  |  |
| in_use_timestamp | smalldatetime | 4 | 1 |  |  |  |
| in_use_user_name | varchar | 25 | 1 |  |  |  |
