# dbo.sysdiagrams

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| name | sysname | 256 | 0 |  |  |  |
| principal_id | int | 4 | 0 |  |  |  |
| diagram_id | int | 4 | 0 | YES |  |  |
| version | int | 4 | 1 |  |  |  |
| definition | varbinary | -1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.sp_alterdiagram](../../StoredProcedures/me_01/dbo.sp_alterdiagram.md)
- [me_01: dbo.sp_creatediagram](../../StoredProcedures/me_01/dbo.sp_creatediagram.md)
- [me_01: dbo.sp_dropdiagram](../../StoredProcedures/me_01/dbo.sp_dropdiagram.md)
- [me_01: dbo.sp_helpdiagramdefinition](../../StoredProcedures/me_01/dbo.sp_helpdiagramdefinition.md)
- [me_01: dbo.sp_helpdiagrams](../../StoredProcedures/me_01/dbo.sp_helpdiagrams.md)
- [me_01: dbo.sp_renamediagram](../../StoredProcedures/me_01/dbo.sp_renamediagram.md)
- [me_01: dbo.sp_upgraddiagrams](../../StoredProcedures/me_01/dbo.sp_upgraddiagrams.md)
- [esell: dbo.sp_alterdiagram](../../StoredProcedures/esell/dbo.sp_alterdiagram.md)
- [esell: dbo.sp_creatediagram](../../StoredProcedures/esell/dbo.sp_creatediagram.md)
- [esell: dbo.sp_dropdiagram](../../StoredProcedures/esell/dbo.sp_dropdiagram.md)
- [esell: dbo.sp_helpdiagramdefinition](../../StoredProcedures/esell/dbo.sp_helpdiagramdefinition.md)
- [esell: dbo.sp_helpdiagrams](../../StoredProcedures/esell/dbo.sp_helpdiagrams.md)
- [esell: dbo.sp_renamediagram](../../StoredProcedures/esell/dbo.sp_renamediagram.md)
- [esell: dbo.sp_upgraddiagrams](../../StoredProcedures/esell/dbo.sp_upgraddiagrams.md)

