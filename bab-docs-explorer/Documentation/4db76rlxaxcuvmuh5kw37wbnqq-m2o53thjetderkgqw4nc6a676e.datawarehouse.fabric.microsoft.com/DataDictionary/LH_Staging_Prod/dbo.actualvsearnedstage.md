# dbo.actualvsearnedstage

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StartDate | date | 3 | 1 |  |  |  |
| EndDate | date | 3 | 1 |  |  |  |
| Year | int | 4 | 1 |  |  |  |
| Week | int | 4 | 1 |  |  |  |
| WeekID | int | 4 | 1 |  |  |  |
| PeriodID | int | 4 | 1 |  |  |  |
| StoreID | int | 4 | 1 |  |  |  |
| ActualHours | decimal | 17 | 1 |  |  |  |
| EarnedHours | decimal | 17 | 1 |  |  |  |
| Variance | decimal | 17 | 1 |  |  |  |
| PercentOfActual | decimal | 17 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| AdjustedSales | decimal | 17 | 1 |  |  |  |
| AdjustedSalesRounded | decimal | 17 | 1 |  |  |  |
| BaseHours | int | 4 | 1 |  |  |  |
