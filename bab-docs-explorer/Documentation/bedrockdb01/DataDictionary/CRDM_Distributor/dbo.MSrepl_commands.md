# dbo.MSrepl_commands

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| publisher_database_id | int | 4 | 0 |  |  |  |
| xact_seqno | varbinary | 16 | 0 |  |  |  |
| type | int | 4 | 0 |  |  |  |
| article_id | int | 4 | 0 |  |  |  |
| originator_id | int | 4 | 0 |  |  |  |
| command_id | int | 4 | 0 |  |  |  |
| partial_command | bit | 1 | 0 |  |  |  |
| command | varbinary | 1024 | 1 |  |  |  |
| hashkey | int | 4 | 1 |  |  |  |
| originator_lsn | varbinary | 16 | 1 |  |  |  |
