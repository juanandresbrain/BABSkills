# dbo.wrk_ib_allocation

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_group_id | int | 4 | 0 |  |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| color_id | smallint | 2 | 0 |  |  |  |
| size_master_id | int | 4 | 0 |  |  |  |
| ib_allocation_id | decimal | 9 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| expected_receipt_date | smalldatetime | 4 | 0 |  |  |  |
| allocated_units | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.cleanup_wrk_ib_allocation_$sp](../../StoredProcedures/ma_01/dbo.cleanup_wrk_ib_allocation_$sp.md)
- [ma_01: dbo.get_max_wrk_ib_allocation_id_$sp](../../StoredProcedures/ma_01/dbo.get_max_wrk_ib_allocation_id_$sp.md)
- [ma_01: dbo.post_wrk_ib_allocation_$sp](../../StoredProcedures/ma_01/dbo.post_wrk_ib_allocation_$sp.md)
- [ma_01: dbo.wpost_all_group_$sp](../../StoredProcedures/ma_01/dbo.wpost_all_group_$sp.md)
- [ma_01: dbo.wpost_all_sku_$sp](../../StoredProcedures/ma_01/dbo.wpost_all_sku_$sp.md)
- [ma_01: dbo.wpost_all_style_$sp](../../StoredProcedures/ma_01/dbo.wpost_all_style_$sp.md)
- [ma_01: dbo.wpost_all_style_color_$sp](../../StoredProcedures/ma_01/dbo.wpost_all_style_color_$sp.md)
- [ma_01: dbo.wprep_all_group_$sp](../../StoredProcedures/ma_01/dbo.wprep_all_group_$sp.md)
- [ma_01: dbo.wprep_all_sku_$sp](../../StoredProcedures/ma_01/dbo.wprep_all_sku_$sp.md)
- [ma_01: dbo.wprep_all_style_$sp](../../StoredProcedures/ma_01/dbo.wprep_all_style_$sp.md)
- [ma_01: dbo.wprep_all_style_color_$sp](../../StoredProcedures/ma_01/dbo.wprep_all_style_color_$sp.md)

