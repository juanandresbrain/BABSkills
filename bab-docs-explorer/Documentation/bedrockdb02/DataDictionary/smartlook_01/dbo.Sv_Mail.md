# dbo.Sv_Mail

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| mail_id | int | 4 | 0 | YES |  |  |
| user_id | int | 4 | 0 |  |  |  |
| send_id | int | 4 | 0 |  |  |  |
| topic_id | int | 4 | 0 |  |  |  |
| send_date | smalldatetime | 4 | 0 |  |  |  |
| read_date | smalldatetime | 4 | 1 |  |  |  |
| message | text | 16 | 1 |  |  |  |
| attached_type | smallint | 2 | 0 |  |  |  |
| attached_id | int | 4 | 0 |  |  |  |
| output_data | varchar | 100 | 1 |  |  |  |
| crosstab_data | varchar | 100 | 1 |  |  |  |
| graph_data | varchar | 100 | 1 |  |  |  |
| default_data_view | char | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Sv_AddObjToFolderFromMail](../../StoredProcedures/fn_01/dbo.Sv_AddObjToFolderFromMail.md)
- [fn_01: dbo.Sv_GetObjRefCount](../../StoredProcedures/fn_01/dbo.Sv_GetObjRefCount.md)
- [fn_01: dbo.Sv_UpdateNextID](../../StoredProcedures/fn_01/dbo.Sv_UpdateNextID.md)
- [smartlook_01: dbo.Sv_AddObjToFolderFromMail](../../StoredProcedures/smartlook_01/dbo.Sv_AddObjToFolderFromMail.md)
- [smartlook_01: dbo.Sv_GetObjRefCount](../../StoredProcedures/smartlook_01/dbo.Sv_GetObjRefCount.md)
- [smartlook_01: dbo.Sv_UpdateNextID](../../StoredProcedures/smartlook_01/dbo.Sv_UpdateNextID.md)

