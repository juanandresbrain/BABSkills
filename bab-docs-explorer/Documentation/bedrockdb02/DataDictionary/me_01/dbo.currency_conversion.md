# dbo.currency_conversion

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| currency_conversion_id | decimal | 9 | 0 | YES |  |  |
| currency_conversion_type | smallint | 2 | 0 |  |  |  |
| from_currency_id | decimal | 9 | 0 |  |  |  |
| to_currency_id | decimal | 9 | 0 |  |  |  |
| exchange_rate | float | 8 | 0 |  |  |  |
| last_modified | smalldatetime | 4 | 0 |  |  |  |
| effective_from_date | smalldatetime | 4 | 0 |  |  |  |
| effective_to_date | smalldatetime | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.balance_cost_factors_$sp](../../StoredProcedures/me_01/dbo.balance_cost_factors_$sp.md)
- [me_01: dbo.cum_val_hist_$sp](../../StoredProcedures/me_01/dbo.cum_val_hist_$sp.md)
- [me_01: dbo.get_cost_rate_$sp](../../StoredProcedures/me_01/dbo.get_cost_rate_$sp.md)
- [me_01: dbo.get_pc_instruction_values_$sp](../../StoredProcedures/me_01/dbo.get_pc_instruction_values_$sp.md)
- [me_01: dbo.import_asn_forth_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_forth_step_$sp.md)
- [me_01: dbo.import_pc_populate_temp_pc_from_ib_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_temp_pc_from_ib_$sp.md)
- [me_01: dbo.insert_packs_bi_$sp](../../StoredProcedures/me_01/dbo.insert_packs_bi_$sp.md)
- [me_01: dbo.insert_pseudo_$sp](../../StoredProcedures/me_01/dbo.insert_pseudo_$sp.md)
- [me_01: dbo.insert_pseudo_bi_$sp](../../StoredProcedures/me_01/dbo.insert_pseudo_bi_$sp.md)
- [me_01: dbo.insert_pseudo_bi_ols_$sp](../../StoredProcedures/me_01/dbo.insert_pseudo_bi_ols_$sp.md)
- [me_01: dbo.insert_pseudo_ols_$sp](../../StoredProcedures/me_01/dbo.insert_pseudo_ols_$sp.md)
- [me_01: dbo.insert_skus_$sp](../../StoredProcedures/me_01/dbo.insert_skus_$sp.md)
- [me_01: dbo.insert_skus_bi_$sp](../../StoredProcedures/me_01/dbo.insert_skus_bi_$sp.md)
- [me_01: dbo.insert_skus_bi_ols_$sp](../../StoredProcedures/me_01/dbo.insert_skus_bi_ols_$sp.md)
- [me_01: dbo.insert_skus_ols_$sp](../../StoredProcedures/me_01/dbo.insert_skus_ols_$sp.md)
- [me_01: dbo.no_wms_create_ss_$sp](../../StoredProcedures/me_01/dbo.no_wms_create_ss_$sp.md)
- [me_01: dbo.pi_move_store_count_$sp](../../StoredProcedures/me_01/dbo.pi_move_store_count_$sp.md)
- [me_01: dbo.pi_update_inventory_tables_$sp](../../StoredProcedures/me_01/dbo.pi_update_inventory_tables_$sp.md)
- [me_01: dbo.pop_25nov25_temp_sale_master_$sp](../../StoredProcedures/me_01/dbo.pop_25nov25_temp_sale_master_$sp.md)
- [me_01: dbo.populate_dynamic_average_cost_$sp](../../StoredProcedures/me_01/dbo.populate_dynamic_average_cost_$sp.md)
- [me_01: dbo.populate_ib_cfd_$sp](../../StoredProcedures/me_01/dbo.populate_ib_cfd_$sp.md)
- [me_01: dbo.populate_ib_cost_retail_$sp](../../StoredProcedures/me_01/dbo.populate_ib_cost_retail_$sp.md)
- [me_01: dbo.populate_multi_currency_location_$sp](../../StoredProcedures/me_01/dbo.populate_multi_currency_location_$sp.md)
- [me_01: dbo.populate_temp_sale_master_$sp](../../StoredProcedures/me_01/dbo.populate_temp_sale_master_$sp.md)
- [me_01: dbo.prep_fixed_avg_cost_calculation_$sp](../../StoredProcedures/me_01/dbo.prep_fixed_avg_cost_calculation_$sp.md)
- [me_01: dbo.process_modified_transactions_$sp](../../StoredProcedures/me_01/dbo.process_modified_transactions_$sp.md)
- [me_01: dbo.sales_balancing_c$sp](../../StoredProcedures/me_01/dbo.sales_balancing_c$sp.md)
- [me_01: dbo.sales_balancing_l$sp](../../StoredProcedures/me_01/dbo.sales_balancing_l$sp.md)
- [me_01: dbo.spHearMeSalesConversion](../../StoredProcedures/me_01/dbo.spHearMeSalesConversion.md)
- [me_01: dbo.spHearMeSalesConversion_bak_01282020LT](../../StoredProcedures/me_01/dbo.spHearMeSalesConversion_bak_01282020LT.md)
- [me_01: dbo.spHearMeSalesConversion_BJB20190326](../../StoredProcedures/me_01/dbo.spHearMeSalesConversion_BJB20190326.md)

