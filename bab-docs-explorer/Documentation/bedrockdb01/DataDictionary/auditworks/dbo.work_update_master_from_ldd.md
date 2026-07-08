# dbo.work_update_master_from_ldd

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| spid | int | 4 | 0 |  |  |  |
| resource_id | numeric | 9 | 0 |  |  |  |
| table_name | nvarchar | 60 | 0 |  |  |  |
| master_description | nvarchar | 2000 | 1 |  |  |  |
| ldd_description | nvarchar | 2000 | 1 |  |  |  |
| master_description_correct | tinyint | 1 | 0 |  |  |  |
| description_column_name | nvarchar | 60 | 0 |  |  |  |
| resource_column_name | nvarchar | 60 | 0 |  |  |  |
