# dbo.alpha_code_description

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| code_type | smallint | 2 | 0 |  |  |  |
| code | nvarchar | 40 | 0 |  |  |  |
| code_status | nchar | 2 | 0 |  |  |  |
| code_display_descr1 | nvarchar | 510 | 0 |  |  |  |
| code_display_descr2 | nvarchar | 510 | 0 |  |  |  |
| system_code | nvarchar | 20 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| active_flag | tinyint | 1 | 0 |  |  |  |
