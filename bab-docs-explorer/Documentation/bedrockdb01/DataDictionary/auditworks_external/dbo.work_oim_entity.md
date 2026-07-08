# dbo.work_oim_entity

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| interface_id | tinyint | 1 | 0 |  |  |  |
| if_entry_no | if_entry_datatype | 9 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| cashier_no | int | 4 | 0 |  |  |  |
| entity_code | smallint | 2 | 0 |  |  |  |
| segment_id | int | 4 | 0 |  |  |  |
| reference_no | nvarchar | 40 | 1 |  |  |  |
| min_line_id | numeric | 5 | 0 |  |  |  |
| max_line_id | numeric | 5 | 0 |  |  |  |
| if_rejection_rules_overriden | numeric | 9 | 1 |  |  |  |
| location_id | numeric | 5 | 1 |  |  |  |
| vendor_no | nvarchar | 60 | 1 |  |  |  |
| other_store_no | int | 4 | 1 |  |  |  |
| location_no | int | 4 | 1 |  |  |  |
| count_date | datetime | 8 | 1 |  |  |  |
| units | unit_datatype | 9 | 1 |  |  |  |
| pos_identifier | nvarchar | 40 | 1 |  |  |  |
| reason | nvarchar | 60 | 1 |  |  |  |
| imrd | nvarchar | 40 | 1 |  |  |  |
| other_location_id | numeric | 5 | 1 |  |  |  |
| initiated_by_host | tinyint | 1 | 0 |  |  |  |
