# dbo.store_count_area_lock

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_count_area_id | int | 4 | 0 | YES |  |  |
| store_count_id | decimal | 9 | 0 | YES |  |  |
| lock_datetime | datetime | 8 | 1 |  |  |  |
| session_id | nvarchar | 80 | 1 |  |  |  |

