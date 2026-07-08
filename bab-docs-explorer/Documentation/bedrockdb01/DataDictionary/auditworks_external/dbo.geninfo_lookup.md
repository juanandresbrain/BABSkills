# dbo.geninfo_lookup

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| form_name | nvarchar | 510 | 0 |  |  |  |
| field_name | nvarchar | 510 | 0 |  |  |  |
| field_datatype | nvarchar | 2 | 0 |  |  |  |
| display_def_id | smallint | 2 | 0 |  |  |  |
| column_name | nvarchar | 60 | 0 |  |  |  |
| auto_config_verified | tinyint | 1 | 0 |  |  |  |
| count_date_flag | tinyint | 1 | 1 |  |  |  |
| imrd_flag | tinyint | 1 | 1 |  |  |  |
| initiated_by_host_flag | tinyint | 1 | 1 |  |  |  |
| location_no_flag | tinyint | 1 | 1 |  |  |  |
| merchandise_key_flag | tinyint | 1 | 1 |  |  |  |
| originating_store_no_flag | tinyint | 1 | 1 |  |  |  |
| other_store_no_flag | tinyint | 1 | 1 |  |  |  |
| pos_deptclass_flag | tinyint | 1 | 1 |  |  |  |
| pos_identifier_flag | tinyint | 1 | 1 |  |  |  |
| reason_flag | tinyint | 1 | 1 |  |  |  |
| units_flag | tinyint | 1 | 1 |  |  |  |
| upc_no_flag | tinyint | 1 | 1 |  |  |  |
| vendor_no_flag | tinyint | 1 | 1 |  |  |  |
| form_code | smallint | 2 | 1 |  |  |  |
| approval_status_date | smalldatetime | 4 | 0 |  |  |  |
