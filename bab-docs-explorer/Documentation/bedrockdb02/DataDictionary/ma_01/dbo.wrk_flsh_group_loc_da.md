# dbo.wrk_flsh_group_loc_da

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | decimal | 9 | 0 | YES |  |  |
| hierarchy_group_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| sales_date | smalldatetime | 4 | 0 |  |  |  |
| sales_net_units | int | 4 | 0 |  |  |  |
| sales_net_retail | decimal | 9 | 0 |  |  |  |
| sales_net_cost | decimal | 9 | 0 |  |  |  |
| sales_net_sellcurr_retail | decimal | 9 | 0 |  |  |  |
| sales_net_retail_te | decimal | 9 | 0 |  |  |  |
| sales_net_sellcurr_retail_te | decimal | 9 | 0 |  |  |  |
| sales_net_cost_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.cleanup_wrk_flash_$sp](../../StoredProcedures/ma_01/dbo.cleanup_wrk_flash_$sp.md)
- [ma_01: dbo.post_flash_group_$sp](../../StoredProcedures/ma_01/dbo.post_flash_group_$sp.md)
- [ma_01: dbo.prep_flash_group_$sp](../../StoredProcedures/ma_01/dbo.prep_flash_group_$sp.md)
- [ma_01: dbo.prep_wrk_flash_$sp](../../StoredProcedures/ma_01/dbo.prep_wrk_flash_$sp.md)
- [ma_01: dbo.validate_flash_$sp](../../StoredProcedures/ma_01/dbo.validate_flash_$sp.md)
- [ma_01: dbo.wpost_flash_group_$sp](../../StoredProcedures/ma_01/dbo.wpost_flash_group_$sp.md)

