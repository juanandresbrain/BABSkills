# dbo.bin_location

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| bin_location_id | decimal | 9 | 0 | YES |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| sku_id | decimal | 9 | 1 |  |  |  |
| pack_id | decimal | 9 | 1 |  |  |  |
| warehouse_code | nvarchar | 40 | 0 |  |  |  |
| warehouse_name | nvarchar | 120 | 0 |  |  |  |
| bin_type | tinyint | 1 | 0 |  |  |  |
| bin_loc_name | nvarchar | 40 | 0 |  |  |  |
| bin_seq_no | smallint | 2 | 0 |  |  |  |

