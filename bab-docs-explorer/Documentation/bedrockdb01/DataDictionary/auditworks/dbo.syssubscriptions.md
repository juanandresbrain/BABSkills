# dbo.syssubscriptions

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| artid | int | 4 | 0 |  |  |  |
| srvid | smallint | 2 | 0 |  |  |  |
| dest_db | sysname | 256 | 0 |  |  |  |
| status | tinyint | 1 | 0 |  |  |  |
| sync_type | tinyint | 1 | 0 |  |  |  |
| login_name | sysname | 256 | 0 |  |  |  |
| subscription_type | int | 4 | 0 |  |  |  |
| distribution_jobid | binary | 16 | 1 |  |  |  |
| timestamp | timestamp | 8 | 0 |  |  |  |
| update_mode | tinyint | 1 | 0 |  |  |  |
| loopback_detection | bit | 1 | 0 |  |  |  |
| queued_reinit | bit | 1 | 0 |  |  |  |
| nosync_type | tinyint | 1 | 0 |  |  |  |
| srvname | sysname | 256 | 0 |  |  |  |
