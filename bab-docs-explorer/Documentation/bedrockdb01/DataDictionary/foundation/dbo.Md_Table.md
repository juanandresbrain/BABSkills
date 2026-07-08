# dbo.Md_Table

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| table_id | int | 4 | 0 |  |  |  |
| table_name | varchar | 30 | 0 |  |  |  |
| pre_code | text | 16 | 1 |  |  |  |
| post_code | text | 16 | 1 |  |  |  |
| db_alias_id | int | 4 | 0 |  |  |  |
| topic_id | int | 4 | 0 |  |  |  |
| apply_period | bit | 1 | 0 |  |  |  |
| multiple_names | bit | 1 | 0 |  |  |  |
| priority | int | 4 | 1 |  |  |  |
| note | varchar | 60 | 1 |  |  |  |
| where_clause | varchar | 512 | 1 |  |  |  |
