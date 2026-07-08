# dbo.stock_control_display_def

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| display_def_id | smallint | 2 | 0 |  |  |  |
| display_def_descr | nvarchar | 510 | 0 |  |  |  |
| upc_no_fe_resource_id | int | 4 | 0 |  |  |  |
| merchandise_key_fe_resource_id | int | 4 | 0 |  |  |  |
| initiated_by_fe_resource_id | int | 4 | 0 |  |  |  |
| units_fe_resource_id | int | 4 | 0 |  |  |  |
| other_store_no_fe_resource_id | int | 4 | 0 |  |  |  |
| location_no_fe_resource_id | int | 4 | 0 |  |  |  |
| vendor_no_fe_resource_id | int | 4 | 0 |  |  |  |
| count_date_fe_resource_id | int | 4 | 0 |  |  |  |
| pos_identifier_fe_resource_id | int | 4 | 0 |  |  |  |
| pos_id_type_fe_resource_id | int | 4 | 0 |  |  |  |
| pos_deptclass_fe_resource_id | int | 4 | 0 |  |  |  |
| upc_division_fe_resource_id | int | 4 | 0 |  |  |  |
| originating_str_fe_resource_id | int | 4 | 0 |  |  |  |
| default_initiated_by_host | tinyint | 1 | 0 |  |  |  |
| default_pos_identifier_type | tinyint | 1 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| other_store_validation | tinyint | 1 | 1 |  |  |  |
| original_store_validation | tinyint | 1 | 1 |  |  |  |
| upc_no_mandatory | tinyint | 1 | 0 |  |  |  |
| merchandise_key_mandatory | tinyint | 1 | 0 |  |  |  |
| units_mandatory | tinyint | 1 | 0 |  |  |  |
| other_store_no_mandatory | tinyint | 1 | 0 |  |  |  |
| location_no_mandatory | tinyint | 1 | 0 |  |  |  |
| vendor_no_mandatory | tinyint | 1 | 0 |  |  |  |
| count_date_mandatory | tinyint | 1 | 0 |  |  |  |
| pos_identifier_mandatory | tinyint | 1 | 0 |  |  |  |
| pos_id_type_mandatory | tinyint | 1 | 0 |  |  |  |
| pos_deptclass_mandatory | tinyint | 1 | 0 |  |  |  |
| upc_division_mandatory | tinyint | 1 | 0 |  |  |  |
| originating_str_mandatory | tinyint | 1 | 0 |  |  |  |
| upc_no_code_type | smallint | 2 | 0 |  |  |  |
| merchandise_key_code_type | smallint | 2 | 0 |  |  |  |
| units_code_type | smallint | 2 | 0 |  |  |  |
| other_store_no_code_type | smallint | 2 | 0 |  |  |  |
| location_no_code_type | smallint | 2 | 0 |  |  |  |
| pos_id_type_code_type | smallint | 2 | 0 |  |  |  |
| pos_deptclass_code_type | smallint | 2 | 0 |  |  |  |
| upc_division_code_type | smallint | 2 | 0 |  |  |  |
| originating_str_code_type | smallint | 2 | 0 |  |  |  |
| initiated_by_code_type | smallint | 2 | 0 |  |  |  |
| imrd_fe_resource_id | int | 4 | 0 |  |  |  |
| imrd_mandatory | tinyint | 1 | 0 |  |  |  |
| imrd_code_type | smallint | 2 | 0 |  |  |  |
| reason_fe_resource_id | int | 4 | 0 |  |  |  |
| reason_mandatory | tinyint | 1 | 0 |  |  |  |
| reason_code_type | smallint | 2 | 0 |  |  |  |
| active_flag | tinyint | 1 | 0 |  |  |  |
| units_reversal_factor | int | 4 | 0 |  |  |  |
| vendor_no_code_type | smallint | 2 | 0 |  |  |  |
| pos_identifier_code_type | smallint | 2 | 0 |  |  |  |
