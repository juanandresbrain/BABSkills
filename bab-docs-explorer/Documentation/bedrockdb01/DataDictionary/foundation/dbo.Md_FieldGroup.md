# dbo.Md_FieldGroup

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| topic_id | int | 4 | 0 |  |  |  |
| field_group_id | int | 4 | 0 |  |  |  |
| field_group_label_1 | nvarchar | 180 | 0 |  |  |  |
| field_group_label_2 | nvarchar | 180 | 1 |  |  |  |
| field_group_description_1 | nvarchar | 510 | 1 |  |  |  |
| field_group_description_2 | nvarchar | 510 | 1 |  |  |  |
| parent_field_group_id | int | 4 | 0 |  |  |  |
| display_fields | bit | 1 | 0 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| field_group_lbl_resource_name | nvarchar | 510 | 1 |  |  |  |
| field_group_desc_resource_name | nvarchar | 510 | 1 |  |  |  |
