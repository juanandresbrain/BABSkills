# dbo.imp_user_def_adj_msg

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_user_def_adj_msg_id | decimal | 9 | 0 | YES |  |  |
| imp_user_def_adj_id | decimal | 9 | 1 |  |  |  |
| action | nchar | 2 | 0 |  |  |  |
| document_no | nvarchar | 40 | 0 |  |  |  |
| message_type | nvarchar | 40 | 0 |  |  |  |
| message_text | nvarchar | 510 | 0 |  |  |  |

