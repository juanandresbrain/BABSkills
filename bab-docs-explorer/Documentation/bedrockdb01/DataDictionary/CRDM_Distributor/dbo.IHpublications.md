# dbo.IHpublications

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| pubid | int | 4 | 0 |  |  |  |
| name | sysname | 256 | 0 |  |  |  |
| repl_freq | tinyint | 1 | 0 |  |  |  |
| status | tinyint | 1 | 0 |  |  |  |
| sync_method | tinyint | 1 | 0 |  |  |  |
| snapshot_jobid | binary | 16 | 1 |  |  |  |
| enabled_for_internet | bit | 1 | 0 |  |  |  |
| immediate_sync_ready | bit | 1 | 0 |  |  |  |
| allow_queued_tran | bit | 1 | 0 |  |  |  |
| allow_sync_tran | bit | 1 | 0 |  |  |  |
| autogen_sync_procs | bit | 1 | 0 |  |  |  |
| snapshot_in_defaultfolder | bit | 1 | 0 |  |  |  |
| alt_snapshot_folder | nvarchar | 1020 | 1 |  |  |  |
| pre_snapshot_script | nvarchar | 1020 | 1 |  |  |  |
| post_snapshot_script | nvarchar | 1020 | 1 |  |  |  |
| compress_snapshot | bit | 1 | 0 |  |  |  |
| ftp_address | sysname | 256 | 1 |  |  |  |
| ftp_port | int | 4 | 0 |  |  |  |
| ftp_subdirectory | nvarchar | 1020 | 1 |  |  |  |
| ftp_login | nvarchar | 512 | 1 |  |  |  |
| ftp_password | nvarchar | 2096 | 1 |  |  |  |
| allow_dts | bit | 1 | 0 |  |  |  |
| allow_anonymous | bit | 1 | 0 |  |  |  |
| centralized_conflicts | bit | 1 | 1 |  |  |  |
| conflict_retention | int | 4 | 1 |  |  |  |
| conflict_policy | int | 4 | 1 |  |  |  |
| queue_type | int | 4 | 1 |  |  |  |
| ad_guidname | sysname | 256 | 1 |  |  |  |
| backward_comp_level | int | 4 | 0 |  |  |  |
| description | nvarchar | 510 | 1 |  |  |  |
| independent_agent | bit | 1 | 0 |  |  |  |
| immediate_sync | bit | 1 | 0 |  |  |  |
| allow_push | bit | 1 | 0 |  |  |  |
| allow_pull | bit | 1 | 0 |  |  |  |
| retention | int | 4 | 1 |  |  |  |
| allow_subscription_copy | bit | 1 | 0 |  |  |  |
| allow_initialize_from_backup | bit | 1 | 0 |  |  |  |
| min_autonosync_lsn | binary | 1 | 1 |  |  |  |
| replicate_ddl | int | 4 | 1 |  |  |  |
| options | int | 4 | 1 |  |  |  |
| originator_id | int | 4 | 1 |  |  |  |
