# dbo.interface

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tran_type_id | int | 4 | 0 |  |  |  |
| interface_id | int | 4 | 0 |  |  |  |
| interface_name | varchar | 25 | 0 |  |  |  |
| request_message_id | int | 4 | 0 |  |  |  |
| reply_message_id | int | 4 | 0 |  |  |  |
| reply_conf_message_id | int | 4 | 0 |  |  |  |
| reversal_message_id | int | 4 | 0 |  |  |  |
| rev_reply_message_id | int | 4 | 0 |  |  |  |
| reply_stat_message_id | int | 4 | 0 |  |  |  |
| loopback_message_id | int | 4 | 0 |  |  |  |
| field_loopback_code | int | 4 | 0 |  |  |  |
| field_loopback_mess | varchar | 255 | 0 |  |  |  |
| attr_loopback_code | int | 4 | 0 |  |  |  |
| attr_loopback_mess | varchar | 255 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
| row_id | int | 4 | 0 | YES |  |  |
