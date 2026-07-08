# dbo.dw_store_master

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| instance_id | smallint | 2 | 0 |  |  |  |
| source_media_rec_recovery_id | smallint | 2 | 1 |  |  |  |
| trans_exist | tinyint | 1 | 1 |  |  |  |
| scaleout_move_requested | datetime | 8 | 1 |  |  |  |
| scaleout_move_request_instance | smallint | 2 | 1 |  |  |  |
