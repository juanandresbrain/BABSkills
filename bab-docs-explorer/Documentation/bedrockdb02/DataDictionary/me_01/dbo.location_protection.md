# dbo.location_protection

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_id | smallint | 2 | 0 |  |  |  |
| hierarchy_group_id | int | 4 | 1 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| protection_level | smallint | 2 | 0 |  |  |  |
| effective_begin_date | datetime | 8 | 1 |  |  |  |
| effective_end_date | datetime | 8 | 1 |  |  |  |

