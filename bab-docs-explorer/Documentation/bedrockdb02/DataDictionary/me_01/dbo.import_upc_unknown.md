# dbo.import_upc_unknown

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_upc_id | decimal | 9 | 0 |  |  |  |
| entity_type | varchar | 2 | 0 |  |  |  |
| action_type | char | 1 | 0 |  |  |  |
| vendor_code | varchar | 20 | 1 |  |  |  |
| vendor_style | varchar | 40 | 1 |  |  |  |
| color_code | varchar | 3 | 1 |  |  |  |
| nrf_code | int | 4 | 1 |  |  |  |
| size_category_code | varchar | 8 | 1 |  |  |  |
| style_size_code | varchar | 17 | 1 |  |  |  |
| pack_code | varchar | 20 | 1 |  |  |  |
| ticket_label_override | varchar | 17 | 1 |  |  |  |
| reorder_flag | char | 1 | 1 |  |  |  |
| upc_number | varchar | 14 | 0 |  |  |  |
| upc_type | char | 1 | 0 |  |  |  |
| inhouse_upc_flag | char | 1 | 1 |  |  |  |
| first_part_inhouse | smallint | 2 | 1 |  |  |  |
| activation_date | smalldatetime | 4 | 1 |  |  |  |
| import_replication_queue_id | decimal | 9 | 1 |  |  |  |
| color_short_description | varchar | 8 | 1 |  |  |  |
| color_long_description | varchar | 20 | 1 |  |  |  |
| fashion_flag | char | 1 | 1 |  |  |  |
| color_reorder_flag | char | 1 | 1 |  |  |  |
| style_code | varchar | 20 | 1 |  |  |  |

