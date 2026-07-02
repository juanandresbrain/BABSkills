# dbo.tempLT_min_max_history

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Week | datetime | 8 | 1 |  |  |  |
| Begin | datetime | 8 | 1 |  |  |  |
| End | datetime | 8 | 1 |  |  |  |
| Duration | varchar | 50 | 1 |  |  |  |
| ProfileCount | varchar | 50 | 1 |  |  |  |
| ProfilesUpdated | nvarchar | 100 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingMinMaxHistory](../../StoredProcedures/me_01/dbo.spMerchandisingMinMaxHistory.md)

