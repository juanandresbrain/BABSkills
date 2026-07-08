# dbo.import_banking

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| INSTN_NUM | int | 4 | 0 |  |  |  |
| BANK_BRNCH_NUM | nchar | 12 | 0 |  |  |  |
| BANK_ACNT_NUM | nvarchar | 50 | 0 |  |  |  |
| posting_datetime | datetime | 8 | 0 |  |  |  |
| posting_amount | line_amount_18_4 | 9 | 0 |  |  |  |
| posting_quantity | line_amount_18_4 | 9 | 1 |  |  |  |
| reference_set_type | nvarchar | 40 | 1 |  |  |  |
| foreign_currency_code | nvarchar | 6 | 1 |  |  |  |
| foreign_currency_amount | line_amount_18_4 | 9 | 1 |  |  |  |
| reference_number | int | 4 | 1 |  |  |  |
| reference_datetime | datetime | 8 | 1 |  |  |  |
| reference_string_1 | nvarchar | 510 | 1 |  |  |  |
| reference_string_2 | nvarchar | 510 | 1 |  |  |  |
| transaction_reference_no | nvarchar | 40 | 1 |  |  |  |
| entry_id | numeric | 9 | 0 | YES |  |  |
| BANK_ACNT_ID | smallint | 2 | 1 |  |  |  |
| BANK_ID | binary | 16 | 1 |  |  |  |
| store_no | int | 4 | 1 |  |  |  |
| originating_store_no | int | 4 | 1 |  |  |  |
| system_code | nvarchar | 20 | 1 |  |  |  |
| export_flag | tinyint | 1 | 1 |  |  |  |
