# dbo.tmpPartyManager_Styles

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StyleCode | varchar | 20 | 1 |  |  |  |
| active_flag | int | 4 | 0 |  |  |  |
| short_desc | varchar | 75 | 0 |  |  |  |
| hierarchy_group_code | char | 11 | 0 |  |  |  |
| total_on_hand_units | int | 4 | 1 |  |  |  |
| allocated | int | 4 | 1 |  |  |  |
| available_to_distribute | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spPartyManager_ActiveDistro](../../StoredProcedures/me_01/dbo.spPartyManager_ActiveDistro.md)

