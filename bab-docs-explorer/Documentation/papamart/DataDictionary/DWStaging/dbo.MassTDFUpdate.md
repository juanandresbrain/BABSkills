# dbo.MassTDFUpdate

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| tdf_key | int | 4 | 1 |  |  |  |
| time_key | int | 4 | 1 |  |  |  |
| product_key | int | 4 | 1 |  |  |  |
| line_object_key | int | 4 | 1 |  |  |  |
| unit_gross_amount | numeric | 5 | 1 |  |  |  |
| unit_disc_amount | numeric | 5 | 1 |  |  |  |
| vat_tax_amount | numeric | 5 | 1 |  |  |  |
| units | int | 4 | 1 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| register_num | int | 4 | 1 |  |  |  |
| party_y_n | varchar | 1 | 1 |  |  |  |
| transaction_type_key | int | 4 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| reference_no | varchar | 80 | 1 |  |  |  |
| UPDT_DT | datetime | 8 | 1 |  |  |  |
| ETL_LOG_ID | int | 4 | 1 |  |  |  |
| upsell_disc_allocated | money | 8 | 1 |  |  |  |
| cashier_id | int | 4 | 1 |  |  |  |
| ext_Cost | money | 8 | 1 |  |  |  |
| line_action_key | int | 4 | 1 |  |  |  |
