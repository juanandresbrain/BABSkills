# dbo.calendar_shift

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| calendar_shift_id | T_ID | 16 | 0 | YES |  |  |
| calendar_week_id | decimal | 9 | 0 |  |  |  |
| calendar_shift_week_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| adjustment_factor | decimal | 5 | 1 |  |  |  |

