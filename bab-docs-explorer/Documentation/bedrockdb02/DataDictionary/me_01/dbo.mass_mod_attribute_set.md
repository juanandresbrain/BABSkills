# dbo.mass_mod_attribute_set

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| mass_modification_id | decimal | 9 | 0 | YES |  |  |
| mass_mod_attribute_set_id | smallint | 2 | 0 | YES |  |  |
| attribute_id | decimal | 9 | 0 |  | YES |  |
| attribute_set_id | decimal | 9 | 1 |  | YES |  |
| action | smallint | 2 | 0 |  |  |  |

