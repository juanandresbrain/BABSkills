# dbo.service_usage_test

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| route_id | int | 4 | 0 |  |  |  |
| test_sequence | int | 4 | 0 |  |  |  |
| tran_type_id | int | 4 | 1 |  |  |  |
| data_source | int | 4 | 0 |  |  |  |
| internal_type | int | 4 | 1 |  |  |  |
| attribute_id | int | 4 | 1 |  |  |  |
| operator | varchar | 2 | 0 |  |  |  |
| field_value | varchar | 25 | 1 |  |  |  |
| expression_operator | varchar | 3 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
| row_id | int | 4 | 0 | YES |  |  |
