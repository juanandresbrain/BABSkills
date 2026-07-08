# dbo.ecp_query_preferences

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| unique_id | int | 4 | 0 | YES |  |  |
| criteria_list | text | 16 | 1 |  |  |  |
| user_id | int | 4 | 0 |  |  |  |
| company_id | int | 4 | 1 |  |  |  |
| application_id | smallint | 2 | 1 |  |  |  |
| query_name | nvarchar | 200 | 1 |  |  |  |
| query_type | int | 4 | 1 |  |  |  |
| query_description | nvarchar | 510 | 1 |  |  |  |
| report_identifier | nvarchar | 200 | 1 |  |  |  |
| modified_time_stamp | decimal | 9 | 0 |  |  |  |
