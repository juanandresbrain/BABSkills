# dbo.vc_lang_compare_master_to_ldd

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| resource_id | numeric | 9 | 0 |  |  |  |
| table_name | nvarchar | 60 | 0 |  |  |  |
| master_description | nvarchar | 2000 | 1 |  |  |  |
| ldd_description | nvarchar | 2000 | 1 |  |  |  |
| master_description_correct | tinyint | 1 | 0 |  |  |  |
| description_column_name | nvarchar | 60 | 0 |  |  |  |
| resource_column_name | nvarchar | 60 | 0 |  |  |  |
