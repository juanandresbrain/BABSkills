# dbo.message_attribute

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tran_type_id | int | 4 | 0 |  |  |  |
| attribute_id | int | 4 | 0 |  |  |  |
| attribute_name | varchar | 25 | 0 |  |  |  |
| data_type | int | 4 | 0 |  |  |  |
| data_length | int | 4 | 0 |  |  |  |
| scale | int | 4 | 0 |  |  |  |
| request_mandatory | int | 4 | 0 |  |  |  |
| reply_mandatory | int | 4 | 0 |  |  |  |
| reply_conf_mandatory | int | 4 | 0 |  |  |  |
| loopback_mandatory | int | 4 | 0 |  |  |  |
| reversal_mandatory | int | 4 | 0 |  |  |  |
| rev_reply_mandatory | int | 4 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
| row_id | int | 4 | 0 | YES |  |  |
