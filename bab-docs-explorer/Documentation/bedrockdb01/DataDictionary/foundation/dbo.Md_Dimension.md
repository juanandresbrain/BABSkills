# dbo.Md_Dimension

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| dim_id | int | 4 | 0 |  |  |  |
| topic_id | int | 4 | 0 |  |  |  |
| dim_label1 | varchar | 30 | 0 |  |  |  |
| dim_label2 | varchar | 30 | 0 |  |  |  |
| dim_description1 | varchar | 255 | 1 |  |  |  |
| dim_description2 | varchar | 255 | 1 |  |  |  |
| one_table_only | bit | 1 | 0 |  |  |  |
| table_id | int | 4 | 1 |  |  |  |
| key_field_id | int | 4 | 1 |  |  |  |
| view_key_field_id | int | 4 | 1 |  |  |  |
| not_same_key_ids | smallint | 2 | 1 |  |  |  |
| multi_alias_by_subfield | tinyint | 1 | 1 |  |  |  |
| super_dim_id | int | 4 | 1 |  |  |  |
