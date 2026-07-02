# dbo.plu_location_3904

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_id | smallint | 2 | 0 | YES |  |  |
| location_code | nvarchar | 40 | 1 |  |  |  |
| location_name | nvarchar | 120 | 1 |  |  |  |
| generate_plu_file_flag | bit | 1 | 1 |  |  |  |
| generate_thin_plu_file_flag | bit | 1 | 1 |  |  |  |
| language_id | int | 4 | 1 |  |  |  |
| locale_identifier | int | 4 | 1 |  |  |  |
| polling_reference | int | 4 | 1 |  |  |  |
| register_type_id | tinyint | 1 | 1 |  |  |  |
| location_status_id | tinyint | 1 | 1 |  |  |  |
| active_flag | bit | 1 | 1 |  |  |  |
| uses_oim_flag | bit | 1 | 1 |  |  |  |
| allow_customer_order_flag | bit | 1 | 1 |  |  |  |
| valid_flag | bit | 1 | 1 |  |  |  |
| full_regenerate_flag | bit | 1 | 1 |  |  |  |
| jurisdiction_id | smallint | 2 | 1 |  |  |  |
| jurisdiction_code | nvarchar | 40 | 1 |  |  |  |
| pricing_group_id | smallint | 2 | 1 |  |  |  |
| pricing_group_code | nvarchar | 20 | 1 |  |  |  |
| currency_id | decimal | 9 | 1 |  |  |  |
| tax_by_size_flag | bit | 1 | 1 |  |  |  |
| override_plu_key_to_sku | bit | 1 | 1 |  |  |  |

