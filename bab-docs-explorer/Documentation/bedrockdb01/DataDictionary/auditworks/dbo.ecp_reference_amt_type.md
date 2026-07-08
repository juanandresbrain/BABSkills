# dbo.ecp_reference_amt_type

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| reference_amount_type | smallint | 2 | 0 |  |  |  |
| reference_amount_type_descr | nvarchar | 510 | 0 |  |  |  |
| CLNDR_LVL_TYPE_ID | binary | 16 | 1 |  |  |  |
| maintenance_type | smallint | 2 | 0 |  |  |  |
| sensitivity_flag | tinyint | 1 | 0 |  |  |  |
| employee_no_flag | tinyint | 1 | 0 |  |  |  |
| store_no_flag | tinyint | 1 | 0 |  |  |  |
| selling_area_flag | tinyint | 1 | 0 |  |  |  |
| position_flag | tinyint | 1 | 0 |  |  |  |
| upper_levels_available | tinyint | 1 | 0 |  |  |  |
| active_flag | tinyint | 1 | 0 |  |  |  |
| code_meaning_control | nchar | 2 | 0 |  |  |  |
| reference_amount_type_desc_sys | nvarchar | 510 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| ref_amt_type_referenced_flag | tinyint | 1 | 0 |  |  |  |
| display_format | nvarchar | 50 | 1 |  |  |  |
