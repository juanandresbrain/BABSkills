# dbo.imp_jur_equivalency

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_jur_equivalency_id | decimal | 9 | 0 | YES |  |  |
| entity_type | nvarchar | 4 | 0 |  |  |  |
| action_type | nchar | 2 | 0 |  |  |  |
| jurisdiction_code | nvarchar | 40 | 0 |  |  |  |
| hierarchy_group_code | nvarchar | 40 | 0 |  |  |  |
| jurisdiction_equivalency_rate | decimal | 5 | 1 |  |  |  |

