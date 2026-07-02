# dbo.plan_exp_element_fields

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| plan_exp_table_group_id | smallint | 2 | 0 |  |  |  |
| plan_exp_field | nvarchar | 60 | 0 |  |  |  |
| plan_exp_field_name | nvarchar | 60 | 0 |  |  |  |
| plan_exp_expression | nvarchar | 200 | 1 |  |  |  |
| plan_exp_lookup_sql | nvarchar | 2000 | 1 |  |  |  |
| expression_flag | bit | 1 | 0 |  |  |  |
| plan_exp_field_local | nvarchar | 100 | 1 |  |  |  |

