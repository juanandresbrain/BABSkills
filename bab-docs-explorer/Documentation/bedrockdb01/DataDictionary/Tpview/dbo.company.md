# dbo.company

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| comp_id | smallint | 2 | 0 |  |  |  |
| comp_name | varchar | 50 | 0 |  |  |  |
| comp_description | varchar | 255 | 1 |  |  |  |
| version_id | int | 4 | 0 |  |  |  |
| acquiring_id | varchar | 12 | 1 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
| row_id | int | 4 | 0 | YES |  |  |
