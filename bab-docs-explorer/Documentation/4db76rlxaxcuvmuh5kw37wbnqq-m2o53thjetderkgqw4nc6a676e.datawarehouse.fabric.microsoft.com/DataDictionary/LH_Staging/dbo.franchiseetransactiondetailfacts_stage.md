# dbo.franchiseetransactiondetailfacts_stage

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| product_key | int | 4 | 1 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| transaction_id | varchar | 8000 | 1 |  |  |  |
| transaction_line_seq | int | 4 | 1 |  |  |  |
| register_num | int | 4 | 1 |  |  |  |
| cashier_id | int | 4 | 1 |  |  |  |
| time_key | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| unit_gross_amount | decimal | 17 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| units | int | 4 | 1 |  |  |  |
| unit_disc_amount | decimal | 17 | 1 |  |  |  |
| party_y_n | int | 4 | 1 |  |  |  |
| transaction_type_key | int | 4 | 1 |  |  |  |
| line_object_key | int | 4 | 1 |  |  |  |
| tdf_key | int | 4 | 1 |  |  |  |
| transaction_no | varchar | 8000 | 1 |  |  |  |
| reference_no | int | 4 | 1 |  |  |  |
| vat_tax_amount | decimal | 17 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
| UPDT_DT | datetime2 | 8 | 1 |  |  |  |
| etl_log_id | int | 4 | 1 |  |  |  |
| etl_evnt_id | int | 4 | 1 |  |  |  |
| upsell_disc_allocated | int | 4 | 1 |  |  |  |
| ext_cost | decimal | 17 | 1 |  |  |  |
| line_action_key | int | 4 | 1 |  |  |  |
