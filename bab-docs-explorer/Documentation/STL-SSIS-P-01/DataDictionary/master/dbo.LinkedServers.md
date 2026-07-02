# dbo.LinkedServers

**Database:** master  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LinkedServerName | sysname | 256 | 0 |  |  |  |
| Product | sysname | 256 | 0 |  |  |  |
| provider | sysname | 256 | 0 |  |  |  |
| data_source | nvarchar | 8000 | 1 |  |  |  |
| catalog | sysname | 256 | 1 |  |  |  |
| is_linked | bit | 1 | 0 |  |  |  |
| remote_name | sysname | 256 | 1 |  |  |  |

