# dbo.processing_code

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| processing_code_id | decimal | 9 | 0 | YES |  |  |
| processing_code | nvarchar | 16 | 0 |  |  |  |
| description | nvarchar | 60 | 0 |  |  |  |
| process_type | smallint | 2 | 0 |  |  |  |
| po_flag | bit | 1 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

