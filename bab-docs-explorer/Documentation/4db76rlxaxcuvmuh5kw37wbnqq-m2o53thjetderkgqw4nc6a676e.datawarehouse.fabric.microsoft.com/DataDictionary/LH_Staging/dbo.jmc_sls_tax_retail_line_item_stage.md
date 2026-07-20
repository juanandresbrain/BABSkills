# dbo.jmc_sls_tax_retail_line_item_stage

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| device_id | varchar | 8000 | 1 |  |  |  |
| business_date | datetime2 | 8 | 1 |  |  |  |
| sequence_number | int | 4 | 1 |  |  |  |
| line_sequence_number | int | 4 | 1 |  |  |  |
| tax_line_sequence_number | int | 4 | 1 |  |  |  |
| authority_id | varchar | 8000 | 1 |  |  |  |
| authority_type | varchar | 8000 | 1 |  |  |  |
| group_id | varchar | 8000 | 1 |  |  |  |
| rule_name | varchar | 8000 | 1 |  |  |  |
| tax_type | varchar | 8000 | 1 |  |  |  |
| tax_holiday_indicator | int | 4 | 1 |  |  |  |
| rate_rule_sequence_number | int | 4 | 1 |  |  |  |
| override_applied | int | 4 | 1 |  |  |  |
| tax_exempt_id | varchar | 8000 | 1 |  |  |  |
| tax_exempt | int | 4 | 1 |  |  |  |
| tax_exempt_amount | decimal | 9 | 1 |  |  |  |
| override_percent | decimal | 9 | 1 |  |  |  |
| override_amount | decimal | 9 | 1 |  |  |  |
| override_reason_code | varchar | 8000 | 1 |  |  |  |
| tax_percentage | decimal | 9 | 1 |  |  |  |
| tax_amount | decimal | 9 | 1 |  |  |  |
| money_tax_amount | decimal | 9 | 1 |  |  |  |
| taxable_amount | decimal | 9 | 1 |  |  |  |
| iso_currency_code | varchar | 8000 | 1 |  |  |  |
| calculation_source | varchar | 8000 | 1 |  |  |  |
| tax_included_in_price | int | 4 | 1 |  |  |  |
| voided | int | 4 | 1 |  |  |  |
| override_user_id | varchar | 8000 | 1 |  |  |  |
| entry_method_code | varchar | 8000 | 1 |  |  |  |
| create_time | datetime2 | 8 | 1 |  |  |  |
| create_by | varchar | 8000 | 1 |  |  |  |
| last_update_by | varchar | 8000 | 1 |  |  |  |
| last_update_time | datetime2 | 8 | 1 |  |  |  |
