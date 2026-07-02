# dbo.MSdbms_datatype_mapping

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| datatype_mapping_id | int | 4 | 0 | YES |  |  |
| map_id | int | 4 | 0 |  | YES |  |
| dest_datatype_id | int | 4 | 0 |  | YES |  |
| dest_precision | bigint | 8 | 1 |  |  |  |
| dest_scale | int | 4 | 1 |  |  |  |
| dest_length | bigint | 8 | 1 |  |  |  |
| dest_nullable | bit | 1 | 1 |  |  |  |
| dest_createparams | int | 4 | 0 |  |  |  |
| dataloss | bit | 1 | 0 |  |  |  |

