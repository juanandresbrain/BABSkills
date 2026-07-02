# dbo.style_mass_mod_cus_prop

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| mass_modification_id | decimal | 9 | 0 |  |  |  |
| custom_property_id | decimal | 9 | 0 |  |  |  |
| cust_prop_code | nvarchar | 40 | 0 |  |  |  |
| cust_prop_label | nvarchar | 100 | 1 |  |  |  |
| property_type | smallint | 2 | 0 |  |  |  |
| custom_property_value | nvarchar | 100 | 1 |  |  |  |
| modify_type | smallint | 2 | 0 |  |  |  |

