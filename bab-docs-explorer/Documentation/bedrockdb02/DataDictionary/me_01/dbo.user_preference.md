# dbo.user_preference

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| user_preference_id | decimal | 9 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| must_use_location_flag | bit | 1 | 0 |  |  |  |
| use_batch_totals_flag | bit | 1 | 0 |  |  |  |
| replace_or_increment | smallint | 2 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| imrd_required_for_transfer | smallint | 2 | 0 |  |  |  |
| imrd_required_for_rtv | smallint | 2 | 0 |  |  |  |
| user_id | numeric | 9 | 0 |  |  |  |

