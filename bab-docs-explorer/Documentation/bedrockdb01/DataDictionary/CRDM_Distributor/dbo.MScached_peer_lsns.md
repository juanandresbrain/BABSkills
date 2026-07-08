# dbo.MScached_peer_lsns

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| agent_id | int | 4 | 1 |  |  |  |
| originator | sysname | 256 | 0 |  |  |  |
| originator_db | sysname | 256 | 0 |  |  |  |
| originator_publication_id | int | 4 | 1 |  |  |  |
| originator_db_version | int | 4 | 1 |  |  |  |
| originator_lsn | varbinary | 16 | 1 |  |  |  |
