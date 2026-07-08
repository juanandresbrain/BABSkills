# dbo.employee_productivity_comment

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ecp_comment_id | numeric | 9 | 0 | YES |  |  |
| period_end_datetime | datetime | 8 | 0 |  |  |  |
| calendar_level | smallint | 2 | 0 |  |  |  |
| employee_no | int | 4 | 0 |  |  |  |
| entry_datetime | datetime | 8 | 0 |  |  |  |
| user_id | numeric | 9 | 1 |  |  |  |
| comment | nvarchar | 6000 | 0 |  |  |  |
| private | tinyint | 1 | 0 |  |  |  |
| deletion_datetime | datetime | 8 | 1 |  |  |  |
| home_store_no | int | 4 | 1 |  |  |  |
| primary_position | nvarchar | 8 | 1 |  |  |  |
| primary_selling_area_no | int | 4 | 1 |  |  |  |
| relationship_set_id | numeric | 9 | 1 |  |  |  |
