# dbo.message_field_test

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| message_id | int | 4 | 0 |  |  |  |
| field_id | int | 4 | 0 |  |  |  |
| test_sequence | int | 4 | 0 |  |  |  |
| operator | varchar | 2 | 0 |  |  |  |
| field_value | varchar | 25 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
| row_id | int | 4 | 0 | YES |  |  |
