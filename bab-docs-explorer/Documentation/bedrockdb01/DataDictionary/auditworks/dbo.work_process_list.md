# dbo.work_process_list

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| spid | smallint | 2 | 0 |  |  |  |
| status | nvarchar | 24 | 0 |  |  |  |
| loginame | nvarchar | 60 | 0 |  |  |  |
| hostname | nvarchar | 20 | 0 |  |  |  |
| blk | smallint | 2 | 0 |  |  |  |
| cmd | nvarchar | 32 | 0 |  |  |  |
| dbname | nvarchar | 60 | 0 |  |  |  |
| instance_id | smallint | 2 | 0 |  |  |  |
| work_tb_entry_date_time | datetime | 8 | 1 |  |  |  |
