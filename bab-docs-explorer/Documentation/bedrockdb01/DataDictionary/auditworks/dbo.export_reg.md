# dbo.export_reg

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| register_name | varchar | 255 | 0 |  |  |  |
| register_function | smallint | 2 | 0 |  |  |  |
| register_poll_id | varchar | 15 | 0 |  |  |  |
| polling_method | tinyint | 1 | 1 |  |  |  |
| register_type | tinyint | 1 | 1 |  |  |  |
| register_location | smallint | 2 | 1 |  |  |  |
| register_department | smallint | 2 | 1 |  |  |  |
| translate_lookup_version | tinyint | 1 | 0 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| assigned_register_group | smallint | 2 | 1 |  |  |  |
| reg_pre_midnight_time | int | 4 | 1 |  |  |  |
| reg_post_midnight_time | int | 4 | 1 |  |  |  |
