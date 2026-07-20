# dbo.jumpmind_sls_trans_summary

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| device_id | varchar | 8000 | 1 |  |  |  |
| business_date | varchar | 8000 | 1 |  |  |  |
| sequence_number | bigint | 8 | 1 |  |  |  |
| business_unit_id | varchar | 8000 | 1 |  |  |  |
| device_type | varchar | 8000 | 1 |  |  |  |
| trans_type_code | varchar | 8000 | 1 |  |  |  |
| trans_status_code | varchar | 8000 | 1 |  |  |  |
| username | varchar | 8000 | 1 |  |  |  |
| begin_time | datetime2 | 8 | 1 |  |  |  |
| end_time | datetime2 | 8 | 1 |  |  |  |
| local_offset | int | 4 | 1 |  |  |  |
| client_offset | int | 4 | 1 |  |  |  |
| transaction_duration_in_sec | bigint | 8 | 1 |  |  |  |
| training_mode | int | 4 | 1 |  |  |  |
| barcode | varchar | 8000 | 1 |  |  |  |
| session_id | varchar | 8000 | 1 |  |  |  |
| till_id | varchar | 8000 | 1 |  |  |  |
| customer_id | varchar | 8000 | 1 |  |  |  |
| loyalty_card_number | varchar | 8000 | 1 |  |  |  |
| customer_name | varchar | 8000 | 1 |  |  |  |
| employee_id_for_discount | varchar | 8000 | 1 |  |  |  |
| voidable_flag | int | 4 | 1 |  |  |  |
| item_count | int | 4 | 1 |  |  |  |
| rcpt_rtn_count | int | 4 | 1 |  |  |  |
| non_rcpt_rtn_count | int | 4 | 1 |  |  |  |
| iso_currency_code | varchar | 8000 | 1 |  |  |  |
| total | decimal | 17 | 1 |  |  |  |
| pre_tender_balance_due | decimal | 17 | 1 |  |  |  |
| tax_total | decimal | 17 | 1 |  |  |  |
| discount_total | decimal | 17 | 1 |  |  |  |
| tender_type_codes | varchar | 8000 | 1 |  |  |  |
| tender1_type_code | varchar | 8000 | 1 |  |  |  |
| tender1_amount | decimal | 17 | 1 |  |  |  |
| tender1_card_type_code | varchar | 8000 | 1 |  |  |  |
| tender1_masked_card_number | varchar | 8000 | 1 |  |  |  |
| tender1_auth_code | varchar | 8000 | 1 |  |  |  |
| tender2_type_code | varchar | 8000 | 1 |  |  |  |
| tender2_amount | decimal | 17 | 1 |  |  |  |
| tender2_card_type_code | varchar | 8000 | 1 |  |  |  |
| tender2_masked_card_number | varchar | 8000 | 1 |  |  |  |
| tender2_auth_code | varchar | 8000 | 1 |  |  |  |
| tender3_type_code | varchar | 8000 | 1 |  |  |  |
| tender3_amount | decimal | 17 | 1 |  |  |  |
| tender3_card_type_code | varchar | 8000 | 1 |  |  |  |
| tender3_masked_card_number | varchar | 8000 | 1 |  |  |  |
| tender3_auth_code | varchar | 8000 | 1 |  |  |  |
| tender4_type_code | varchar | 8000 | 1 |  |  |  |
| tender4_amount | decimal | 17 | 1 |  |  |  |
| tender4_card_type_code | varchar | 8000 | 1 |  |  |  |
| tender4_masked_card_number | varchar | 8000 | 1 |  |  |  |
| tender4_auth_code | varchar | 8000 | 1 |  |  |  |
| tender5_type_code | varchar | 8000 | 1 |  |  |  |
| tender5_amount | decimal | 17 | 1 |  |  |  |
| tender5_card_type_code | varchar | 8000 | 1 |  |  |  |
| tender5_masked_card_number | varchar | 8000 | 1 |  |  |  |
| tender5_auth_code | varchar | 8000 | 1 |  |  |  |
| voided_sequence_number | bigint | 8 | 1 |  |  |  |
| suspended_sequence_number | bigint | 8 | 1 |  |  |  |
| suspended_device_id | varchar | 8000 | 1 |  |  |  |
| resumed_sequence_number | bigint | 8 | 1 |  |  |  |
| resumed_device_id | varchar | 8000 | 1 |  |  |  |
| reason_code | varchar | 8000 | 1 |  |  |  |
| paid_to | varchar | 8000 | 1 |  |  |  |
| store_bank_id | varchar | 8000 | 1 |  |  |  |
| mfr_coupons_total | decimal | 17 | 1 |  |  |  |
| mfr_coupons_count | int | 4 | 1 |  |  |  |
| mfr_coupons_taxable_total | decimal | 17 | 1 |  |  |  |
| mfr_coupons_taxable_count | int | 4 | 1 |  |  |  |
| mfr_coupons_non_taxable_total | decimal | 17 | 1 |  |  |  |
| mfr_coupons_non_taxable_count | int | 4 | 1 |  |  |  |
| store_promos_total | decimal | 17 | 1 |  |  |  |
| store_promos_count | int | 4 | 1 |  |  |  |
| store_physical_coupons_total | decimal | 17 | 1 |  |  |  |
| store_physical_coupons_count | int | 4 | 1 |  |  |  |
| store_electronic_promos_total | decimal | 17 | 1 |  |  |  |
| store_electronic_promos_count | int | 4 | 1 |  |  |  |
| store_promos_taxable_total | decimal | 17 | 1 |  |  |  |
| store_promos_taxable_count | int | 4 | 1 |  |  |  |
| store_promos_non_taxable_total | decimal | 17 | 1 |  |  |  |
| store_promos_non_taxable_count | int | 4 | 1 |  |  |  |
| total_physical_coupons_count | int | 4 | 1 |  |  |  |
| loyalty_rewards_total | decimal | 17 | 1 |  |  |  |
| loyalty_rewards_count | int | 4 | 1 |  |  |  |
| create_time | datetime2 | 8 | 1 |  |  |  |
| create_by | varchar | 8000 | 1 |  |  |  |
| last_update_time | datetime2 | 8 | 1 |  |  |  |
| last_update_by | varchar | 8000 | 1 |  |  |  |
