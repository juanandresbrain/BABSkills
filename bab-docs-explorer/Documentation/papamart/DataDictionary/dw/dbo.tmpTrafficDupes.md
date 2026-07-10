# dbo.tmpTrafficDupes

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ActDate | date | 3 | 1 |  |  |  |
| store_id | int | 4 | 1 |  |  |  |
| tm_key | int | 4 | 1 |  |  |  |
| MinKey | int | 4 | 1 |  |  |  |
| MaxKey | int | 4 | 1 |  |  |  |
| MinExits | int | 4 | 1 |  |  |  |
| MaxExits | int | 4 | 1 |  |  |  |
| MinInsDate | datetime | 8 | 1 |  |  |  |
| MaxInsDate | datetime | 8 | 1 |  |  |  |
| Entries | int | 4 | 1 |  |  |  |
