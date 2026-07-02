# dbo.sysmail_attachments_transfer

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transfer_id | int | 4 | 0 | YES |  |  |
| uid | uniqueidentifier | 16 | 0 |  |  |  |
| filename | nvarchar | 520 | 0 |  |  |  |
| filesize | int | 4 | 0 |  |  |  |
| attachment | varbinary | -1 | 1 |  |  |  |
| create_date | datetime | 8 | 0 |  |  |  |

