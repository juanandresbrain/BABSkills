# dbo.import_style_attachment

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_style_attachment_id | decimal | 9 | 0 | YES |  |  |
| entity_type | nvarchar | 4 | 0 |  |  |  |
| action_type | nchar | 2 | 0 |  |  |  |
| style_code | nvarchar | 40 | 0 |  |  |  |
| attachment_type_code | nvarchar | 6 | 1 |  |  |  |
| attachment_desc | nvarchar | 60 | 1 |  |  |  |
| attachment_date | smalldatetime | 4 | 1 |  |  |  |
| primary_flag | nchar | 2 | 1 |  |  |  |
| url | nvarchar | 510 | 1 |  |  |  |

