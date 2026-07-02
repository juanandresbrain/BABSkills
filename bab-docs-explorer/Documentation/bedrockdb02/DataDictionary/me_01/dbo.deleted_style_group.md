# dbo.deleted_style_group

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_group_id | decimal | 9 | 0 | YES |  |  |
| hierarchy_group_id | int | 4 | 0 |  |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| main_group_flag | bit | 1 | 0 |  |  |  |
| deleted_date | smalldatetime | 4 | 0 |  |  |  |
| reclass_pending_flag | bit | 1 | 0 |  |  |  |
| reclass_to_group_id | int | 4 | 1 |  |  |  |
| reclass_move_history_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.ecom_get_style_list_$sp](../../StoredProcedures/me_01/dbo.ecom_get_style_list_$sp.md)

