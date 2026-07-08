# dbo.interface_status

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| interface_id | tinyint | 1 | 0 |  |  |  |
| posting_in_progress | tinyint | 1 | 0 |  |  |  |
| retrieval_in_progress | tinyint | 1 | 0 |  |  |  |
| last_retrieval_datetime | datetime | 8 | 0 |  |  |  |
| last_posting_datetime | datetime | 8 | 0 |  |  |  |
| immediate_posting_requested | tinyint | 1 | 1 |  |  |  |
| hold_datetime | datetime | 8 | 1 |  |  |  |
| last_transfer_datetime | datetime | 8 | 1 |  |  |  |
