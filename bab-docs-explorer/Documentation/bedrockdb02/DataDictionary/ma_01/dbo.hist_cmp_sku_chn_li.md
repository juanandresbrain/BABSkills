# dbo.hist_cmp_sku_chn_li

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 0 | YES |  |  |
| color_id | smallint | 2 | 0 | YES |  |  |
| size_master_id | int | 4 | 0 | YES |  |  |
| component_type_code | smallint | 2 | 0 | YES |  |  |
| history_component_id | smallint | 2 | 0 | YES |  |  |
| component_units | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.hk_sku_modify_hist_cmp_$sp](../../StoredProcedures/ma_01/dbo.hk_sku_modify_hist_cmp_$sp.md)
- [ma_01: dbo.hk_style_delete_hist_cmp_$sp](../../StoredProcedures/ma_01/dbo.hk_style_delete_hist_cmp_$sp.md)
- [ma_01: dbo.post_cmp_sku_$sp](../../StoredProcedures/ma_01/dbo.post_cmp_sku_$sp.md)
- [ma_01: dbo.post_hist_cmp_sku_$sp](../../StoredProcedures/ma_01/dbo.post_hist_cmp_sku_$sp.md)
- [ma_01: dbo.summarize_hist_cmp_sku_$sp](../../StoredProcedures/ma_01/dbo.summarize_hist_cmp_sku_$sp.md)

