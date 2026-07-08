# dbo.sysschemaarticles

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| artid | int | 4 | 0 |  |  |  |
| creation_script | nvarchar | 510 | 1 |  |  |  |
| description | nvarchar | 510 | 1 |  |  |  |
| dest_object | sysname | 256 | 0 |  |  |  |
| name | sysname | 256 | 0 |  |  |  |
| objid | int | 4 | 0 |  |  |  |
| pubid | int | 4 | 0 |  |  |  |
| pre_creation_cmd | tinyint | 1 | 0 |  |  |  |
| status | int | 4 | 0 |  |  |  |
| type | tinyint | 1 | 0 |  |  |  |
| schema_option | binary | 8 | 1 |  |  |  |
| dest_owner | sysname | 256 | 1 |  |  |  |
