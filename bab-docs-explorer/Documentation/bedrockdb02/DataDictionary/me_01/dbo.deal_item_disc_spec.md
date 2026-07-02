# dbo.deal_item_disc_spec

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| deal_item_disc_spec_id | int | 4 | 0 | YES |  |  |
| deal_id | int | 4 | 0 |  |  |  |
| deal_discount_id | int | 4 | 0 |  |  |  |
| identity_type | nvarchar | 8 | 0 |  |  |  |
| item_num | decimal | 9 | 1 |  |  |  |
| division_num | int | 4 | 1 |  |  |  |
| department_num | int | 4 | 1 |  |  |  |
| dept_group_num | int | 4 | 1 |  |  |  |
| class_num | int | 4 | 1 |  |  |  |
| item_group_num | int | 4 | 1 |  |  |  |
| quantity | tinyint | 1 | 1 |  |  |  |
| disc_type | nvarchar | 8 | 0 |  |  |  |
| disc_pct | decimal | 5 | 1 |  |  |  |
| disc_amt | decimal | 9 | 1 |  |  |  |
| disc_applies_to | nvarchar | 8 | 1 |  |  |  |

