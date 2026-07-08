# dbo.IHsubscriptions

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| article_id | int | 4 | 0 |  |  |  |
| srvid | smallint | 2 | 0 |  |  |  |
| dest_db | sysname | 256 | 0 |  |  |  |
| login_name | sysname | 256 | 0 |  |  |  |
| distribution_jobid | binary | 16 | 0 |  |  |  |
| timestamp | timestamp | 8 | 1 |  |  |  |
| queued_reinit | bit | 1 | 0 |  |  |  |
| status | tinyint | 1 | 0 |  |  |  |
| sync_type | tinyint | 1 | 0 |  |  |  |
| subscription_type | int | 4 | 0 |  |  |  |
| update_mode | tinyint | 1 | 0 |  |  |  |
| loopback_detection | bit | 1 | 0 |  |  |  |
| nosync_type | tinyint | 1 | 0 |  |  |  |
| srvname | sysname | 256 | 0 |  |  |  |
