# dbo.transaction_detail_facts

**Database:** LH_Mart_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| product_key | int | 4 | 1 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| transaction_id | decimal | 9 | 1 |  |  |  |
| transaction_line_seq | decimal | 5 | 1 |  |  |  |
| Register_Num | int | 4 | 1 |  |  |  |
| cashier_id | int | 4 | 1 |  |  |  |
| time_key | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| unit_gross_amount | decimal | 5 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| units | int | 4 | 1 |  |  |  |
| unit_disc_amount | decimal | 5 | 1 |  |  |  |
| party_y_n | varchar | 8000 | 1 |  |  |  |
| transaction_type_key | int | 4 | 1 |  |  |  |
| line_object_key | int | 4 | 1 |  |  |  |
| tdf_key | int | 4 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| reference_no | varchar | 8000 | 1 |  |  |  |
| vat_tax_amount | decimal | 5 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
| UPDT_DT | datetime2 | 8 | 1 |  |  |  |
| ETL_LOG_ID | int | 4 | 1 |  |  |  |
| ETL_EVNT_ID | int | 4 | 1 |  |  |  |
| upsell_disc_allocated | decimal | 9 | 1 |  |  |  |
| ext_cost | decimal | 9 | 1 |  |  |  |
| line_action_key | int | 4 | 1 |  |  |  |
