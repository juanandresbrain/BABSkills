# dbo.sysdiagrams

**Database:** SSISTemplates  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| name | sysname | 256 | 0 |  |  |  |
| principal_id | int | 4 | 0 |  |  |  |
| diagram_id | int | 4 | 0 | YES |  |  |
| version | int | 4 | 1 |  |  |  |
| definition | varbinary | -1 | 1 |  |  |  |
