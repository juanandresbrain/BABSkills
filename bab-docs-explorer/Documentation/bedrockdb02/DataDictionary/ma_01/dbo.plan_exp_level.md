# dbo.plan_exp_level

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| plan_exp_level_id | smallint | 2 | 0 | YES |  |  |
| plan_exp_level_label | nvarchar | 60 | 0 |  |  |  |
| merchandise_field_name | nvarchar | 100 | 0 |  |  |  |
| location_field_name | nvarchar | 60 | 1 |  |  |  |
| time_period_field_name | nvarchar | 100 | 0 |  |  |  |
| period_indicator | nchar | 2 | 0 |  |  |  |
| additional_from_clause | nvarchar | 2000 | 1 |  |  |  |
| additional_where_clause | nvarchar | 2000 | 1 |  |  |  |
| batch_column_name | nvarchar | 60 | 0 |  |  |  |
| batch_size | smallint | 2 | 0 |  |  |  |
| export_flag | bit | 1 | 0 |  |  |  |
| default_export_flag | bit | 1 | 0 |  |  |  |
| distinct_list_sql | nvarchar | 2000 | 0 |  |  |  |
| location_indicator | nchar | 2 | 0 |  |  |  |
| list_table_name | nvarchar | 60 | 0 |  |  |  |
| list_table_where_clause | nvarchar | 2000 | 0 |  |  |  |

