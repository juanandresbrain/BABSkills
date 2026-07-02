# dbo.ApplicationDim

**Database:** BABWForgetMe  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| AppKey | int | 4 | 0 | YES |  |  |
| AppName | varchar | 64 | 0 |  |  |  |
| AppTeam | varchar | 64 | 0 |  |  |  |
| TeamEmailAddress | varchar | 128 | 1 |  |  |  |
| AppCustName | varchar | 128 | 1 |  |  |  |
| ManualProcess | tinyint | 1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [BABWForgetMe_Restore: dbo.spForgetMeNewRequestEmail](../../StoredProcedures/BABWForgetMe_Restore/dbo.spForgetMeNewRequestEmail.md)
- [BABWForgetMe_Restore: dbo.spForgetMeRequestEmail](../../StoredProcedures/BABWForgetMe_Restore/dbo.spForgetMeRequestEmail.md)
- [BABWForgetMe: dbo.spForgetMeNewRequestEmail](../../StoredProcedures/BABWForgetMe/dbo.spForgetMeNewRequestEmail.md)
- [BABWForgetMe: dbo.spForgetMeRequestEmail](../../StoredProcedures/BABWForgetMe/dbo.spForgetMeRequestEmail.md)

