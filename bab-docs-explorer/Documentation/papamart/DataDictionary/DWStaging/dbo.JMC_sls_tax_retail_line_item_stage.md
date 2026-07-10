# dbo.JMC_sls_tax_retail_line_item_stage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| device_id | varchar | 128 | 0 |  |  |  |
| business_date | smalldatetime | 4 | 1 |  |  |  |
| sequence_number | int | 4 | 0 |  |  |  |
| line_sequence_number | int | 4 | 0 |  |  |  |
| tax_line_sequence_number | int | 4 | 0 |  |  |  |
| authority_id | varchar | 128 | 1 |  |  |  |
| authority_type | varchar | 128 | 1 |  |  |  |
| group_id | varchar | 128 | 1 |  |  |  |
| rule_name | varchar | 128 | 1 |  |  |  |
| tax_type | varchar | 128 | 1 |  |  |  |
| tax_holiday_indicator | int | 4 | 1 |  |  |  |
| rate_rule_sequence_number | int | 4 | 1 |  |  |  |
| override_applied | int | 4 | 1 |  |  |  |
| tax_exempt_id | varchar | 128 | 1 |  |  |  |
| tax_exempt | int | 4 | 1 |  |  |  |
| tax_exempt_amount | numeric | 9 | 1 |  |  |  |
| override_percent | numeric | 9 | 1 |  |  |  |
| override_amount | numeric | 9 | 1 |  |  |  |
| override_reason_code | varchar | 128 | 1 |  |  |  |
| tax_percentage | numeric | 9 | 1 |  |  |  |
| tax_amount | numeric | 9 | 1 |  |  |  |
| money_tax_amount | numeric | 9 | 1 |  |  |  |
| taxable_amount | numeric | 9 | 1 |  |  |  |
| iso_currency_code | varchar | 128 | 0 |  |  |  |
| calculation_source | varchar | 128 | 1 |  |  |  |
| tax_included_in_price | int | 4 | 1 |  |  |  |
| voided | int | 4 | 1 |  |  |  |
| override_user_id | varchar | 128 | 1 |  |  |  |
| entry_method_code | varchar | 128 | 1 |  |  |  |
| create_time | datetime | 8 | 0 |  |  |  |
| create_by | varchar | 50 | 0 |  |  |  |
| last_update_by | varchar | 50 | 0 |  |  |  |
| last_update_time | datetime | 8 | 1 |  |  |  |
