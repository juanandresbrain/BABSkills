# dbo.reference_set

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| reference_set_id | int | 4 | 0 | YES |  |  |
| reference_set_code | nvarchar | 40 | 0 |  |  |  |
| reference_set_description | nvarchar | 60 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |

