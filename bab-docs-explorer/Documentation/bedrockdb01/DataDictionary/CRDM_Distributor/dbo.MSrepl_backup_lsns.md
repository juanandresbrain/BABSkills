# dbo.MSrepl_backup_lsns

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| publisher_database_id | int | 4 | 0 |  |  |  |
| valid_xact_id | varbinary | 16 | 1 |  |  |  |
| valid_xact_seqno | varbinary | 16 | 1 |  |  |  |
| next_xact_id | varbinary | 16 | 1 |  |  |  |
| next_xact_seqno | varbinary | 16 | 1 |  |  |  |
