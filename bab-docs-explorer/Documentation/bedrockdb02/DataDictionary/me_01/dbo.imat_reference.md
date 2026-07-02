# dbo.imat_reference

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imat_reference_id | decimal | 9 | 0 | YES |  |  |
| imat_header_id | decimal | 9 | 0 |  |  |  |
| reference_number | nvarchar | 40 | 1 |  |  |  |
| validity_flag | bit | 1 | 0 |  |  |  |
| reference_type_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |

