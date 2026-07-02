# dbo.deal_item_req

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| deal_item_req_id | int | 4 | 0 | YES |  |  |
| deal_id | int | 4 | 0 |  |  |  |
| deal_discount_id | int | 4 | 0 |  |  |  |
| identity_type | nvarchar | 8 | 0 |  |  |  |
| item_num | decimal | 9 | 1 |  |  |  |
| division_num | int | 4 | 1 |  |  |  |
| department_num | int | 4 | 1 |  |  |  |
| dept_group_num | int | 4 | 1 |  |  |  |
| class_num | int | 4 | 1 |  |  |  |
| item_group_num | int | 4 | 1 |  |  |  |
| quantity | decimal | 9 | 1 |  |  |  |

