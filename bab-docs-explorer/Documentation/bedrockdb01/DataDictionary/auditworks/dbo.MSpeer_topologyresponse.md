# dbo.MSpeer_topologyresponse

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| request_id | int | 4 | 1 |  |  |  |
| peer | sysname | 256 | 0 |  |  |  |
| peer_version | int | 4 | 1 |  |  |  |
| peer_db | sysname | 256 | 0 |  |  |  |
| originator_id | int | 4 | 1 |  |  |  |
| peer_conflict_retention | int | 4 | 1 |  |  |  |
| received_date | datetime | 8 | 1 |  |  |  |
| connection_info | xml | -1 | 1 |  |  |  |
