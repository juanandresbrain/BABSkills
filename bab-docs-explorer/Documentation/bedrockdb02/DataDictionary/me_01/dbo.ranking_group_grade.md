# dbo.ranking_group_grade

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ranking_group_code | nvarchar | 40 | 0 | YES |  |  |
| grade | nvarchar | 20 | 0 | YES |  |  |
| minimum | int | 4 | 1 |  |  |  |
| maximum | int | 4 | 1 |  |  |  |
| weight | decimal | 5 | 1 |  |  |  |

