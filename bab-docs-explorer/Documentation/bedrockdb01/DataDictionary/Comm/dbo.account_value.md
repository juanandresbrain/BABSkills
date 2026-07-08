# dbo.account_value

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tran_type_id | int | 4 | 0 |  |  |  |
| message_id | int | 4 | 0 |  |  |  |
| message_role | int | 4 | 0 |  |  |  |
| test_sequence | int | 4 | 0 |  |  |  |
| account_type_id | int | 4 | 1 |  |  |  |
| field_id | int | 4 | 0 |  |  |  |
| operator | varchar | 2 | 0 |  |  |  |
| field_value | nvarchar | 50 | 0 |  |  |  |
| expression_operator | varchar | 3 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
| row_id | int | 4 | 0 | YES |  |  |
| DATA_SRC | int | 4 | 0 |  |  |  |
| INTRNL_TYPE | int | 4 | 0 |  |  |  |
| ATRBT_ID | int | 4 | 0 |  |  |  |
