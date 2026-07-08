# dbo.oim_uda

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| oim_uda_id | numeric | 9 | 0 |  |  |  |
| document_no | nvarchar | 40 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| reason_code | nvarchar | 10 | 1 |  |  |  |
| grouping_label | nvarchar | 40 | 1 |  |  |  |
| performed_by | nvarchar | 120 | 1 |  |  |  |
| submit_date | smalldatetime | 4 | 1 |  |  |  |
| document_source | smallint | 2 | 0 |  |  |  |
| last_modified | smalldatetime | 4 | 0 |  |  |  |
| line_id | numeric | 5 | 1 |  |  |  |
