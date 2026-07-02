# dbo.import_style_description

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_style_description_id | decimal | 9 | 0 | YES |  |  |
| entity_type | nvarchar | 4 | 0 |  |  |  |
| action_type | nchar | 2 | 0 |  |  |  |
| style_code | nvarchar | 40 | 0 |  |  |  |
| locale_identifier | smallint | 2 | 0 |  |  |  |
| long_desc | nvarchar | 240 | 1 |  |  |  |
| short_desc | nvarchar | 40 | 1 |  |  |  |
| plu_description | nvarchar | 80 | 1 |  |  |  |

