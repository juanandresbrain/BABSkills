# dbo.component_xref

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_type_code | smallint | 2 | 0 |  |  |  |
| include_oh_flag | bit | 1 | 0 |  |  |  |
| component_type_code | tinyint | 1 | 1 |  |  |  |
| component_sign | smallint | 2 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.post_cmp_work_group_$sp](../../StoredProcedures/ma_01/dbo.post_cmp_work_group_$sp.md)
- [ma_01: dbo.post_cmp_work_sku_$sp](../../StoredProcedures/ma_01/dbo.post_cmp_work_sku_$sp.md)
- [ma_01: dbo.post_cmp_work_style_$sp](../../StoredProcedures/ma_01/dbo.post_cmp_work_style_$sp.md)
- [ma_01: dbo.post_cmp_work_styleclr_$sp](../../StoredProcedures/ma_01/dbo.post_cmp_work_styleclr_$sp.md)
- [ma_01: dbo.wpost_cf_cmp_group_$sp](../../StoredProcedures/ma_01/dbo.wpost_cf_cmp_group_$sp.md)
- [ma_01: dbo.wpost_cf_cmp_style_$sp](../../StoredProcedures/ma_01/dbo.wpost_cf_cmp_style_$sp.md)
- [ma_01: dbo.wpost_cf_cmp_style_color_$sp](../../StoredProcedures/ma_01/dbo.wpost_cf_cmp_style_color_$sp.md)
- [ma_01: dbo.wpost_cmp_sku_$sp](../../StoredProcedures/ma_01/dbo.wpost_cmp_sku_$sp.md)
- [ma_01: dbo.wpost_iv_cmp_group_$sp](../../StoredProcedures/ma_01/dbo.wpost_iv_cmp_group_$sp.md)
- [ma_01: dbo.wpost_iv_cmp_style_$sp](../../StoredProcedures/ma_01/dbo.wpost_iv_cmp_style_$sp.md)
- [ma_01: dbo.wpost_iv_cmp_style_color_$sp](../../StoredProcedures/ma_01/dbo.wpost_iv_cmp_style_color_$sp.md)

