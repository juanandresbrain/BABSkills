# dbo.language_identification

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| language_id | smallint | 2 | 0 |  |  |  |
| language_description | nvarchar | 100 | 0 |  |  |  |
| active_flag | tinyint | 1 | 0 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| root_language_id | smallint | 2 | 1 |  |  |  |
