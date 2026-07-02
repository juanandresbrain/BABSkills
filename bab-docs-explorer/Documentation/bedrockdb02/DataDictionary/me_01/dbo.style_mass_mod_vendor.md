# dbo.style_mass_mod_vendor

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| mass_modification_id | decimal | 9 | 0 |  |  |  |
| vendor_id | decimal | 9 | 0 |  |  |  |
| vendor_code | nvarchar | 40 | 0 |  |  |  |
| vendor_name | nvarchar | 100 | 1 |  |  |  |
| vendor_style | nvarchar | 100 | 1 |  |  |  |
| current_cost | decimal | 9 | 1 |  |  |  |
| modify_type | smallint | 2 | 0 |  |  |  |

