# dbo.entity_custom_property

**Database:** LH_Staging_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| entity_custom_property_id | decimal | 9 | 1 |  |  |  |
| custom_property_id | decimal | 9 | 1 |  |  |  |
| parent_type | int | 4 | 1 |  |  |  |
| parent_id | decimal | 9 | 1 |  |  |  |
| custom_property_value | varchar | 8000 | 1 |  |  |  |
