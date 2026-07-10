# dbo.tblDBA_DDLChangesRepository

**Database:** DBAUtilityMaster  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DDLChangeID | int | 4 | 0 | YES |  |  |
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
