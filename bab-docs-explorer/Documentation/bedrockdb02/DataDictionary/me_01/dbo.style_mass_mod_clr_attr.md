# dbo.style_mass_mod_clr_attr

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| mass_modification_id | decimal | 9 | 0 |  |  |  |
| color_attribute_mass_modify_id | int | 4 | 0 |  |  |  |
| color_code | nvarchar | 20 | 0 |  |  |  |
| color_short_desc | nvarchar | 100 | 1 |  |  |  |
| attribute_id | decimal | 9 | 0 |  |  |  |
| attribute_code | nvarchar | 40 | 0 |  |  |  |
| attribute_label | nvarchar | 100 | 1 |  |  |  |
| attribute_set_id | decimal | 9 | 1 |  |  |  |
| attribute_set_code | nvarchar | 40 | 1 |  |  |  |
| attribute_set_label | nvarchar | 100 | 1 |  |  |  |
| modify_type | smallint | 2 | 0 |  |  |  |

