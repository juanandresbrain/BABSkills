# dbo.sd_job_script

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| row_id | int | 4 | 0 |  |  |  |
| sd_job_id | int | 4 | 0 |  |  |  |
| action_order | int | 4 | 0 |  |  |  |
| action_type | int | 4 | 0 |  |  |  |
| action_key | nvarchar | 510 | 0 |  |  |  |
| action_key_download | int | 4 | 0 |  |  |  |
| command_parameters | nvarchar | 510 | 0 |  |  |  |
| copy_rename_name | nvarchar | 510 | 0 |  |  |  |
| ini_section_name | nvarchar | 200 | 0 |  |  |  |
| ini_key_name | nvarchar | 200 | 0 |  |  |  |
| ini_value | nvarchar | 510 | 0 |  |  |  |
| xml_element_name | nvarchar | 510 | 0 |  |  |  |
| xml_element_value | nvarchar | 510 | 0 |  |  |  |
| xml_attribute_name | nvarchar | 510 | 0 |  |  |  |
| xml_attribute_value | nvarchar | 510 | 0 |  |  |  |
| file_old_section | nvarchar | 2048 | 0 |  |  |  |
| file_new_section | nvarchar | 2048 | 0 |  |  |  |
| hive | nvarchar | 38 | 0 |  |  |  |
| registry_value_name | nvarchar | 200 | 0 |  |  |  |
| registry_value_type | int | 4 | 0 |  |  |  |
| registry_value_data | nvarchar | 510 | 0 |  |  |  |
| recursive_flag | int | 4 | 0 |  |  |  |
| pause_delay | int | 4 | 0 |  |  |  |
| hidden_flag | int | 4 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
