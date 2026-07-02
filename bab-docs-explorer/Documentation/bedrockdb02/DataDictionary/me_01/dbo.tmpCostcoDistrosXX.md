# dbo.tmpCostcoDistrosXX

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sourceid | varchar | 4 | 1 |  |  |  |
| destid | int | 4 | 0 |  |  |  |
| style_code | varchar | 6 | 1 |  |  |  |
| quantity | int | 4 | 0 |  |  |  |
| rec_type | int | 4 | 0 |  |  |  |
| reasoncode | nvarchar | 510 | 1 |  |  |  |
| priority | int | 4 | 1 |  |  |  |
| sequencenbr | bigint | 8 | 1 |  |  |  |
| distribution_number | varchar | 31 | 1 |  |  |  |
| po_nbr | varchar | 20 | 1 |  |  |  |
| active_pick_flag | varchar | 1 | 0 |  |  |  |
| average_cost | decimal | 5 | 1 |  |  |  |

