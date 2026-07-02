# dbo.hist_flsh_group_loc_da

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_group_id | int | 4 | 0 | YES |  |  |
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

- [me_01: dbo.sales_balancing_c$sp](../../StoredProcedures/me_01/dbo.sales_balancing_c$sp.md)
- [me_01: dbo.sales_balancing_l$sp](../../StoredProcedures/me_01/dbo.sales_balancing_l$sp.md)
- [ma_01: dbo.post_flash_group_$sp](../../StoredProcedures/ma_01/dbo.post_flash_group_$sp.md)
- [ma_01: dbo.reclass_hist_flsh_$sp](../../StoredProcedures/ma_01/dbo.reclass_hist_flsh_$sp.md)
- [ma_01: dbo.startup_flsh_group_loc_da_$sp](../../StoredProcedures/ma_01/dbo.startup_flsh_group_loc_da_$sp.md)

