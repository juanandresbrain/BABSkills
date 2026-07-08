# dbo.dw_dblink_peripheral

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| instance_id | smallint | 2 | 0 |  |  |  |
| dblink_name | nvarchar | 256 | 0 |  |  |  |
| database_name | nvarchar | 60 | 0 |  |  |  |
| rdbms_instance_name | nvarchar | 100 | 1 |  |  |  |
