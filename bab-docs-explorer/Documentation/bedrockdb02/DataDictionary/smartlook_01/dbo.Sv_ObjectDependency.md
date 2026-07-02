# dbo.Sv_ObjectDependency

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| object_id | int | 4 | 0 | YES |  |  |
| use_sequence | int | 4 | 0 | YES |  |  |
| use_object_id | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Sv_CleanDependency](../../StoredProcedures/fn_01/dbo.Sv_CleanDependency.md)
- [smartlook_01: dbo.Sv_CleanDependency](../../StoredProcedures/smartlook_01/dbo.Sv_CleanDependency.md)

