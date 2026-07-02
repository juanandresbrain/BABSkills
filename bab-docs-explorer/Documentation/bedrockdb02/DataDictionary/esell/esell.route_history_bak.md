# esell.route_history_bak

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| route_id | int | 4 | 0 |  |  |  |
| order_id | nvarchar | 60 | 0 |  |  |  |
| route_timestamp | datetime | 8 | 1 |  |  |  |
| original_location | nvarchar | 40 | 0 |  |  |  |
| route_to_location | nvarchar | 40 | 1 |  |  |  |
| string1 | nvarchar | 510 | 1 |  |  |  |
| string2 | nvarchar | 510 | 1 |  |  |  |
| string3 | nvarchar | 510 | 1 |  |  |  |
| int1 | int | 4 | 1 |  |  |  |
| int2 | int | 4 | 1 |  |  |  |
| int3 | int | 4 | 1 |  |  |  |

