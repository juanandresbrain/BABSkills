# dbo.d365_weeklysales

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store | varchar | 8000 | 1 |  |  |  |
| product_key | varchar | 8000 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| merch_year_wk | varchar | 8000 | 1 |  |  |  |
| perm_md_retail | decimal | 17 | 1 |  |  |  |
| perm_mu_retail | decimal | 17 | 1 |  |  |  |
| promo_pc_total_retail | decimal | 17 | 1 |  |  |  |
| promo_pc_total_retail_te | decimal | 17 | 1 |  |  |  |
| distributions_units | decimal | 17 | 1 |  |  |  |
| distributions_retail | decimal | 17 | 1 |  |  |  |
| received_units | decimal | 17 | 1 |  |  |  |
| received_retail | decimal | 17 | 1 |  |  |  |
| transfer_in_units | decimal | 17 | 1 |  |  |  |
| transfer_in_retail | decimal | 17 | 1 |  |  |  |
| transfer_out_units | decimal | 17 | 1 |  |  |  |
| transfer_out_retail | decimal | 17 | 1 |  |  |  |
| sales_total_units | decimal | 17 | 1 |  |  |  |
| sales_total_retail | decimal | 17 | 1 |  |  |  |
| sales_total_retail_us_te | decimal | 17 | 1 |  |  |  |
| sales_total_retail_native_te | decimal | 17 | 1 |  |  |  |
| sales_total_cost | decimal | 17 | 1 |  |  |  |
| return_units | decimal | 17 | 1 |  |  |  |
| return_retail | decimal | 17 | 1 |  |  |  |
| return_retail_us_te | decimal | 17 | 1 |  |  |  |
| return_cost | decimal | 17 | 1 |  |  |  |
| return_retail_native_te | decimal | 17 | 1 |  |  |  |
| shrink_actual_units | decimal | 17 | 1 |  |  |  |
| shrink_actual_retail | decimal | 17 | 1 |  |  |  |
| return_cost_native | decimal | 17 | 1 |  |  |  |
| sales_total_cost_native | decimal | 17 | 1 |  |  |  |
| adjustments_total_units | decimal | 17 | 1 |  |  |  |
| adjustments_retail | decimal | 17 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
| style_code | varchar | 8000 | 1 |  |  |  |
| jurisdiction_code | varchar | 8000 | 1 |  |  |  |
| LegalEntity | varchar | 8000 | 1 |  |  |  |
