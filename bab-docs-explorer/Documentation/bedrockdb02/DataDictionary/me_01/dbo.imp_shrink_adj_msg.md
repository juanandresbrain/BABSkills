# dbo.imp_shrink_adj_msg

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_shrink_adj_msg_id | decimal | 9 | 0 | YES |  |  |
| imp_shrink_adj_id | decimal | 9 | 1 |  |  |  |
| action | char | 1 | 0 |  |  |  |
| document_no | varchar | 20 | 0 |  |  |  |
| message_type | varchar | 20 | 0 |  |  |  |
| message_text | varchar | 255 | 0 |  |  |  |

