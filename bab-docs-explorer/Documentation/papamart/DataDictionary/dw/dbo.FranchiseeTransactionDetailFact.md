# dbo.FranchiseeTransactionDetailFact

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tdf_key | int | 4 | 0 | YES |  |  |
| product_key | int | 4 | 0 |  |  |  |
| currency_key | int | 4 | 0 |  |  |  |
| transaction_id | varchar | 20 | 0 |  |  |  |
| transaction_line_seq | int | 4 | 0 |  |  |  |
| register_num | int | 4 | 0 |  |  |  |
| cashier_id | int | 4 | 1 |  |  |  |
| time_key | int | 4 | 0 |  |  |  |
| store_key | int | 4 | 0 |  |  |  |
| unit_gross_amount | numeric | 17 | 1 |  |  |  |
| date_key | int | 4 | 0 |  |  |  |
| units | int | 4 | 1 |  |  |  |
| unit_disc_amount | numeric | 17 | 1 |  |  |  |
| party_y_n | char | 1 | 1 |  |  |  |
| transaction_type_key | int | 4 | 1 |  |  |  |
| line_object_key | int | 4 | 1 |  |  |  |
| transaction_no | varchar | 20 | 0 |  |  |  |
| reference_no | int | 4 | 1 |  |  |  |
| vat_tax_amount | numeric | 17 | 1 |  |  |  |
| upsell_disc_allocated | int | 4 | 0 |  |  |  |
| ext_cost | numeric | 17 | 1 |  |  |  |
| line_action_key | int | 4 | 1 |  |  |  |
| INS_DT | datetime | 8 | 0 |  |  |  |
| UPDT_DT | datetime | 8 | 0 |  |  |  |
| etl_log_id | int | 4 | 1 |  |  |  |
| etl_evnt_id | int | 4 | 1 |  |  |  |
