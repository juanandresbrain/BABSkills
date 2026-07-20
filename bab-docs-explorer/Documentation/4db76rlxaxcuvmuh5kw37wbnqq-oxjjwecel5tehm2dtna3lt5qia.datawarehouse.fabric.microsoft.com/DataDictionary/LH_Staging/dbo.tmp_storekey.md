# dbo.tmp_storekey

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreID | int | 4 | 1 |  |  |  |
| Year | int | 4 | 1 |  |  |  |
| Week | int | 4 | 1 |  |  |  |
| StartDate | datetime2 | 8 | 1 |  |  |  |
| EndDate | datetime2 | 8 | 1 |  |  |  |
| dpc | decimal | 9 | 1 |  |  |  |
| law | decimal | 9 | 1 |  |  |  |
| hoo | decimal | 9 | 1 |  |  |  |
| eqv | decimal | 9 | 1 |  |  |  |
| spp | decimal | 9 | 1 |  |  |  |
| msc | decimal | 9 | 1 |  |  |  |
| ffh | bit | 1 | 1 |  |  |  |
| StoreSales | int | 4 | 1 |  |  |  |
| StoreSalez | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| country | varchar | 8000 | 1 |  |  |  |
| Week_ID | int | 4 | 1 |  |  |  |
| Date_Key | int | 4 | 1 |  |  |  |
| Period_ID | int | 4 | 1 |  |  |  |
| AdjustedSales | int | 4 | 1 |  |  |  |
| AdjustedSalesRounded | decimal | 17 | 1 |  |  |  |
| BaseHours | decimal | 9 | 1 |  |  |  |
| LaborCredit | decimal | 9 | 1 |  |  |  |
| dpc_derived | decimal | 9 | 1 |  |  |  |
| EarnedHours | decimal | 17 | 1 |  |  |  |
| EarnedHourz | decimal | 17 | 1 |  |  |  |
| ActualHours | decimal | 9 | 1 |  |  |  |
| ActualHourz | decimal | 9 | 1 |  |  |  |
| Variance | decimal | 17 | 1 |  |  |  |
| PercentOfActual | decimal | 17 | 1 |  |  |  |
