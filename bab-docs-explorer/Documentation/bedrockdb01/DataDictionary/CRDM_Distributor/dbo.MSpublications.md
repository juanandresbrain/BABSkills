# dbo.MSpublications

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| publisher_id | smallint | 2 | 0 |  |  |  |
| publisher_db | sysname | 256 | 1 |  |  |  |
| publication | sysname | 256 | 0 |  |  |  |
| publication_id | int | 4 | 0 | YES |  |  |
| publication_type | int | 4 | 0 |  |  |  |
| thirdparty_flag | bit | 1 | 0 |  |  |  |
| independent_agent | bit | 1 | 0 |  |  |  |
| immediate_sync | bit | 1 | 0 |  |  |  |
| allow_push | bit | 1 | 0 |  |  |  |
| allow_pull | bit | 1 | 0 |  |  |  |
| allow_anonymous | bit | 1 | 0 |  |  |  |
| description | nvarchar | 510 | 1 |  |  |  |
| vendor_name | nvarchar | 200 | 1 |  |  |  |
| retention | int | 4 | 1 |  |  |  |
| sync_method | int | 4 | 0 |  |  |  |
| allow_subscription_copy | bit | 1 | 0 |  |  |  |
| thirdparty_options | int | 4 | 1 |  |  |  |
| allow_queued_tran | bit | 1 | 0 |  |  |  |
| options | int | 4 | 0 |  |  |  |
| retention_period_unit | tinyint | 1 | 0 |  |  |  |
| allow_initialize_from_backup | bit | 1 | 0 |  |  |  |
| min_autonosync_lsn | varbinary | 16 | 1 |  |  |  |
