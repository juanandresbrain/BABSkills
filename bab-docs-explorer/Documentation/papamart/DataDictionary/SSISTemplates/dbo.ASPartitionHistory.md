# dbo.ASPartitionHistory

**Database:** SSISTemplates  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| histID | int | 4 | 0 | YES |  | Surrogate Key |
| partID | int | 4 | 0 |  |  | FK to ASPartition |
| refreshDateTime | datetime | 8 | 0 |  |  |  |
| numSeconds | int | 4 | 0 |  |  |  |
