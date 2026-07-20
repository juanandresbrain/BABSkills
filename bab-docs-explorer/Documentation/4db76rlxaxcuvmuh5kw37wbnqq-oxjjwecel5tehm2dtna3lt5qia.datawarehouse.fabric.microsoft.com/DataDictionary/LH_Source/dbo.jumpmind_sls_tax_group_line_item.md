# dbo.jumpmind_sls_tax_group_line_item

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| device_id | varchar | 8000 | 1 |  |  |  |
| business_date | varchar | 8000 | 1 |  |  |  |
| sequence_number | bigint | 8 | 1 |  |  |  |
| line_sequence_number | int | 4 | 1 |  |  |  |
| authority_id | varchar | 8000 | 1 |  |  |  |
| authority_type | varchar | 8000 | 1 |  |  |  |
| group_id | varchar | 8000 | 1 |  |  |  |
| tax_type | varchar | 8000 | 1 |  |  |  |
| rule_name | varchar | 8000 | 1 |  |  |  |
| tax_percentage | decimal | 17 | 1 |  |  |  |
| tax_amount | decimal | 17 | 1 |  |  |  |
| money_tax_amount | decimal | 17 | 1 |  |  |  |
| taxable_amount | decimal | 17 | 1 |  |  |  |
| return_tax_flag | int | 4 | 1 |  |  |  |
| iso_currency_code | varchar | 8000 | 1 |  |  |  |
| tax_included_in_price | int | 4 | 1 |  |  |  |
| voided | int | 4 | 1 |  |  |  |
| override_user_id | varchar | 8000 | 1 |  |  |  |
| entry_method_code | varchar | 8000 | 1 |  |  |  |
| create_time | datetime2 | 8 | 1 |  |  |  |
| create_by | varchar | 8000 | 1 |  |  |  |
| last_update_time | datetime2 | 8 | 1 |  |  |  |
| last_update_by | varchar | 8000 | 1 |  |  |  |
| rule_description | varchar | 8000 | 1 |  |  |  |
