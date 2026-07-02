# dbo.tmpRecent

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style | nvarchar | 8000 | 1 |  |  |  |
| sku_desc | nvarchar | 8000 | 1 |  |  |  |
| hierarchy_group_label | nvarchar | 80 | 1 |  |  |  |
| hierarchy_group_code | nvarchar | 40 | 1 |  |  |  |
| US_HTS | nvarchar | 8000 | 1 |  |  |  |
| CA_HTS | nvarchar | 8000 | 1 |  |  |  |
| UK_HTS | nvarchar | 8000 | 1 |  |  |  |
| country | nvarchar | 8000 | 1 |  |  |  |
| style_created | datetime | 8 | 1 |  |  |  |
| recent_distro_date | datetime | 8 | 1 |  |  |  |

