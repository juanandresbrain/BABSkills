# dbo.crmtranfact24mstage

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CustomerNumber | varchar | 8000 | 1 |  |  |  |
| MonthRange | varchar | 8000 | 1 |  |  |  |
| TransactionCount | int | 4 | 1 |  |  |  |
| RecencyCount | int | 4 | 1 |  |  |  |
| SalesTotal | decimal | 17 | 1 |  |  |  |
| minDaysBetween | int | 4 | 1 |  |  |  |
| maxDaysBetween | int | 4 | 1 |  |  |  |
| DaysBetween | int | 4 | 1 |  |  |  |
