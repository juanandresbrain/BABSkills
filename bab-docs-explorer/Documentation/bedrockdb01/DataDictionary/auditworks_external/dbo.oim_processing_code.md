# dbo.oim_processing_code

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| oim_processing_code_id | numeric | 9 | 0 |  |  |  |
| entity_id | numeric | 9 | 0 |  |  |  |
| entity_code | smallint | 2 | 0 |  |  |  |
| processing_code | nvarchar | 16 | 0 |  |  |  |
| quantity | int | 4 | 1 |  |  |  |
| line_id | numeric | 5 | 1 |  |  |  |
