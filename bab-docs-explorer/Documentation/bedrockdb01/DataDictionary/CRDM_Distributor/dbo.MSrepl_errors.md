# dbo.MSrepl_errors

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 |  |  |  |
| time | datetime | 8 | 0 |  |  |  |
| error_type_id | int | 4 | 1 |  |  |  |
| source_type_id | int | 4 | 1 |  |  |  |
| source_name | nvarchar | 200 | 1 |  |  |  |
| error_code | sysname | 256 | 1 |  |  |  |
| error_text | ntext | 16 | 1 |  |  |  |
| xact_seqno | varbinary | 16 | 1 |  |  |  |
| command_id | int | 4 | 1 |  |  |  |
| session_id | int | 4 | 1 |  |  |  |
