# dbo.entity_position

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| entity_position_id | decimal | 9 | 0 | YES |  |  |
| parent_id | decimal | 9 | 0 |  |  |  |
| parent_type | smallint | 2 | 0 |  |  |  |
| position_id | decimal | 9 | 0 |  |  |  |
| default_position_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.get_pc_instruction_values_$sp](../../StoredProcedures/me_01/dbo.get_pc_instruction_values_$sp.md)
- [me_01: dbo.update_location_position_$sp](../../StoredProcedures/me_01/dbo.update_location_position_$sp.md)

