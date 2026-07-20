# dbo.jmc_sls_order

**Database:** LH_Mart_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| order_id | varchar | 8000 | 1 |  |  |  |
| business_date | varchar | 8000 | 1 |  |  |  |
| business_unit_id | varchar | 8000 | 1 |  |  |  |
| device_id | varchar | 8000 | 1 |  |  |  |
| total | decimal | 9 | 1 |  |  |  |
| pre_tender_balance_due | decimal | 9 | 1 |  |  |  |
| subtotal | decimal | 9 | 1 |  |  |  |
| tax_total | decimal | 9 | 1 |  |  |  |
| tax_total_for_display | decimal | 9 | 1 |  |  |  |
| discount_total | decimal | 9 | 1 |  |  |  |
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
| order_status_code | varchar | 8000 | 1 |  |  |  |
| order_type_code | varchar | 8000 | 1 |  |  |  |
| estimated_availability_date | varchar | 8000 | 1 |  |  |  |
| actual_availability_date | varchar | 8000 | 1 |  |  |  |
| order_due_date | varchar | 8000 | 1 |  |  |  |
| amount_due | decimal | 9 | 1 |  |  |  |
| payment_status_code | varchar | 8000 | 1 |  |  |  |
| fulfilling_business_unit_id | varchar | 8000 | 1 |  |  |  |
| pickup_business_unit_id | varchar | 8000 | 1 |  |  |  |
| handling_method_type_code | varchar | 8000 | 1 |  |  |  |
| handling_cost | decimal | 9 | 1 |  |  |  |
| handling_date | varchar | 8000 | 1 |  |  |  |
| handling_description | varchar | 8000 | 1 |  |  |  |
| create_time | datetime2 | 8 | 1 |  |  |  |
| create_by | varchar | 8000 | 1 |  |  |  |
| last_update_time | datetime2 | 8 | 1 |  |  |  |
| last_update_by | varchar | 8000 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
