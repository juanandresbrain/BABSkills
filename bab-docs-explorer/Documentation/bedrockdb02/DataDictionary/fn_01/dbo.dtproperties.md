# dbo.dtproperties

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 | YES |  |  |
| objectid | int | 4 | 1 |  |  |  |
| property | varchar | 64 | 0 | YES |  |  |
| value | varchar | 255 | 1 |  |  |  |
| uvalue | nvarchar | 510 | 1 |  |  |  |
| lvalue | image | 16 | 1 |  |  |  |
| version | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.sp_upgraddiagrams](../../StoredProcedures/me_01/dbo.sp_upgraddiagrams.md)
- [esell: dbo.sp_upgraddiagrams](../../StoredProcedures/esell/dbo.sp_upgraddiagrams.md)

