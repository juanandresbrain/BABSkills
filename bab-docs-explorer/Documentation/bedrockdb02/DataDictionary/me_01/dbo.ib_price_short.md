# dbo.ib_price_short

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ib_price_id | decimal | 9 | 0 | YES |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| color_id | smallint | 2 | 1 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| jurisdiction_id | smallint | 2 | 0 |  |  |  |
| pricing_group_id | smallint | 2 | 1 |  |  |  |
| temp_price_flag | bit | 1 | 0 |  |  |  |
| start_date | smalldatetime | 4 | 0 |  |  |  |
| end_date | smalldatetime | 4 | 1 |  |  |  |
| valuation_retail_price | decimal | 9 | 0 |  |  |  |
| selling_retail_price | decimal | 9 | 0 |  |  |  |
| price_status_id | smallint | 2 | 0 |  |  |  |
| document_number | nvarchar | 40 | 1 |  |  |  |
| cancel_promo_flag | bit | 1 | 0 |  |  |  |
| effective_date | smalldatetime | 4 | 1 |  |  |  |
| price_change_type | smallint | 2 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.ib_rmv_loc_from_pg_$sp](../../StoredProcedures/me_01/dbo.ib_rmv_loc_from_pg_$sp.md)
- [me_01: dbo.insert_ib_price_$sp](../../StoredProcedures/me_01/dbo.insert_ib_price_$sp.md)
- [me_01: dbo.plu_common_price_$sp](../../StoredProcedures/me_01/dbo.plu_common_price_$sp.md)
- [me_01: dbo.plu_common_promo_price_$sp](../../StoredProcedures/me_01/dbo.plu_common_promo_price_$sp.md)
- [me_01: dbo.pop_25nov25_temp_sale_master_$sp](../../StoredProcedures/me_01/dbo.pop_25nov25_temp_sale_master_$sp.md)
- [me_01: dbo.pop_fixed_avg_cost_by_jurisdiction_$sp](../../StoredProcedures/me_01/dbo.pop_fixed_avg_cost_by_jurisdiction_$sp.md)
- [me_01: dbo.populate_ib_price_short_$sp](../../StoredProcedures/me_01/dbo.populate_ib_price_short_$sp.md)
- [me_01: dbo.populate_temp_sale_master_$sp](../../StoredProcedures/me_01/dbo.populate_temp_sale_master_$sp.md)
- [me_01: dbo.rebuild_ib_price_short_$sp](../../StoredProcedures/me_01/dbo.rebuild_ib_price_short_$sp.md)

