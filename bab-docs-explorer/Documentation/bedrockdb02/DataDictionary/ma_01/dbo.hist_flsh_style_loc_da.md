# dbo.hist_flsh_style_loc_da

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| sales_date | smalldatetime | 4 | 0 | YES |  |  |
| sales_net_units | int | 4 | 0 |  |  |  |
| sales_net_retail | decimal | 9 | 0 |  |  |  |
| sales_net_cost | decimal | 9 | 0 |  |  |  |
| sales_net_sellcurr_retail | decimal | 9 | 0 |  |  |  |
| sales_net_retail_te | decimal | 9 | 0 |  |  |  |
| sales_net_sellcurr_retail_te | decimal | 9 | 0 |  |  |  |
| sales_net_cost_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.hk_style_delete_hist_flsh_$sp](../../StoredProcedures/ma_01/dbo.hk_style_delete_hist_flsh_$sp.md)
- [ma_01: dbo.hk_style_reclass_hist_flsh_$sp](../../StoredProcedures/ma_01/dbo.hk_style_reclass_hist_flsh_$sp.md)
- [ma_01: dbo.post_flash_style_$sp](../../StoredProcedures/ma_01/dbo.post_flash_style_$sp.md)
- [ma_01: dbo.reclass_hist_flsh_$sp](../../StoredProcedures/ma_01/dbo.reclass_hist_flsh_$sp.md)
- [ma_01: dbo.startup_flsh_style_loc_da_$sp](../../StoredProcedures/ma_01/dbo.startup_flsh_style_loc_da_$sp.md)

