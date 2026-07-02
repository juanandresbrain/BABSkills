# dbo.posting_parameter

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | decimal | 9 | 0 | YES |  |  |
| posting_date | smalldatetime | 4 | 0 |  |  |  |
| starting_job_id | int | 4 | 0 |  |  |  |
| from_ib_inventory_id | decimal | 9 | 1 |  |  |  |
| to_ib_inventory_id | decimal | 9 | 1 |  |  |  |
| from_ib_cost_factor_disc_id | decimal | 9 | 1 |  |  |  |
| to_ib_cost_factor_disc_id | decimal | 9 | 1 |  |  |  |
| from_ib_allocation_id | decimal | 9 | 1 |  |  |  |
| to_ib_allocation_id | decimal | 9 | 1 |  |  |  |
| from_ib_on_order_id | decimal | 9 | 1 |  |  |  |
| to_ib_on_order_id | decimal | 9 | 1 |  |  |  |
| init_posting_flag | bit | 1 | 0 |  |  |  |
| cmp_posting_flag | bit | 1 | 0 |  |  |  |
| flsh_posting_flag | bit | 1 | 0 |  |  |  |
| hist_posting_flag | bit | 1 | 0 |  |  |  |
| oh_posting_flag | bit | 1 | 0 |  |  |  |
| oo_all_posting_flag | bit | 1 | 0 |  |  |  |
| cmp_first_phase_flag | bit | 1 | 0 |  |  |  |
| flsh_first_phase_flag | bit | 1 | 0 |  |  |  |
| hist_first_phase_flag | bit | 1 | 0 |  |  |  |
| oh_first_phase_flag | bit | 1 | 0 |  |  |  |
| oo_all_first_phase_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerification](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerification.md)
- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2.md)
- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2V2](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2V2.md)
- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJCtest](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJCtest.md)
- [ma_01: dbo.get_last_range_end_phase2_$sp](../../StoredProcedures/ma_01/dbo.get_last_range_end_phase2_$sp.md)
- [ma_01: dbo.initial_load_posting_parameter_$sp](../../StoredProcedures/ma_01/dbo.initial_load_posting_parameter_$sp.md)
- [ma_01: dbo.prep_cmp_$sp](../../StoredProcedures/ma_01/dbo.prep_cmp_$sp.md)
- [ma_01: dbo.prep_flash_$sp](../../StoredProcedures/ma_01/dbo.prep_flash_$sp.md)
- [ma_01: dbo.prep_hist_$sp](../../StoredProcedures/ma_01/dbo.prep_hist_$sp.md)
- [ma_01: dbo.prep_new_posting_$sp](../../StoredProcedures/ma_01/dbo.prep_new_posting_$sp.md)
- [ma_01: dbo.prep_oh_$sp](../../StoredProcedures/ma_01/dbo.prep_oh_$sp.md)
- [ma_01: dbo.prep_oo_all_$sp](../../StoredProcedures/ma_01/dbo.prep_oo_all_$sp.md)
- [ma_01: dbo.prep_roll_oh_$sp](../../StoredProcedures/ma_01/dbo.prep_roll_oh_$sp.md)
- [ma_01: dbo.prep_wrk_cmp_$sp](../../StoredProcedures/ma_01/dbo.prep_wrk_cmp_$sp.md)
- [ma_01: dbo.prep_wrk_flash_$sp](../../StoredProcedures/ma_01/dbo.prep_wrk_flash_$sp.md)
- [ma_01: dbo.prep_wrk_hist_$sp](../../StoredProcedures/ma_01/dbo.prep_wrk_hist_$sp.md)
- [ma_01: dbo.prep_wrk_ib_$sp](../../StoredProcedures/ma_01/dbo.prep_wrk_ib_$sp.md)
- [ma_01: dbo.prep_wrk_ib_allocation_$sp](../../StoredProcedures/ma_01/dbo.prep_wrk_ib_allocation_$sp.md)
- [ma_01: dbo.prep_wrk_ib_cost_fact_disc_$sp](../../StoredProcedures/ma_01/dbo.prep_wrk_ib_cost_fact_disc_$sp.md)
- [ma_01: dbo.prep_wrk_ib_inventory_$sp](../../StoredProcedures/ma_01/dbo.prep_wrk_ib_inventory_$sp.md)
- [ma_01: dbo.prep_wrk_ib_on_order_$sp](../../StoredProcedures/ma_01/dbo.prep_wrk_ib_on_order_$sp.md)
- [ma_01: dbo.prep_wrk_oh_$sp](../../StoredProcedures/ma_01/dbo.prep_wrk_oh_$sp.md)
- [ma_01: dbo.prep_wrk_oo_all_$sp](../../StoredProcedures/ma_01/dbo.prep_wrk_oo_all_$sp.md)
- [ma_01: dbo.validate_cmp_$sp](../../StoredProcedures/ma_01/dbo.validate_cmp_$sp.md)
- [ma_01: dbo.validate_flash_$sp](../../StoredProcedures/ma_01/dbo.validate_flash_$sp.md)
- [ma_01: dbo.validate_hist_$sp](../../StoredProcedures/ma_01/dbo.validate_hist_$sp.md)
- [ma_01: dbo.validate_oh_$sp](../../StoredProcedures/ma_01/dbo.validate_oh_$sp.md)
- [ma_01: dbo.validate_oo_all_$sp](../../StoredProcedures/ma_01/dbo.validate_oo_all_$sp.md)
- [ma_01: dbo.validate_wrk_cmp_$sp](../../StoredProcedures/ma_01/dbo.validate_wrk_cmp_$sp.md)
- [ma_01: dbo.validate_wrk_flash_$sp](../../StoredProcedures/ma_01/dbo.validate_wrk_flash_$sp.md)
- [ma_01: dbo.validate_wrk_hist_$sp](../../StoredProcedures/ma_01/dbo.validate_wrk_hist_$sp.md)
- [ma_01: dbo.validate_wrk_ib_$sp](../../StoredProcedures/ma_01/dbo.validate_wrk_ib_$sp.md)
- [ma_01: dbo.validate_wrk_oh_$sp](../../StoredProcedures/ma_01/dbo.validate_wrk_oh_$sp.md)
- [ma_01: dbo.validate_wrk_oo_all_$sp](../../StoredProcedures/ma_01/dbo.validate_wrk_oo_all_$sp.md)

