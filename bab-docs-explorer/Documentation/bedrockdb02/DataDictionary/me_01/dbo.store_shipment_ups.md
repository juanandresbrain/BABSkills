# dbo.store_shipment_ups

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | bigint | 8 | 0 |  |  |  |
| destid | varchar | 4 | 1 |  |  |  |
| sourceid | varchar | 4 | 1 |  |  |  |
| rec_type | varchar | 6 | 1 |  |  |  |
| message | nvarchar | 510 | 1 |  |  |  |
| style_code | varchar | 20 | 1 |  |  |  |
| quantity | int | 4 | 1 |  |  |  |
| release_date | datetime | 8 | 1 |  |  |  |
| distribution_number | varchar | 50 | 1 |  |  |  |
| ref_field_1 | varchar | 20 | 1 |  |  |  |
| short_desc | varchar | 20 | 1 |  |  |  |
| vendor_style | varchar | 40 | 1 |  |  |  |
| color_code | varchar | 3 | 1 |  |  |  |
| exported_date | datetime | 8 | 1 |  |  |  |

