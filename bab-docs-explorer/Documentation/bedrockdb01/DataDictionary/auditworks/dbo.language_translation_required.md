# dbo.language_translation_required

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| table_name | nvarchar | 60 | 0 |  |  |  |
| description_column_name | nvarchar | 60 | 0 |  |  |  |
| category | nchar | 20 | 0 |  |  |  |
| comments | nvarchar | 510 | 1 |  |  |  |
| table_key | nvarchar | 510 | 1 |  |  |  |
| resource_column_name | nvarchar | 60 | 1 |  |  |  |
| table_key_oracle | nvarchar | 510 | 1 |  |  |  |
