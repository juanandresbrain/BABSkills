# dbo.tmpTransactionDetailFactsUpdatedTmp

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| product_key | int | 4 | 0 |  |  |  |
| currency_key | int | 4 | 0 |  |  |  |
| transaction_id | decimal | 9 | 0 |  |  |  |
| transaction_line_seq | decimal | 5 | 1 |  |  |  |
| Register_Num | int | 4 | 0 |  |  |  |
| cashier_id | int | 4 | 1 |  |  |  |
| time_key | int | 4 | 0 |  |  |  |
| store_key | int | 4 | 0 |  |  |  |
| unit_gross_amount | decimal | 5 | 1 |  |  |  |
| date_key | int | 4 | 0 |  |  |  |
| units | int | 4 | 1 |  |  |  |
| unit_disc_amount | decimal | 5 | 1 |  |  |  |
| party_y_n | char | 1 | 1 |  |  |  |
| transaction_type_key | int | 4 | 1 |  |  |  |
| line_object_key | int | 4 | 1 |  |  |  |
| tdf_key | int | 4 | 0 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| reference_no | varchar | 80 | 1 |  |  |  |
| vat_tax_amount | decimal | 5 | 1 |  |  |  |
| INS_DT | datetime | 8 | 1 |  |  |  |
| UPDT_DT | datetime | 8 | 1 |  |  |  |
| ETL_LOG_ID | int | 4 | 1 |  |  |  |
| ETL_EVNT_ID | int | 4 | 1 |  |  |  |
| upsell_disc_allocated | money | 8 | 1 |  |  |  |
| ext_cost | money | 8 | 1 |  |  |  |
