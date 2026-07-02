# dbo.mass_modification

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| mass_modification_id | decimal | 9 | 0 | YES |  |  |
| mass_modification_type | smallint | 2 | 0 |  |  |  |
| mass_modification_status | smallint | 2 | 0 |  |  |  |
| description | nvarchar | 120 | 1 |  |  |  |
| scheduled_date | datetime | 8 | 1 |  |  |  |
| execution_date | datetime | 8 | 1 |  |  |  |
| user_id | numeric | 9 | 0 |  |  |  |

