# esell.airport

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| airport_code | nchar | 6 | 0 | YES |  |  |
| airport_desc | nvarchar | 80 | 1 |  |  |  |
| airport1_address | nvarchar | 200 | 1 |  |  |  |
| airport2_address | nvarchar | 200 | 1 |  |  |  |
| city_name | nvarchar | 120 | 1 |  |  |  |
| state_code | nchar | 4 | 1 |  |  |  |
| postal_code | nvarchar | 30 | 1 |  |  |  |
| country_code | nchar | 6 | 1 |  |  |  |
| latitude | float | 8 | 1 |  |  |  |
| longitude | float | 8 | 1 |  |  |  |

