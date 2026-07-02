# dbo.pack_cs

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| pack_id | decimal | 9 | 0 | YES |  |  |
| pack_code | nvarchar | 40 | 0 |  |  |  |
| pack_description | nvarchar | 100 | 0 |  |  |  |
| pack_short_description | nvarchar | 40 | 0 |  |  |  |
| pack_status | smallint | 2 | 0 |  |  |  |
| pack_type | tinyint | 1 | 0 |  |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| vendor_id | decimal | 9 | 0 |  |  |  |
| vendor_pack_code | nvarchar | 40 | 1 |  |  |  |
| vendor_upc_flag | bit | 1 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| multi_color_flag | bit | 1 | 0 |  |  |  |
| bin_location | nvarchar | 20 | 1 |  |  |  |
| document_source | tinyint | 1 | 0 |  |  |  |
| export_status | tinyint | 1 | 1 |  |  |  |

