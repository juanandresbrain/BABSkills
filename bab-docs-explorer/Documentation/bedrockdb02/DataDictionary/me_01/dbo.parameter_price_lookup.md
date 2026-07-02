# dbo.parameter_price_lookup

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| parameter_price_lookup_id | tinyint | 1 | 0 | YES |  |  |
| main_directory | varchar | 50 | 0 |  |  |  |
| transmission_log_directory | varchar | 50 | 0 |  |  |  |
| error_log_directory | varchar | 50 | 0 |  |  |  |
| plu_key | smallint | 2 | 0 |  |  |  |
| use_mix_match_flag | bit | 1 | 0 |  |  |  |
| override_for_style_flag | bit | 1 | 0 |  |  |  |
| retrieve_group_code_flag | bit | 1 | 0 |  |  |  |
| send_price_change_flag | bit | 1 | 0 |  |  |  |
| shared_attribute_id | decimal | 9 | 0 |  |  |  |
| use_ftp_flag | bit | 1 | 0 |  |  |  |
| use_style_level_flag | bit | 1 | 0 |  |  |  |
| send_description_flag | bit | 1 | 0 |  |  |  |
| send_check_digit_flag | bit | 1 | 0 |  |  |  |
| upc_style_code_length | tinyint | 1 | 1 |  |  |  |
| unix_server_address | varchar | 50 | 1 |  |  |  |
| unix_account | varchar | 20 | 1 |  |  |  |
| unix_password | varchar | 20 | 1 |  |  |  |
| backup_directory_pipeline | varchar | 50 | 1 |  |  |  |
| backup_directory_application | varchar | 50 | 1 |  |  |  |
| backup_retention_period | smallint | 2 | 1 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| tax_by_size_flag | bit | 1 | 0 |  |  |  |
| last_crq_id | decimal | 9 | 0 |  |  |  |
| crs_location_batch_size | smallint | 2 | 0 |  |  |  |
| crs_style_batch_size | int | 4 | 0 |  |  |  |
| price_lookup_days | int | 4 | 0 |  |  |  |
| item_no_lookup_length | int | 4 | 0 |  |  |  |
| last_crs_crq_id | decimal | 9 | 0 |  |  |  |
| brand_attribute_id | decimal | 9 | 1 |  |  |  |
| override_plu_key_to_sku | bit | 1 | 0 |  |  |  |
| upc_no_lookup_length | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.imw_price_change_v1_$sp](../../StoredProcedures/me_01/dbo.imw_price_change_v1_$sp.md)
- [me_01: dbo.plu_crs_del_temp_output_$sp](../../StoredProcedures/me_01/dbo.plu_crs_del_temp_output_$sp.md)
- [me_01: dbo.plu_crs_temp_output_$sp](../../StoredProcedures/me_01/dbo.plu_crs_temp_output_$sp.md)
- [me_01: dbo.plu_deleted_item_$sp](../../StoredProcedures/me_01/dbo.plu_deleted_item_$sp.md)
- [me_01: dbo.plu_key_$sp](../../StoredProcedures/me_01/dbo.plu_key_$sp.md)
- [me_01: dbo.plu_output_$sp](../../StoredProcedures/me_01/dbo.plu_output_$sp.md)
- [me_01: dbo.plu_regen_queue_$sp](../../StoredProcedures/me_01/dbo.plu_regen_queue_$sp.md)
- [me_01: dbo.plu_resend_queue_$sp](../../StoredProcedures/me_01/dbo.plu_resend_queue_$sp.md)
- [me_01: dbo.plu_shared_attribute_$sp](../../StoredProcedures/me_01/dbo.plu_shared_attribute_$sp.md)
- [me_01: dbo.plu_style_queue_$sp](../../StoredProcedures/me_01/dbo.plu_style_queue_$sp.md)

