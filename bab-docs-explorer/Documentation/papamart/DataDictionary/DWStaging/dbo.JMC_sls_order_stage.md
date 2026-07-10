# dbo.JMC_sls_order_stage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| order_id | varchar | 128 | 0 |  |  |  |
| business_date | varchar | 10 | 1 |  |  |  |
| business_unit_id | varchar | 128 | 1 |  |  |  |
| device_id | varchar | 128 | 1 |  |  |  |
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
| iso_currency_code | varchar | 128 | 1 |  |  |  |
| line_item_count | int | 4 | 1 |  |  |  |
| age_restricted_date_of_birth | datetime | 8 | 1 |  |  |  |
| item_count | int | 4 | 1 |  |  |  |
| customer_name | varchar | 128 | 1 |  |  |  |
| tender_type_codes | varchar | 128 | 1 |  |  |  |
| voidable_flag | int | 4 | 1 |  |  |  |
| tax_geo_code_origin | varchar | 128 | 1 |  |  |  |
| order_status_code | varchar | 128 | 1 |  |  |  |
| order_type_code | varchar | 128 | 1 |  |  |  |
| estimated_availability_date | varchar | 128 | 1 |  |  |  |
| actual_availability_date | varchar | 128 | 1 |  |  |  |
| order_due_date | varchar | 128 | 1 |  |  |  |
| amount_due | numeric | 9 | 1 |  |  |  |
| payment_status_code | varchar | 128 | 1 |  |  |  |
| fulfilling_business_unit_id | varchar | 128 | 1 |  |  |  |
| pickup_business_unit_id | varchar | 128 | 1 |  |  |  |
| handling_method_type_code | varchar | 128 | 1 |  |  |  |
| handling_cost | numeric | 9 | 1 |  |  |  |
| handling_date | varchar | 128 | 1 |  |  |  |
| handling_description | varchar | 128 | 1 |  |  |  |
| create_time | datetime | 8 | 1 |  |  |  |
| create_by | varchar | 50 | 1 |  |  |  |
| last_update_time | datetime | 8 | 1 |  |  |  |
| last_update_by | varchar | 50 | 1 |  |  |  |
