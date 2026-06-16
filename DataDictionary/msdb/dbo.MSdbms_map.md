# dbo.MSdbms_map

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| map_id | int | 4 | 0 | YES |  |  |
| src_dbms_id | int | 4 | 0 |  | YES |  |
| dest_dbms_id | int | 4 | 0 |  | YES |  |
| src_datatype_id | int | 4 | 0 |  | YES |  |
| src_len_min | bigint | 8 | 1 |  |  |  |
| src_len_max | bigint | 8 | 1 |  |  |  |
| src_prec_min | bigint | 8 | 1 |  |  |  |
| src_prec_max | bigint | 8 | 1 |  |  |  |
| src_scale_min | bigint | 8 | 1 |  |  |  |
| src_scale_max | bigint | 8 | 1 |  |  |  |
| src_nullable | bit | 1 | 1 |  |  |  |
| default_datatype_mapping_id | int | 4 | 1 |  | YES |  |

