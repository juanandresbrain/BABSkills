# dbo.import_std_register

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| entry_type | char | 1 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | numeric | 9 | 0 |  |  |  |
| register_name | varchar | 30 | 0 |  |  |  |
| register_function | int | 4 | 0 |  |  |  |
| register_poll_id | varchar | 15 | 0 |  |  |  |
| polling_method | int | 4 | 1 |  |  |  |
| register_type | int | 4 | 1 |  |  |  |
| register_location | int | 4 | 1 |  |  |  |
| register_department | int | 4 | 1 |  |  |  |
| translate_lookup_version | int | 4 | 0 |  |  |  |
| import_id | numeric | 9 | 0 | YES |  |  |
