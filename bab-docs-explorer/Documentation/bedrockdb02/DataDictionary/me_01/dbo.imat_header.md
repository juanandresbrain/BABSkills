# dbo.imat_header

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imat_header_id | decimal | 9 | 0 | YES |  |  |
| invoice_number | nvarchar | 48 | 0 |  |  |  |
| discount_date | smalldatetime | 4 | 0 |  |  |  |
| due_date | smalldatetime | 4 | 0 |  |  |  |
| entry_date_time | smalldatetime | 4 | 0 |  |  |  |
| exchange_rate | float | 8 | 0 |  |  |  |
| gross_amount_payable | decimal | 9 | 0 |  |  |  |
| invoice_date | smalldatetime | 4 | 0 |  |  |  |
| invoice_item_flag | bit | 1 | 0 |  |  |  |
| invoice_status_code | tinyint | 1 | 0 |  |  |  |
| state_no | int | 4 | 0 |  |  |  |
| match_cost_discount_amount | decimal | 9 | 0 |  |  |  |
| match_other_discount_amount | decimal | 9 | 0 |  |  |  |
| match_date_time | smalldatetime | 4 | 1 |  |  |  |
| match_net_amount | decimal | 9 | 0 |  |  |  |
| match_status_code | tinyint | 1 | 0 |  |  |  |
| payment_reference_number | nvarchar | 60 | 1 |  |  |  |
| payment_status_code | tinyint | 1 | 0 |  |  |  |
| scan_file_name | nvarchar | 60 | 1 |  |  |  |
| terms_discount_amount | decimal | 9 | 0 |  |  |  |
| transaction_type | int | 4 | 0 |  |  |  |
| entry_mode | tinyint | 1 | 0 |  |  |  |
| release_date | smalldatetime | 4 | 1 |  |  |  |
| currency_id | decimal | 9 | 0 |  |  |  |
| gl_distribution_set_id | decimal | 9 | 0 |  |  |  |
| invoice_reference_id | decimal | 9 | 1 |  |  |  |
| remit_to_vendor_id | decimal | 9 | 1 |  |  |  |
| terms_id | decimal | 9 | 1 |  |  |  |
| vendor_id | decimal | 9 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| updatestamp | decimal | 5 | 0 |  |  |  |
| invoice_adjustment_flag | bit | 1 | 0 |  |  |  |
| jurisdiction_id | smallint | 2 | 1 |  |  |  |
| total_tax_amount_calculated | decimal | 9 | 1 |  |  |  |
| total_tax_amount_charged | decimal | 9 | 1 |  |  |  |
| tax_valid_flag | bit | 1 | 0 |  |  |  |
| manually_matched_flag | bit | 1 | 0 |  |  |  |
| itc_user_set_flag | bit | 1 | 0 |  |  |  |
| user_id | numeric | 9 | 1 |  |  |  |
| gl_company_no | tinyint | 1 | 1 |  |  |  |

