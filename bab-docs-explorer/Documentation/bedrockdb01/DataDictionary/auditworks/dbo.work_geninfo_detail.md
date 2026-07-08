# dbo.work_geninfo_detail

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| row_sequence_no | numeric | 9 | 0 |  |  |  |
| request_id | binary | 16 | 0 |  |  |  |
| auto_config_verified | tinyint | 1 | 1 |  |  |  |
| count_date | datetime | 8 | 1 |  |  |  |
| imrd | nvarchar | 3000 | 1 |  |  |  |
| initiated_by_host | tinyint | 1 | 0 |  |  |  |
| location_no | int | 4 | 1 |  |  |  |
| merchandise_key | numeric | 9 | 1 |  |  |  |
| originating_store_no | int | 4 | 1 |  |  |  |
| other_store_no | int | 4 | 1 |  |  |  |
| pos_deptclass | int | 4 | 1 |  |  |  |
| pos_identifier | nvarchar | 3000 | 1 |  |  |  |
| reason | nvarchar | 3000 | 1 |  |  |  |
| units | unit_datatype | 9 | 1 |  |  |  |
| upc_no | numeric | 9 | 1 |  |  |  |
| vendor_no | nvarchar | 3000 | 1 |  |  |  |
