# dbo.table_sizes

**Database:** DBAUtility  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| dbname | varchar | 250 | 1 |  |  |  |
| tablename | varchar | 250 | 1 |  |  |  |
| crdate | datetime | 8 | 1 |  |  |  |
| rows | int | 4 | 1 |  |  |  |
| KBreserved | decimal | 9 | 1 |  |  |  |
| KBdata | decimal | 9 | 1 |  |  |  |
| KBindex_size | decimal | 9 | 1 |  |  |  |
| KBunused | decimal | 9 | 1 |  |  |  |
