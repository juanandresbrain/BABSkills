# dbo.application_server

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| application_server_id | T_ID | 16 | 0 | YES |  |  |
| server_name | nvarchar | 120 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingInsertMinMaxProfileArchive](../../StoredProcedures/me_01/dbo.spMerchandisingInsertMinMaxProfileArchive.md)

