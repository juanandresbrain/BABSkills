# dbo.imp_pack

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_pack_id | decimal | 9 | 0 | YES |  |  |
| pack_code | nvarchar | 40 | 0 |  |  |  |
| pack_description | nvarchar | 100 | 1 |  |  |  |
| pack_short_description | nvarchar | 40 | 1 |  |  |  |
| vendor_code | nvarchar | 40 | 1 |  |  |  |
| style_code | nvarchar | 40 | 1 |  |  |  |
| pack_type | tinyint | 1 | 1 |  |  |  |
| pack_status | tinyint | 1 | 1 |  |  |  |
| vendor_upc_flag | nvarchar | 2 | 1 |  |  |  |
| vendor_pack_code | nvarchar | 40 | 1 |  |  |  |
| active_flag | nvarchar | 2 | 1 |  |  |  |
| imp_file_name | nvarchar | 100 | 1 |  |  |  |
| concept_code | nvarchar | 40 | 1 |  |  |  |

