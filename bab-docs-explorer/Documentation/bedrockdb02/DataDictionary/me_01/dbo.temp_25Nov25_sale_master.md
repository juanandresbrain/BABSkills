# dbo.temp_25Nov25_sale_master

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_id | int | 4 | 0 | YES |  |  |
| transaction_date | datetime | 8 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| jurisdiction_id | smallint | 2 | 0 |  |  |  |
| sku_id | decimal | 9 | 0 | YES |  |  |
| style_id | decimal | 9 | 0 | YES |  |  |
| style_color_id | decimal | 9 | 0 | YES |  |  |
| color_id | smallint | 2 | 0 | YES |  |  |
| curr_price_status_id | smallint | 2 | 1 |  |  |  |
| curr_prm_val_unit_retail | decimal | 9 | 1 |  |  |  |
| curr_prm_sel_unit_retail | decimal | 9 | 1 |  |  |  |
| curr_eff_document_number | nvarchar | 40 | 1 |  |  |  |
| curr_effective_date | smalldatetime | 4 | 1 |  |  |  |
| curr_price_change_type | smallint | 2 | 1 |  |  |  |
| price_status_id | smallint | 2 | 1 |  |  |  |
| valuation_unit_retail | decimal | 9 | 1 |  |  |  |
| selling_unit_retail | decimal | 9 | 1 |  |  |  |
| start_price_status_id | smallint | 2 | 1 |  |  |  |
| start_val_unit_retail | decimal | 9 | 1 |  |  |  |
| start_sel_unit_retail | decimal | 9 | 1 |  |  |  |
| prm_price_status_id | smallint | 2 | 1 |  |  |  |
| prm_valuation_unit_retail | decimal | 9 | 1 |  |  |  |
| prm_selling_unit_retail | decimal | 9 | 1 |  |  |  |
| average_cost | decimal | 9 | 1 |  |  |  |
| exchange_rate | float | 8 | 1 |  |  |  |
| average_cost_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.pop_25Nov25_temp_ib_inv_$sp](../../StoredProcedures/me_01/dbo.pop_25Nov25_temp_ib_inv_$sp.md)
- [me_01: dbo.pop_25nov25_temp_sale_master_$sp](../../StoredProcedures/me_01/dbo.pop_25nov25_temp_sale_master_$sp.md)
- [me_01: dbo.pop_25Nov25_tmp_sale_md_audit_$sp](../../StoredProcedures/me_01/dbo.pop_25Nov25_tmp_sale_md_audit_$sp.md)
- [me_01: dbo.post_25Nov25_cust_order_sale_$sp](../../StoredProcedures/me_01/dbo.post_25Nov25_cust_order_sale_$sp.md)

