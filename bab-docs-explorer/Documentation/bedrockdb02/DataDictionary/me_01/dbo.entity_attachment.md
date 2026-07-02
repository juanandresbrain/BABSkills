# dbo.entity_attachment

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| entity_attachment_id | decimal | 9 | 0 | YES |  |  |
| attachment_type_id | decimal | 9 | 0 |  |  |  |
| parent_type | tinyint | 1 | 0 |  |  |  |
| parent_id | decimal | 9 | 0 |  |  |  |
| attachment_desc | nvarchar | 100 | 0 |  |  |  |
| attachment_date | smalldatetime | 4 | 0 |  |  |  |
| primary_flag | bit | 1 | 0 |  |  |  |
| url | nvarchar | 510 | 0 |  |  |  |

