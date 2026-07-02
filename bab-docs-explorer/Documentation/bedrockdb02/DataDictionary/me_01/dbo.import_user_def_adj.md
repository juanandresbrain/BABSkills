# dbo.import_user_def_adj

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_user_def_adj_id | decimal | 9 | 0 | YES |  |  |
| action_code | nvarchar | 2 | 0 |  |  |  |
| document_no | nvarchar | 40 | 1 |  |  |  |
| location_code | nvarchar | 40 | 0 |  |  |  |
| reason_code | nvarchar | 10 | 0 |  |  |  |
| performed_by | nvarchar | 120 | 1 |  |  |  |
| upc_number | nvarchar | 28 | 1 |  |  |  |
| style_number | nvarchar | 40 | 1 |  |  |  |
| color_code | nvarchar | 16 | 1 |  |  |  |
| primary_size | nvarchar | 16 | 1 |  |  |  |
| secondary_size | nvarchar | 16 | 1 |  |  |  |
| units_to_adjust | int | 4 | 1 |  |  |  |
| cost_to_adjust | decimal | 9 | 1 |  |  |  |
| date_submitted | smalldatetime | 4 | 0 |  |  |  |

