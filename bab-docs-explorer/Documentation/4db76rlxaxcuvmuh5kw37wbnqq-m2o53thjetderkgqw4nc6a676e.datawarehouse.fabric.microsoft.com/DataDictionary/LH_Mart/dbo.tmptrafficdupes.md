# dbo.tmptrafficdupes

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

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
| MinInsDate | datetime2 | 8 | 1 |  |  |  |
| MaxInsDate | datetime2 | 8 | 1 |  |  |  |
| Entries | int | 4 | 1 |  |  |  |
