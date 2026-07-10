# dbo.entity_custom_property

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| entity_custom_property_id | decimal | 9 | 0 |  |  |  |
| custom_property_id | decimal | 9 | 0 |  |  |  |
| parent_type | smallint | 2 | 0 |  |  |  |
| parent_id | decimal | 9 | 0 |  |  |  |
| custom_property_value | nvarchar | 60 | 0 |  |  |  |
