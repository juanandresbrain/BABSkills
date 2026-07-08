# dbo.input_cust_liability

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_batch_id | numeric | 9 | 0 |  |  |  |
| reference_no | nvarchar | 40 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| rule_id | nvarchar | 6 | 0 |  |  |  |
| store_no | numeric | 9 | 0 |  |  |  |
| pos_identifier_type | tinyint | 1 | 0 |  |  |  |
| pos_identifier | nvarchar | 40 | 1 |  |  |  |
| upc_no | numeric | 9 | 1 |  |  |  |
| units | unit_datatype | 9 | 0 |  |  |  |
| serial_no | nvarchar | 160 | 1 |  |  |  |
