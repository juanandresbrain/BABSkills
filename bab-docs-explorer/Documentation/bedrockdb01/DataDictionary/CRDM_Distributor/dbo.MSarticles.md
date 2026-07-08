# dbo.MSarticles

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| publisher_id | smallint | 2 | 0 |  |  |  |
| publisher_db | sysname | 256 | 1 |  |  |  |
| publication_id | int | 4 | 0 |  |  |  |
| article | sysname | 256 | 0 |  |  |  |
| article_id | int | 4 | 0 |  |  |  |
| destination_object | sysname | 256 | 1 |  |  |  |
| source_owner | sysname | 256 | 1 |  |  |  |
| source_object | sysname | 256 | 1 |  |  |  |
| description | nvarchar | 510 | 1 |  |  |  |
| destination_owner | sysname | 256 | 1 |  |  |  |
