# dbo.MSrepl_identity_range

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| publisher | sysname | 256 | 0 |  |  |  |
| publisher_db | sysname | 256 | 0 |  |  |  |
| tablename | sysname | 256 | 0 |  |  |  |
| identity_support | int | 4 | 1 |  |  |  |
| next_seed | bigint | 8 | 1 |  |  |  |
| pub_range | bigint | 8 | 1 |  |  |  |
| range | bigint | 8 | 1 |  |  |  |
| max_identity | bigint | 8 | 1 |  |  |  |
| threshold | int | 4 | 1 |  |  |  |
| current_max | bigint | 8 | 1 |  |  |  |
