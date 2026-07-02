# dbo.plu_location

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_id | smallint | 2 | 0 | YES |  |  |
| generate_plu_file_flag | bit | 1 | 0 |  |  |  |
| register_type_id | tinyint | 1 | 0 |  |  |  |
| location_status_id | tinyint | 1 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| uses_oim_flag | bit | 1 | 1 |  |  |  |
| allow_customer_order_flag | bit | 1 | 1 |  |  |  |
| language_id | int | 4 | 1 |  |  |  |
| generate_thin_plu_file_flag | bit | 1 | 0 |  |  |  |
| tax_by_size_flag | bit | 1 | 0 |  |  |  |
| override_plu_key_to_sku | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.plu_regen_queue_$sp](../../StoredProcedures/me_01/dbo.plu_regen_queue_$sp.md)

