# dbo.ActionRequest

**Database:** BABWForgetMe_Restore  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ActionRequestID | tinyint | 1 | 0 | YES |  |  |
| ActionRequestName | varchar | 32 | 0 |  |  |  |

## Referenced By Stored Procedures

- [BABWForgetMe_Restore: dbo.spForgetMeNewRequestEmail](../../StoredProcedures/BABWForgetMe_Restore/dbo.spForgetMeNewRequestEmail.md)
- [BABWForgetMe_Restore: dbo.spForgetMeRequestEmail](../../StoredProcedures/BABWForgetMe_Restore/dbo.spForgetMeRequestEmail.md)
- [BABWForgetMe_Restore: dbo.spGetCompleteActionStatusByDate](../../StoredProcedures/BABWForgetMe_Restore/dbo.spGetCompleteActionStatusByDate.md)
- [BABWForgetMe: dbo.spForgetMeNewRequestEmail](../../StoredProcedures/BABWForgetMe/dbo.spForgetMeNewRequestEmail.md)
- [BABWForgetMe: dbo.spForgetMeRequestEmail](../../StoredProcedures/BABWForgetMe/dbo.spForgetMeRequestEmail.md)
- [BABWForgetMe: dbo.spGetCompleteActionStatusByDate](../../StoredProcedures/BABWForgetMe/dbo.spGetCompleteActionStatusByDate.md)

