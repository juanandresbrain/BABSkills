# dbo.sd_job_script

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| row_id | int | 4 | 0 | YES |  |  |
| sd_job_id | int | 4 | 0 |  |  |  |
| action_order | int | 4 | 0 |  |  |  |
| action_type | int | 4 | 0 |  |  |  |
| action_key | varchar | 255 | 0 |  |  |  |
| action_key_download | int | 4 | 0 |  |  |  |
| command_parameters | varchar | 255 | 0 |  |  |  |
| copy_rename_name | varchar | 255 | 0 |  |  |  |
| ini_section_name | varchar | 100 | 0 |  |  |  |
| ini_key_name | varchar | 100 | 0 |  |  |  |
| ini_value | varchar | 255 | 0 |  |  |  |
| xml_element_name | varchar | 255 | 0 |  |  |  |
| xml_element_value | varchar | 255 | 0 |  |  |  |
| xml_attribute_name | varchar | 255 | 0 |  |  |  |
| xml_attribute_value | varchar | 255 | 0 |  |  |  |
| file_old_section | varchar | 1024 | 0 |  |  |  |
| file_new_section | varchar | 1024 | 0 |  |  |  |
| hive | varchar | 19 | 0 |  |  |  |
| registry_value_name | varchar | 100 | 0 |  |  |  |
| registry_value_type | int | 4 | 0 |  |  |  |
| registry_value_data | varchar | 255 | 0 |  |  |  |
| recursive_flag | int | 4 | 0 |  |  |  |
| pause_delay | int | 4 | 0 |  |  |  |
| hidden_flag | int | 4 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
