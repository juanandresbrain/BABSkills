# dbo.bulk_insert_item_master

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Item_Number | varchar | 6 | 1 |  |  |  |
| Description | varchar | 52 | 1 |  |  |  |
| Ship_unit | varchar | 1 | 1 |  |  |  |
| Slot_unit | varchar | 1 | 1 |  |  |  |
| Slot_Unit_Height | int | 4 | 1 |  |  |  |
| Slot_Unit_Length | int | 4 | 1 |  |  |  |
| Slot_Unit_Width | int | 4 | 1 |  |  |  |
| Slot_Unit_Weight | int | 4 | 1 |  |  |  |
| Slot_Unit_Each_Qty | int | 4 | 1 |  |  |  |
| Pick_Unit_Each_Qty | int | 4 | 1 |  |  |  |
| department | varchar | 10 | 1 |  |  |  |
| season_code | varchar | 10 | 1 |  |  |  |
| launch_date | datetime | 8 | 1 |  |  |  |
| discontinue_date | datetime | 8 | 1 |  |  |  |

