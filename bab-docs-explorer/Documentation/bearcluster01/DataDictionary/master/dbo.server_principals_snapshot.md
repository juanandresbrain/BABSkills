# dbo.server_principals_snapshot

**Database:** master  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| name | sysname | 256 | 0 |  |  |  |
| sid | varbinary | 85 | 1 |  |  |  |
| type_desc | sysname | 256 | 0 |  |  |  |
| create_date | datetime | 8 | 1 |  |  |  |
| modify_date | datetime | 8 | 1 |  |  |  |
| action | sysname | 256 | 1 |  |  |  |

