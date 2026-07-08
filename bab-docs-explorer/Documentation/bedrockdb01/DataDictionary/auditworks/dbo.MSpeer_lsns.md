# dbo.MSpeer_lsns

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 | YES |  |  |
| last_updated | datetime | 8 | 1 |  |  |  |
| originator | sysname | 256 | 0 |  |  |  |
| originator_db | sysname | 256 | 0 |  |  |  |
| originator_publication | sysname | 256 | 0 |  |  |  |
| originator_publication_id | int | 4 | 1 |  |  |  |
| originator_db_version | int | 4 | 1 |  |  |  |
| originator_lsn | varbinary | 16 | 1 |  |  |  |
| originator_version | int | 4 | 1 |  |  |  |
| originator_id | int | 4 | 1 |  |  |  |
