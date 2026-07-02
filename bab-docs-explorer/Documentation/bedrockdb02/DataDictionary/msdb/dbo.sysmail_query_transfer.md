# dbo.sysmail_query_transfer

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| uid | uniqueidentifier | 16 | 0 | YES |  |  |
| text_data | nvarchar | -1 | 1 |  |  |  |
| create_date | datetime | 8 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_send_dbmail](../../StoredProcedures/msdb/dbo.sp_send_dbmail.md)

