# dbo.JMC_sls_retail_trans

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| device_id | varchar | 128 | 0 |  |  |  |
| business_date | smalldatetime | 4 | 1 |  |  |  |
| sequence_number | bigint | 8 | 0 |  |  |  |
| total | numeric | 9 | 1 |  |  |  |
| pre_tender_balance_due | numeric | 9 | 1 |  |  |  |
| subtotal | numeric | 9 | 1 |  |  |  |
| tax_total | numeric | 9 | 1 |  |  |  |
| tax_total_for_display | numeric | 9 | 1 |  |  |  |
| discount_total | numeric | 9 | 1 |  |  |  |
| customer_id | varchar | 128 | 1 |  |  |  |
| selling_channel_code | varchar | 128 | 1 |  |  |  |
| loyalty_card_number | varchar | 128 | 1 |  |  |  |
| tax_exempt_customer_id | varchar | 128 | 1 |  |  |  |
| tax_exempt_certificate | varchar | 128 | 1 |  |  |  |
| tax_exempt_code | varchar | 128 | 1 |  |  |  |
| employee_id_for_discount | varchar | 128 | 1 |  |  |  |
| iso_currency_code | varchar | 128 | 0 |  |  |  |
| line_item_count | int | 4 | 1 |  |  |  |
| item_count | int | 4 | 1 |  |  |  |
| customer_name | varchar | 128 | 1 |  |  |  |
| tender_type_codes | varchar | 128 | 1 |  |  |  |
| voidable_flag | int | 4 | 1 |  |  |  |
| tax_geo_code_origin | varchar | 128 | 1 |  |  |  |
| rcpt_rtn_total | numeric | 9 | 1 |  |  |  |
| non_rcpt_rtn_total | numeric | 9 | 1 |  |  |  |
| customer_entry_method_code | varchar | 128 | 1 |  |  |  |
| cust_other_id | varchar | 128 | 1 |  |  |  |
| rcpt_rtn_count | int | 4 | 1 |  |  |  |
| non_rcpt_rtn_count | int | 4 | 1 |  |  |  |
| ring_elapsed_time_in_secs | int | 4 | 1 |  |  |  |
| tender_elapsed_time_in_secs | int | 4 | 1 |  |  |  |
| idle_elapsed_time_in_secs | int | 4 | 1 |  |  |  |
| lock_elapsed_time_in_secs | int | 4 | 1 |  |  |  |
| entry_mode_code | varchar | 128 | 1 |  |  |  |
| suspended_reason_code | varchar | 128 | 1 |  |  |  |
| suspended_note | varchar | 128 | 1 |  |  |  |
| order_id | varchar | 128 | 1 |  |  |  |
| loyalty_points_earned | numeric | 9 | 1 |  |  |  |
| customer_callout | varchar | 128 | 1 |  |  |  |
| fiscal_control_number | varchar | 128 | 1 |  |  |  |
| gift_receipt_print_type | varchar | 128 | 1 |  |  |  |
| fiscal_processor_code | varchar | 128 | 1 |  |  |  |
| create_time | datetime | 8 | 0 |  |  |  |
| create_by | varchar | 50 | 0 |  |  |  |
| last_update_by | varchar | 50 | 0 |  |  |  |
| last_update_time | datetime | 8 | 1 |  |  |  |
| party_id | varchar | 128 | 1 |  |  |  |
| employee_name_for_discount | varchar | 128 | 1 |  |  |  |
| event_id | varchar | 128 | 1 |  |  |  |
| event_invoice | varchar | 128 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| age_restricted_date_of_birth | smalldatetime | 4 | 1 |  |  |  |
