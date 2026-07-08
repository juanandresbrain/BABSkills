# dbo.message_attribute

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tran_type_id | int | 4 | 0 |  |  |  |
| attribute_id | int | 4 | 0 |  |  |  |
| attribute_name | nvarchar | 50 | 0 |  |  |  |
| data_type | int | 4 | 0 |  |  |  |
| data_length | int | 4 | 0 |  |  |  |
| scale | int | 4 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
| row_id | int | 4 | 0 | YES |  |  |
