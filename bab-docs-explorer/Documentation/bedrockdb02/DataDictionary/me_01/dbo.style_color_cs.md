# dbo.style_color_cs

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_color_id | decimal | 9 | 0 | YES |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| color_id | smallint | 2 | 0 |  |  |  |
| long_desc | nvarchar | 40 | 0 |  |  |  |
| short_desc | nvarchar | 16 | 0 |  |  |  |
| fashion_flag | bit | 1 | 0 |  |  |  |
| reorder_flag | bit | 1 | 0 |  |  |  |
| attachment_url | nvarchar | 510 | 1 |  |  |  |
| red_value | decimal | 5 | 1 |  |  |  |
| green_value | decimal | 5 | 1 |  |  |  |
| blue_value | decimal | 5 | 1 |  |  |  |

