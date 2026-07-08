# dbo.MSsubscriptions

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| publisher_database_id | int | 4 | 0 |  |  |  |
| publisher_id | smallint | 2 | 0 |  |  |  |
| publisher_db | sysname | 256 | 0 |  |  |  |
| publication_id | int | 4 | 0 |  |  |  |
| article_id | int | 4 | 0 |  |  |  |
| subscriber_id | smallint | 2 | 0 |  |  |  |
| subscriber_db | sysname | 256 | 0 |  |  |  |
| subscription_type | int | 4 | 0 |  |  |  |
| sync_type | tinyint | 1 | 0 |  |  |  |
| status | tinyint | 1 | 0 |  |  |  |
| subscription_seqno | varbinary | 16 | 0 |  |  |  |
| snapshot_seqno_flag | bit | 1 | 0 |  |  |  |
| independent_agent | bit | 1 | 0 |  |  |  |
| subscription_time | datetime | 8 | 0 |  |  |  |
| loopback_detection | bit | 1 | 0 |  |  |  |
| agent_id | int | 4 | 0 |  |  |  |
| update_mode | tinyint | 1 | 0 |  |  |  |
| publisher_seqno | varbinary | 16 | 0 |  |  |  |
| ss_cplt_seqno | varbinary | 16 | 0 |  |  |  |
| nosync_type | tinyint | 1 | 0 |  |  |  |
