# dbo.size_grid

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| size_grid_id | decimal | 9 | 0 | YES |  |  |
| size_category_id | decimal | 9 | 0 |  |  |  |
| size_grid_code | nvarchar | 16 | 0 |  |  |  |
| size_grid_desc | nvarchar | 160 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.dl_style_task_validate_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_validate_$sp.md)
- [me_01: dbo.dl_validate_import_upc_$sp](../../StoredProcedures/me_01/dbo.dl_validate_import_upc_$sp.md)

