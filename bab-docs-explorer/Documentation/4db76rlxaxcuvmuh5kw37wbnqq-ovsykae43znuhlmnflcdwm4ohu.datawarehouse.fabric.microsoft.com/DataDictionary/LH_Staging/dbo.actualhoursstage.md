# dbo.actualhoursstage

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreID | int | 4 | 1 |  |  |  |
| Year | int | 4 | 1 |  |  |  |
| Week | int | 4 | 1 |  |  |  |
| WeekStartDate | date | 3 | 1 |  |  |  |
| ActualHours | decimal | 9 | 1 |  |  |  |
