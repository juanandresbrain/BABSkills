# dbo.tblDBA_DDLChangesLog

**Database:** DBAUtility  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DDLChangeID | int | 4 | 0 |  |  |  |
| ServerName | nvarchar | 256 | 0 |  |  |  |
| EventType | nvarchar | -1 | 1 |  |  |  |
| SchemaName | nvarchar | -1 | 1 |  |  |  |
| ObjectName | nvarchar | -1 | 1 |  |  |  |
| ObjectType | nvarchar | -1 | 1 |  |  |  |
| EventDate | datetime | 8 | 1 |  |  |  |
| SystemUser | varchar | 100 | 1 |  |  |  |
| CurrentUser | varchar | 100 | 1 |  |  |  |
| OriginalUser | varchar | 100 | 1 |  |  |  |
| DatabaseName | varchar | 100 | 1 |  |  |  |
| TSQLCode | nvarchar | -1 | 1 |  |  |  |
| EmailSent | bit | 1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [DBAUtility: dbo.spDBA_Transfer_DDLChangesRepository](../../StoredProcedures/DBAUtility/dbo.spDBA_Transfer_DDLChangesRepository.md)

