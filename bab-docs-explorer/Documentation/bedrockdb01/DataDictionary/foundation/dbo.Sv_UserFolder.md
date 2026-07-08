# dbo.Sv_UserFolder

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| folder_id | int | 4 | 0 |  |  |  |
| user_id | int | 4 | 0 |  |  |  |
| topic_id | int | 4 | 0 |  |  |  |
| folder_type | smallint | 2 | 0 |  |  |  |
| folder_level | smallint | 2 | 0 |  |  |  |
| folder_name | nvarchar | 60 | 0 |  |  |  |
| period_id | int | 4 | 1 |  |  |  |
