# dbo.jumpmind_sls_retail_trans

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| device_id | varchar | 8000 | 1 |  |  |  |
| business_date | varchar | 8000 | 1 |  |  |  |
| sequence_number | bigint | 8 | 1 |  |  |  |
| total | decimal | 17 | 1 |  |  |  |
| pre_tender_balance_due | decimal | 17 | 1 |  |  |  |
| subtotal | decimal | 17 | 1 |  |  |  |
| tax_total | decimal | 17 | 1 |  |  |  |
| tax_total_for_display | decimal | 17 | 1 |  |  |  |
| discount_total | decimal | 17 | 1 |  |  |  |
| customer_id | varchar | 8000 | 1 |  |  |  |
| selling_channel_code | varchar | 8000 | 1 |  |  |  |
| loyalty_card_number | varchar | 8000 | 1 |  |  |  |
| tax_exempt_customer_id | varchar | 8000 | 1 |  |  |  |
| tax_exempt_certificate | varchar | 8000 | 1 |  |  |  |
| tax_exempt_code | varchar | 8000 | 1 |  |  |  |
| employee_id_for_discount | varchar | 8000 | 1 |  |  |  |
| iso_currency_code | varchar | 8000 | 1 |  |  |  |
| line_item_count | int | 4 | 1 |  |  |  |
| age_restricted_date_of_birth | datetime2 | 8 | 1 |  |  |  |
| item_count | int | 4 | 1 |  |  |  |
| customer_name | varchar | 8000 | 1 |  |  |  |
| tender_type_codes | varchar | 8000 | 1 |  |  |  |
| voidable_flag | int | 4 | 1 |  |  |  |
| tax_geo_code_origin | varchar | 8000 | 1 |  |  |  |
| rcpt_rtn_total | decimal | 17 | 1 |  |  |  |
| non_rcpt_rtn_total | decimal | 17 | 1 |  |  |  |
| customer_entry_method_code | varchar | 8000 | 1 |  |  |  |
| cust_other_id | varchar | 8000 | 1 |  |  |  |
| rcpt_rtn_count | int | 4 | 1 |  |  |  |
| non_rcpt_rtn_count | int | 4 | 1 |  |  |  |
| ring_elapsed_time_in_secs | int | 4 | 1 |  |  |  |
| tender_elapsed_time_in_secs | int | 4 | 1 |  |  |  |
| idle_elapsed_time_in_secs | int | 4 | 1 |  |  |  |
| lock_elapsed_time_in_secs | int | 4 | 1 |  |  |  |
| entry_mode_code | varchar | 8000 | 1 |  |  |  |
| suspended_reason_code | varchar | 8000 | 1 |  |  |  |
| suspended_note | varchar | 8000 | 1 |  |  |  |
| order_id | varchar | 8000 | 1 |  |  |  |
| loyalty_points_earned | decimal | 17 | 1 |  |  |  |
| customer_callout | varchar | 8000 | 1 |  |  |  |
| fiscal_control_number | varchar | 8000 | 1 |  |  |  |
| gift_receipt_print_type | varchar | 8000 | 1 |  |  |  |
| fiscal_processor_code | varchar | 8000 | 1 |  |  |  |
| create_time | datetime2 | 8 | 1 |  |  |  |
| create_by | varchar | 8000 | 1 |  |  |  |
| last_update_time | datetime2 | 8 | 1 |  |  |  |
| last_update_by | varchar | 8000 | 1 |  |  |  |
| party_id | varchar | 8000 | 1 |  |  |  |
| employee_name_for_discount | varchar | 8000 | 1 |  |  |  |
| event_id | varchar | 8000 | 1 |  |  |  |
| event_invoice | varchar | 8000 | 1 |  |  |  |
| extended_subtotal | decimal | 17 | 1 |  |  |  |
| parent_order_id | varchar | 8000 | 1 |  |  |  |
| additional_attributes | varchar | 8000 | 1 |  |  |  |
