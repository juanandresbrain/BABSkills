# dbo.carrier_service

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| carrier_service_id | decimal | 9 | 0 | YES |  |  |
| carrier_id | smallint | 2 | 0 |  |  |  |
| carrier_service_code | nvarchar | 12 | 0 |  |  |  |
| carrier_service_description | nvarchar | 100 | 0 |  |  |  |
| carrier_service_charge | decimal | 9 | 0 |  |  |  |
| unit_id | tinyint | 1 | 0 |  |  |  |
| currency_id | decimal | 9 | 0 |  |  |  |

