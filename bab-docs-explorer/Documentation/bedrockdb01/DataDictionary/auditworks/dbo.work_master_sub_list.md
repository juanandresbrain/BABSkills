# dbo.work_master_sub_list

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| interface_id | tinyint | 1 | 0 |  |  |  |
| table_name | nvarchar | 60 | 0 |  |  |  |
| table_key | nvarchar | 510 | 0 |  |  |  |
| posting_datetime | datetime | 8 | 0 |  |  |  |
| action | tinyint | 1 | 0 |  |  |  |
| entry_id | numeric | 9 | 0 |  |  |  |
