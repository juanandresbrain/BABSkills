# dbo.size_scale_param_loc

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| size_scale_param_id | bigint | 8 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| suspend_flag | bit | 1 | 0 |  |  |  |
| suspend_from_date | smalldatetime | 4 | 1 |  |  |  |
| suspend_to_date | smalldatetime | 4 | 1 |  |  |  |

