# dbo.count_import_temp

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| count_import_temp_id | decimal | 9 | 0 | YES |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| upc_number | nvarchar | 28 | 1 |  |  |  |
| zone_label | nvarchar | 30 | 1 |  |  |  |
| units_counted | int | 4 | 0 |  |  |  |
| cost | decimal | 9 | 1 |  |  |  |
| total_retail | decimal | 9 | 1 |  |  |  |
| location_code | nvarchar | 40 | 1 |  |  |  |
| import_error | nvarchar | 240 | 1 |  |  |  |
| pack_code | nvarchar | 40 | 1 |  |  |  |
| cost_local | decimal | 9 | 1 |  |  |  |
| total_valuation_retail | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.insert_packs_$sp](../../StoredProcedures/me_01/dbo.insert_packs_$sp.md)
- [me_01: dbo.insert_packs_bi_$sp](../../StoredProcedures/me_01/dbo.insert_packs_bi_$sp.md)
- [me_01: dbo.insert_pseudo_$sp](../../StoredProcedures/me_01/dbo.insert_pseudo_$sp.md)
- [me_01: dbo.insert_pseudo_bi_$sp](../../StoredProcedures/me_01/dbo.insert_pseudo_bi_$sp.md)
- [me_01: dbo.insert_skus_$sp](../../StoredProcedures/me_01/dbo.insert_skus_$sp.md)
- [me_01: dbo.insert_skus_bi_$sp](../../StoredProcedures/me_01/dbo.insert_skus_bi_$sp.md)
- [me_01: dbo.pi_load_retail_data_loc_$sp](../../StoredProcedures/me_01/dbo.pi_load_retail_data_loc_$sp.md)
- [me_01: dbo.pi_process_loc_$sp](../../StoredProcedures/me_01/dbo.pi_process_loc_$sp.md)
- [me_01: dbo.pi_update_inventory_tables_$sp](../../StoredProcedures/me_01/dbo.pi_update_inventory_tables_$sp.md)

