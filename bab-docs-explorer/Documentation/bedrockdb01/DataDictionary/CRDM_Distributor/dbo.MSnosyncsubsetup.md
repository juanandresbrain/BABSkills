# dbo.MSnosyncsubsetup

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| publisher_database_id | int | 4 | 0 |  |  |  |
| publication_id | int | 4 | 0 |  |  |  |
| artid | int | 4 | 0 |  |  |  |
| next_valid_lsn | varbinary | 10 | 0 |  |  |  |
| parameterName | sysname | 256 | 0 |  |  |  |
| parameterValue | nvarchar | -1 | 1 |  |  |  |
