# esell.postal_code

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| postal_code | nvarchar | 30 | 0 |  |  |  |
| type | nchar | 2 | 1 |  |  |  |
| city | nvarchar | 100 | 1 |  |  |  |
| city_type | nchar | 2 | 1 |  |  |  |
| state | nvarchar | 150 | 1 |  |  |  |
| state_code | nvarchar | 40 | 1 |  |  |  |
| area_code | nchar | 6 | 1 |  |  |  |
| timezone | nvarchar | 30 | 1 |  |  |  |
| GMT_Offset | int | 4 | 1 |  |  |  |
| dst | nchar | 2 | 1 |  |  |  |
| latitude | float | 8 | 1 |  |  |  |
| longitude | float | 8 | 1 |  |  |  |
| country | nvarchar | 6 | 1 |  |  |  |
| update_time | datetime | 8 | 1 |  |  |  |

