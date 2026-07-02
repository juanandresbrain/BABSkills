# dbo.gl_component

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| gl_component_id | decimal | 9 | 0 | YES |  |  |
| gl_component_label | nvarchar | 120 | 0 |  |  |  |
| debit_account_id | decimal | 9 | 0 |  |  |  |
| credit_account_id | decimal | 9 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |

