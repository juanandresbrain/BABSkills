# dbo.position_data

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| position_id | decimal | 9 | 0 | YES |  |  |
| position_label | nvarchar | 60 | 0 |  |  |  |
| approved_by_position_id | decimal | 9 | 1 |  |  |  |
| employee_role_id | decimal | 9 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| position_code | nvarchar | 40 | 0 |  |  |  |

