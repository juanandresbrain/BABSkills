# dbo.plu_file_regenerate

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| plu_file_regenerate_id | decimal | 9 | 0 | YES |  |  |
| hierarchy_group_id | int | 4 | 0 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| thin_pos_server_id | smallint | 2 | 1 |  |  |  |
| regenerate_type | tinyint | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.copy_like_location_prices_$sp](../../StoredProcedures/me_01/dbo.copy_like_location_prices_$sp.md)
- [me_01: dbo.plu_cu_hg_regen_$sp](../../StoredProcedures/me_01/dbo.plu_cu_hg_regen_$sp.md)
- [me_01: dbo.plu_cu_regen_$sp](../../StoredProcedures/me_01/dbo.plu_cu_regen_$sp.md)
- [me_01: dbo.plu_hg_regen_queue_$sp](../../StoredProcedures/me_01/dbo.plu_hg_regen_queue_$sp.md)
- [me_01: dbo.plu_regen_queue_$sp](../../StoredProcedures/me_01/dbo.plu_regen_queue_$sp.md)

