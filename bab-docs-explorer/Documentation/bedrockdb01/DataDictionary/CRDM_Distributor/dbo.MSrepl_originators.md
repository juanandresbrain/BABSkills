# dbo.MSrepl_originators

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 | YES |  |  |
| publisher_database_id | int | 4 | 0 |  |  |  |
| srvname | sysname | 256 | 0 |  |  |  |
| dbname | sysname | 256 | 0 |  |  |  |
| publication_id | int | 4 | 1 |  |  |  |
| dbversion | int | 4 | 1 |  |  |  |
