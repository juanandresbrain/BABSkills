# dbo.ma_weeklysales

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_code | varchar | 8000 | 1 |  |  |  |
| jurisdiction_code | varchar | 8000 | 1 |  |  |  |
| LegalEntity | int | 4 | 1 |  |  |  |
| store_key | varchar | 8000 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| merch_year_wk | int | 4 | 1 |  |  |  |
| perm_md_retail | decimal | 9 | 1 |  |  |  |
| perm_mu_retail | decimal | 9 | 1 |  |  |  |
| perm_mdc_retail | decimal | 9 | 1 |  |  |  |
| perm_muc_retail | decimal | 9 | 1 |  |  |  |
| promo_pc_total_retail | decimal | 9 | 1 |  |  |  |
| promo_pc_total_retail_te | decimal | 9 | 1 |  |  |  |
| received_units | int | 4 | 1 |  |  |  |
| received_retail | decimal | 9 | 1 |  |  |  |
| return_to_vendor_units | int | 4 | 1 |  |  |  |
| return_to_vendor_retail | decimal | 9 | 1 |  |  |  |
| distributions_units | int | 4 | 1 |  |  |  |
| distributions_retail | decimal | 9 | 1 |  |  |  |
| transfer_in_units | int | 4 | 1 |  |  |  |
| transfer_in_retail | decimal | 9 | 1 |  |  |  |
| transfer_out_units | int | 4 | 1 |  |  |  |
| transfer_out_retail | decimal | 9 | 1 |  |  |  |
| sales_total_units | int | 4 | 1 |  |  |  |
| sales_total_retail | decimal | 9 | 1 |  |  |  |
| sales_total_retail_us_te | decimal | 9 | 1 |  |  |  |
| sales_total_retail_native_te | decimal | 9 | 1 |  |  |  |
| sales_total_cost | decimal | 9 | 1 |  |  |  |
| return_units | int | 4 | 1 |  |  |  |
| return_retail | decimal | 9 | 1 |  |  |  |
| return_retail_us_te | decimal | 9 | 1 |  |  |  |
| return_retail_native_te | decimal | 9 | 1 |  |  |  |
| return_cost | decimal | 9 | 1 |  |  |  |
| shrink_actual_units | int | 4 | 1 |  |  |  |
| shrink_actual_retail | decimal | 9 | 1 |  |  |  |
| adjustments_total_units | int | 4 | 1 |  |  |  |
| adjustments_total_retail | decimal | 9 | 1 |  |  |  |
| sales_total_cost_native | decimal | 9 | 1 |  |  |  |
| return_cost_native | decimal | 9 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
