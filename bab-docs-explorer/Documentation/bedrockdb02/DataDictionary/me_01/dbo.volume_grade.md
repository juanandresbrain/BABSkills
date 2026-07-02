# dbo.volume_grade

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| volume_grade_id | bigint | 8 | 0 | YES |  |  |
| hierarchy_group_id | int | 4 | 0 | YES |  |  |
| grade_code | nvarchar | 20 | 0 |  |  |  |
| sales_lower_limit | decimal | 5 | 0 |  |  |  |
| minimum | int | 4 | 0 |  |  |  |
| maximum | int | 4 | 0 |  |  |  |
| style_minimum | int | 4 | 0 |  |  |  |
| style_maximum | int | 4 | 0 |  |  |  |
| weight | decimal | 5 | 0 |  |  |  |

