# dbo.sl_component

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sl_component_id | decimal | 9 | 0 | YES |  |  |
| sl_component_label | nvarchar | 120 | 0 |  |  |  |
| rim_method | tinyint | 1 | 1 |  |  |  |
| on_hand_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.roll_onhand_$sp](../../StoredProcedures/me_01/dbo.roll_onhand_$sp.md)

