# dbo.Sv_Object

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| object_id | int | 4 | 0 |  |  |  |
| topic_id | int | 4 | 0 |  |  |  |
| object_type | smallint | 2 | 0 |  |  |  |
| created_date | smalldatetime | 4 | 0 |  |  |  |
| owner_id | int | 4 | 0 |  |  |  |
| modified_date | datetime | 8 | 0 |  |  |  |
| modified_id | int | 4 | 0 |  |  |  |
| last_used_date | smalldatetime | 4 | 1 |  |  |  |
| last_used_id | int | 4 | 1 |  |  |  |
| label_1 | nvarchar | 60 | 0 |  |  |  |
| label_2 | nvarchar | 60 | 0 |  |  |  |
| description_1 | nvarchar | 510 | 1 |  |  |  |
| description_2 | nvarchar | 510 | 1 |  |  |  |
| data | nvarchar | -1 | 0 |  |  |  |
| flags | char | 20 | 1 |  |  |  |
| permission | char | 6 | 0 |  |  |  |
| object_code | varchar | 30 | 1 |  |  |  |
| built_by_version | varchar | 11 | 1 |  |  |  |
| version | int | 4 | 1 |  |  |  |
| web_access | int | 4 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
