# dbo.MSmerge_sessions

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| session_id | int | 4 | 0 | YES |  |  |
| agent_id | int | 4 | 0 |  |  |  |
| start_time | datetime | 8 | 1 |  |  |  |
| end_time | datetime | 8 | 1 |  |  |  |
| duration | int | 4 | 1 |  |  |  |
| delivery_time | int | 4 | 0 |  |  |  |
| upload_time | int | 4 | 0 |  |  |  |
| download_time | int | 4 | 0 |  |  |  |
| schema_change_time | int | 4 | 0 |  |  |  |
| prepare_snapshot_time | int | 4 | 0 |  |  |  |
| delivery_rate | decimal | 9 | 0 |  |  |  |
| time_remaining | int | 4 | 0 |  |  |  |
| percent_complete | decimal | 5 | 0 |  |  |  |
| upload_inserts | int | 4 | 1 |  |  |  |
| upload_updates | int | 4 | 1 |  |  |  |
| upload_deletes | int | 4 | 1 |  |  |  |
| upload_conflicts | int | 4 | 1 |  |  |  |
| upload_rows_retried | int | 4 | 1 |  |  |  |
| download_inserts | int | 4 | 1 |  |  |  |
| download_updates | int | 4 | 1 |  |  |  |
| download_deletes | int | 4 | 1 |  |  |  |
| download_conflicts | int | 4 | 1 |  |  |  |
| download_rows_retried | int | 4 | 1 |  |  |  |
| schema_changes | int | 4 | 1 |  |  |  |
| bulk_inserts | int | 4 | 1 |  |  |  |
| metadata_rows_cleanedup | int | 4 | 1 |  |  |  |
| runstatus | int | 4 | 0 |  |  |  |
| estimated_upload_changes | int | 4 | 1 |  |  |  |
| estimated_download_changes | int | 4 | 1 |  |  |  |
| connection_type | int | 4 | 1 |  |  |  |
| timestamp | timestamp | 8 | 0 |  |  |  |
| current_phase_id | int | 4 | 1 |  |  |  |
| spid | smallint | 2 | 1 |  |  |  |
| spid_login_time | datetime | 8 | 1 |  |  |  |
