# dbo.Md_FieldPeriodGroup

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| field_period_group_id | int | 4 | 0 | YES |  |  |
| topic_id | int | 4 | 0 |  |  |  |
| label_1 | varchar | 30 | 0 |  |  |  |
| label_2 | varchar | 30 | 0 |  |  |  |
| description_1 | varchar | 255 | 1 |  |  |  |
| description_2 | varchar | 255 | 1 |  |  |  |
| label_resource_name | nvarchar | 510 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| description_resource_name | nvarchar | 510 | 1 |  |  |  |

