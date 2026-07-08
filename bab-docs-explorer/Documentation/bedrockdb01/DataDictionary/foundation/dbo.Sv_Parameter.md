# dbo.Sv_Parameter

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| topic_id | int | 4 | 0 |  |  |  |
| db_group_id | int | 4 | 0 |  |  |  |
| app_id | int | 4 | 0 |  |  |  |
| parameter_key | varchar | 30 | 0 |  |  |  |
| parameter_value | varchar | 50 | 1 |  |  |  |
| label_1 | varchar | 60 | 1 |  |  |  |
| label_2 | varchar | 60 | 1 |  |  |  |
| description_1 | varchar | 255 | 1 |  |  |  |
| description_2 | varchar | 255 | 1 |  |  |  |
| max_value | varchar | 50 | 1 |  |  |  |
| min_value | varchar | 50 | 1 |  |  |  |
| default_value | varchar | 50 | 0 |  |  |  |
| data_type | varchar | 20 | 0 |  |  |  |
| parameter_modifiable | tinyint | 1 | 1 |  |  |  |
