# dbo.import_upc

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_upc_id | decimal | 9 | 0 | YES |  |  |
| entity_type | nvarchar | 4 | 0 |  |  |  |
| action_type | nchar | 2 | 0 |  |  |  |
| vendor_code | nvarchar | 40 | 1 |  |  |  |
| vendor_style | nvarchar | 80 | 1 |  |  |  |
| color_code | nvarchar | 6 | 1 |  |  |  |
| nrf_code | int | 4 | 1 |  |  |  |
| size_category_code | nvarchar | 16 | 1 |  |  |  |
| style_size_code | nvarchar | 34 | 1 |  |  |  |
| pack_code | nvarchar | 40 | 1 |  |  |  |
| ticket_label_override | nvarchar | 34 | 1 |  |  |  |
| reorder_flag | nchar | 2 | 1 |  |  |  |
| upc_number | nvarchar | 28 | 0 |  |  |  |
| upc_type | nchar | 2 | 0 |  |  |  |
| inhouse_upc_flag | nchar | 2 | 1 |  |  |  |
| first_part_inhouse | smallint | 2 | 1 |  |  |  |
| activation_date | smalldatetime | 4 | 1 |  |  |  |
| import_replication_queue_id | decimal | 9 | 1 |  |  |  |
| color_short_description | nvarchar | 16 | 1 |  |  |  |
| color_long_description | nvarchar | 40 | 1 |  |  |  |
| fashion_flag | nchar | 2 | 1 |  |  |  |
| color_reorder_flag | nchar | 2 | 1 |  |  |  |
| style_code | nvarchar | 40 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.dl_generate_upc_state_$sp](../../StoredProcedures/me_01/dbo.dl_generate_upc_state_$sp.md)

