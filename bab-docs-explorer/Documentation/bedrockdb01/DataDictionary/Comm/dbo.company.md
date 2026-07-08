# dbo.company

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| comp_id | smallint | 2 | 0 |  |  |  |
| comp_name | nvarchar | 100 | 0 |  |  |  |
| comp_description | nvarchar | 510 | 1 |  |  |  |
| version_id | int | 4 | 0 |  |  |  |
| acquiring_id | nvarchar | 24 | 1 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
| row_id | int | 4 | 0 | YES |  |  |
