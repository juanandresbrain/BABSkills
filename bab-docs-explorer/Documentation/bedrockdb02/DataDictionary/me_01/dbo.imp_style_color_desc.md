# dbo.imp_style_color_desc

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_style_color_desc_id | decimal | 9 | 0 | YES |  |  |
| entity_type | nvarchar | 4 | 0 |  |  |  |
| action_type | nvarchar | 2 | 0 |  |  |  |
| style_code | nvarchar | 40 | 0 |  |  |  |
| color_code | nvarchar | 6 | 0 |  |  |  |
| locale_identifier | smallint | 2 | 0 |  |  |  |
| long_desc | nvarchar | 40 | 1 |  |  |  |
| short_desc | nvarchar | 16 | 1 |  |  |  |

