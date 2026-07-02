# dbo.sysmail_attachments

**Database:** msdb  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| attachment_id | int | 4 | 0 |  |  |  |
| mailitem_id | int | 4 | 0 |  | YES |  |
| filename | nvarchar | 520 | 0 |  |  |  |
| filesize | int | 4 | 0 |  |  |  |
| attachment | varbinary | -1 | 1 |  |  |  |
| last_mod_date | datetime | 8 | 0 |  |  |  |
| last_mod_user | sysname | 256 | 0 |  |  |  |

