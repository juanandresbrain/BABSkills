# dbo.xref_location_store

**Database:** dw_mirror  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_id | smallint | 2 | 0 | YES |  |  |
| store_key | int | 4 | 0 |  |  |  |
| jurisdiction_id | smallint | 2 | 0 |  |  |  |
| jurisdiction_code | varchar | 20 | 0 |  |  |  |
| location_type | tinyint | 1 | 0 |  |  |  |
| location_type_label | varchar | 40 | 0 |  |  |  |

