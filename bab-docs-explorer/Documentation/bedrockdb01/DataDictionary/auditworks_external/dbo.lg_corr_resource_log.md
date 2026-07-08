# dbo.lg_corr_resource_log

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| execution_datetime | datetime | 8 | 0 |  |  |  |
| key_col | nvarchar | 400 | 0 |  |  |  |
| row_count | int | 4 | 0 |  |  |  |
| lg_query | nvarchar | 6000 | 1 |  |  |  |
