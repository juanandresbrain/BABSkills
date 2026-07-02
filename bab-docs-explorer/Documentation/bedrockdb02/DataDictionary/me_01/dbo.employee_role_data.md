# dbo.employee_role_data

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| employee_role_id | decimal | 9 | 0 | YES |  |  |
| role_label | nvarchar | 60 | 0 |  |  |  |
| role_mask | nvarchar | 40 | 0 |  |  |  |
| exclusivity_flag | bit | 1 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |

