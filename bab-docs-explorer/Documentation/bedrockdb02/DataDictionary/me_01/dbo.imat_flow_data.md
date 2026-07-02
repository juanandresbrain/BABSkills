# dbo.imat_flow_data

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imat_flow_id | int | 4 | 0 | YES |  |  |
| matching_flow_option | nvarchar | 40 | 0 |  |  |  |
| matching_flow_desc | nvarchar | 80 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |

