# dbo.MSpeer_conflictdetectionconfigresponse

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| request_id | int | 4 | 0 |  |  |  |
| peer_node | sysname | 256 | 0 |  |  |  |
| peer_db | sysname | 256 | 0 |  |  |  |
| peer_version | int | 4 | 1 |  |  |  |
| peer_db_version | int | 4 | 1 |  |  |  |
| is_peer | bit | 1 | 1 |  |  |  |
| conflictdetection_enabled | bit | 1 | 1 |  |  |  |
| originator_id | int | 4 | 1 |  |  |  |
| peer_conflict_retention | int | 4 | 1 |  |  |  |
| peer_continue_onconflict | bit | 1 | 1 |  |  |  |
| peer_subscriptions | xml | -1 | 1 |  |  |  |
| progress_phase | nvarchar | 64 | 0 |  |  |  |
| modified_date | datetime | 8 | 1 |  |  |  |
