# dbo.plan_exp_table_group

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| plan_exp_table_group_id | smallint | 2 | 0 | YES |  |  |
| plan_exp_table_group_label | nvarchar | 40 | 0 |  |  |  |
| display_expression_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.post_hist_cmp_group_$sp](../../StoredProcedures/ma_01/dbo.post_hist_cmp_group_$sp.md)
- [ma_01: dbo.post_hist_group_rim_$sp](../../StoredProcedures/ma_01/dbo.post_hist_group_rim_$sp.md)
- [ma_01: dbo.post_hist_oh_group_$sp](../../StoredProcedures/ma_01/dbo.post_hist_oh_group_$sp.md)
- [ma_01: dbo.post_oo_all_group_$sp](../../StoredProcedures/ma_01/dbo.post_oo_all_group_$sp.md)

