# dbo.oim_in_xfer

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| oim_in_xfer_id | numeric | 9 | 0 |  |  |  |
| document_no | nvarchar | 40 | 0 |  |  |  |
| receive_date | smalldatetime | 4 | 1 |  |  |  |
| performed_by | nvarchar | 120 | 1 |  |  |  |
| manifest_no | nvarchar | 40 | 1 |  |  |  |
| delta_flag | tinyint | 1 | 0 |  |  |  |
| last_modified | smalldatetime | 4 | 0 |  |  |  |
| line_id | numeric | 5 | 1 |  |  |  |
