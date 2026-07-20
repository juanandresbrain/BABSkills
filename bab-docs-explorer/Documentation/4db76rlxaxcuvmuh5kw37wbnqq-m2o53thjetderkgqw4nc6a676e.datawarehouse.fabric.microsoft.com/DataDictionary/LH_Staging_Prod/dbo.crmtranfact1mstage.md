# dbo.crmtranfact1mstage

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

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
