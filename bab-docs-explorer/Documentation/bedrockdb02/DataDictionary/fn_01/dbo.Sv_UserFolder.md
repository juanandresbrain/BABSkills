# dbo.Sv_UserFolder

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| folder_id | int | 4 | 0 | YES |  |  |
| user_id | int | 4 | 0 |  |  |  |
| topic_id | int | 4 | 0 |  |  |  |
| folder_type | smallint | 2 | 0 |  |  |  |
| folder_level | smallint | 2 | 0 |  |  |  |
| folder_name | nvarchar | 60 | 0 |  |  |  |
| period_id | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Sv_AddNewFolder](../../StoredProcedures/fn_01/dbo.Sv_AddNewFolder.md)
- [fn_01: dbo.Sv_AddObjToFolderType](../../StoredProcedures/fn_01/dbo.Sv_AddObjToFolderType.md)
- [fn_01: dbo.Sv_AutoTargetFolder](../../StoredProcedures/fn_01/dbo.Sv_AutoTargetFolder.md)
- [fn_01: dbo.Sv_UpdateNextID](../../StoredProcedures/fn_01/dbo.Sv_UpdateNextID.md)
- [smartlook_01: dbo.Sv_AddNewFolder](../../StoredProcedures/smartlook_01/dbo.Sv_AddNewFolder.md)
- [smartlook_01: dbo.Sv_AddObjToFolderType](../../StoredProcedures/smartlook_01/dbo.Sv_AddObjToFolderType.md)
- [smartlook_01: dbo.Sv_AutoTargetFolder](../../StoredProcedures/smartlook_01/dbo.Sv_AutoTargetFolder.md)
- [smartlook_01: dbo.Sv_UpdateNextID](../../StoredProcedures/smartlook_01/dbo.Sv_UpdateNextID.md)

