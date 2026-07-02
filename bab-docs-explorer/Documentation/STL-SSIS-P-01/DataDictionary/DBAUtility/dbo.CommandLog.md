# dbo.CommandLog

**Database:** DBAUtility  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ID | int | 4 | 0 | YES |  |  |
| DatabaseName | sysname | 256 | 1 |  |  |  |
| SchemaName | sysname | 256 | 1 |  |  |  |
| ObjectName | sysname | 256 | 1 |  |  |  |
| ObjectType | char | 2 | 1 |  |  |  |
| IndexName | sysname | 256 | 1 |  |  |  |
| IndexType | tinyint | 1 | 1 |  |  |  |
| StatisticsName | sysname | 256 | 1 |  |  |  |
| PartitionNumber | int | 4 | 1 |  |  |  |
| ExtendedInfo | xml | -1 | 1 |  |  |  |
| Command | nvarchar | -1 | 0 |  |  |  |
| CommandType | nvarchar | 120 | 0 |  |  |  |
| StartTime | datetime | 8 | 0 |  |  |  |
| EndTime | datetime | 8 | 1 |  |  |  |
| ErrorNumber | int | 4 | 1 |  |  |  |
| ErrorMessage | nvarchar | -1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [DBAUtility: dbo.CommandExecute](../../StoredProcedures/DBAUtility/dbo.CommandExecute.md)

