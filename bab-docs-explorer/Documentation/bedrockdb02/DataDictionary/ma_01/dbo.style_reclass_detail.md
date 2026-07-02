# dbo.style_reclass_detail

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 0 | YES |  |  |
| old_hierarchy_group_id | int | 4 | 0 | YES |  |  |
| new_hierarchy_group_id | int | 4 | 0 | YES |  |  |
| as_of_week | int | 4 | 0 |  |  |  |
| transaction_reason_id | smallint | 2 | 1 |  |  |  |
| hist_step | bit | 1 | 0 |  |  |  |
| cmp_step | bit | 1 | 0 |  |  |  |
| flsh_step | bit | 1 | 0 |  |  |  |
| le_step | bit | 1 | 0 |  |  |  |
| oo_all_step | bit | 1 | 0 |  |  |  |
| oh_step | bit | 1 | 0 |  |  |  |
| track_adj_cmp_step | bit | 1 | 0 |  |  |  |
| create_date | smalldatetime | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.reclass_hist_$sp](../../StoredProcedures/ma_01/dbo.reclass_hist_$sp.md)
- [ma_01: dbo.reclass_hist_cmp_$sp](../../StoredProcedures/ma_01/dbo.reclass_hist_cmp_$sp.md)
- [ma_01: dbo.reclass_hist_flsh_$sp](../../StoredProcedures/ma_01/dbo.reclass_hist_flsh_$sp.md)
- [ma_01: dbo.reclass_hist_le_$sp](../../StoredProcedures/ma_01/dbo.reclass_hist_le_$sp.md)
- [ma_01: dbo.reclass_hist_oh_$sp](../../StoredProcedures/ma_01/dbo.reclass_hist_oh_$sp.md)
- [ma_01: dbo.reclass_oo_all_$sp](../../StoredProcedures/ma_01/dbo.reclass_oo_all_$sp.md)

