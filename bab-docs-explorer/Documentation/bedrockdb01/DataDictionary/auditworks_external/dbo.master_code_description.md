# dbo.master_code_description

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| table_name | nvarchar | 60 | 0 |  |  |  |
| column_name | nvarchar | 60 | 0 |  |  |  |
| code | smallint | 2 | 0 |  |  |  |
| code_display_descr | nvarchar | 160 | 0 |  |  |  |
| code_system_descr | nvarchar | 160 | 0 |  |  |  |
| remark | nvarchar | 510 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
