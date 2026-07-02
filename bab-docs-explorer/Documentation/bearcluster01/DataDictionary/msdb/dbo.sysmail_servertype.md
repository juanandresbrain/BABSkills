# dbo.sysmail_servertype

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| servertype | sysname | 256 | 0 | YES |  |  |
| is_incoming | bit | 1 | 0 |  |  |  |
| is_outgoing | bit | 1 | 0 |  |  |  |
| last_mod_datetime | datetime | 8 | 0 |  |  |  |
| last_mod_user | sysname | 256 | 0 |  |  |  |

