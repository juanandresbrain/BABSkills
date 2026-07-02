# dbo.Sv_FolderItem

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| folder_id | int | 4 | 0 | YES |  |  |
| item_sequence | smallint | 2 | 0 | YES |  |  |
| item_type | smallint | 2 | 0 |  |  |  |
| item_id | int | 4 | 0 |  |  |  |
| output_data | varchar | 100 | 1 |  |  |  |
| crosstab_data | varchar | 100 | 1 |  |  |  |
| graph_data | varchar | 100 | 1 |  |  |  |
| default_data_view | char | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Sv_AddObjToFolder](../../StoredProcedures/fn_01/dbo.Sv_AddObjToFolder.md)
- [fn_01: dbo.Sv_AddObjToFolderFromFolder](../../StoredProcedures/fn_01/dbo.Sv_AddObjToFolderFromFolder.md)
- [fn_01: dbo.Sv_AddObjToFolderFromMail](../../StoredProcedures/fn_01/dbo.Sv_AddObjToFolderFromMail.md)
- [fn_01: dbo.Sv_AddObjToFolderType](../../StoredProcedures/fn_01/dbo.Sv_AddObjToFolderType.md)
- [fn_01: dbo.Sv_GetObjRefCount](../../StoredProcedures/fn_01/dbo.Sv_GetObjRefCount.md)
- [fn_01: dbo.Sv_ObjCountByName](../../StoredProcedures/fn_01/dbo.Sv_ObjCountByName.md)
- [smartlook_01: dbo.Sv_AddObjToFolder](../../StoredProcedures/smartlook_01/dbo.Sv_AddObjToFolder.md)
- [smartlook_01: dbo.Sv_AddObjToFolderFromFolder](../../StoredProcedures/smartlook_01/dbo.Sv_AddObjToFolderFromFolder.md)
- [smartlook_01: dbo.Sv_AddObjToFolderFromMail](../../StoredProcedures/smartlook_01/dbo.Sv_AddObjToFolderFromMail.md)
- [smartlook_01: dbo.Sv_AddObjToFolderType](../../StoredProcedures/smartlook_01/dbo.Sv_AddObjToFolderType.md)
- [smartlook_01: dbo.Sv_GetObjRefCount](../../StoredProcedures/smartlook_01/dbo.Sv_GetObjRefCount.md)
- [smartlook_01: dbo.Sv_ObjCountByName](../../StoredProcedures/smartlook_01/dbo.Sv_ObjCountByName.md)

