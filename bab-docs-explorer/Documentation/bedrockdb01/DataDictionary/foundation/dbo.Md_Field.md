# dbo.Md_Field

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| field_id | int | 4 | 0 |  |  |  |
| field_owner_id | int | 4 | 0 |  |  |  |
| table_id | int | 4 | 0 |  |  |  |
| topic_id | int | 4 | 0 |  |  |  |
| field_label_1 | nvarchar | 180 | 0 |  |  |  |
| field_label_2 | nvarchar | 180 | 0 |  |  |  |
| field_description_1 | nvarchar | 510 | 1 |  |  |  |
| field_description_2 | nvarchar | 510 | 1 |  |  |  |
| field_expression_1 | nvarchar | 510 | 0 |  |  |  |
| field_expression_2 | nvarchar | 510 | 0 |  |  |  |
| field_type | char | 1 | 0 |  |  |  |
| field_format | varchar | 20 | 1 |  |  |  |
| field_width | tinyint | 1 | 0 |  |  |  |
| field_size | smallint | 2 | 1 |  |  |  |
| field_permission | char | 6 | 0 |  |  |  |
| input_mask | varchar | 60 | 1 |  |  |  |
| field_flags | char | 20 | 0 |  |  |  |
| default_method | char | 1 | 1 |  |  |  |
| lookup_type | smallint | 2 | 0 |  |  |  |
| lookup_id | int | 4 | 1 |  |  |  |
| short_label_1 | nvarchar | 120 | 1 |  |  |  |
| short_label_2 | nvarchar | 120 | 1 |  |  |  |
| field_period_group_id | int | 4 | 1 |  |  |  |
| subfield_lookup_id | int | 4 | 1 |  |  |  |
| native_type_syb | varchar | 30 | 1 |  |  |  |
| native_type_ora | varchar | 30 | 1 |  |  |  |
| native_type_sql | varchar | 30 | 1 |  |  |  |
| resource_id_1 | numeric | 9 | 1 |  |  |  |
| resource_id_2 | numeric | 9 | 1 |  |  |  |
| field_min_value | varchar | 30 | 1 |  |  |  |
| field_max_value | varchar | 30 | 1 |  |  |  |
| extended_field_id | binary | 16 | 1 |  |  |  |
| field_label_resource_name | nvarchar | 510 | 1 |  |  |  |
| short_label_resource_name | nvarchar | 510 | 1 |  |  |  |
| field_desc_resource_name | nvarchar | 510 | 1 |  |  |  |
