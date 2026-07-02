# dbo.inventory_status_data

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| inventory_status_id | smallint | 2 | 0 | YES |  |  |
| inventory_status_code | nvarchar | 6 | 0 |  |  |  |
| inventory_status_desc | nvarchar | 120 | 0 |  |  |  |
| user_defined_flag | bit | 1 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| include_on_hand_totals_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

