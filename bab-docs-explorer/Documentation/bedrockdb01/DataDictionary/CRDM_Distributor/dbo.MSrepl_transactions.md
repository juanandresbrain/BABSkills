# dbo.MSrepl_transactions

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| publisher_database_id | int | 4 | 0 |  |  |  |
| xact_id | varbinary | 16 | 1 |  |  |  |
| xact_seqno | varbinary | 16 | 0 |  |  |  |
| entry_time | datetime | 8 | 0 |  |  |  |
