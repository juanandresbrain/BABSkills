# dbo.flashsummary_sqlsynccopy

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreKey | varchar | 8000 | 1 |  |  |  |
| FiscalYear | int | 4 | 1 |  |  |  |
| FiscalMonth | int | 4 | 1 |  |  |  |
| BusinessDate | date | 3 | 1 |  |  |  |
| StoreID | int | 4 | 1 |  |  |  |
| StoreName | varchar | 8000 | 1 |  |  |  |
| BusinessHour | int | 4 | 1 |  |  |  |
| TYGaapByHourNative | decimal | 17 | 1 |  |  |  |
| TYGaapByHourUSD | decimal | 17 | 1 |  |  |  |
| TYGaapByHourRunningTotalNative | decimal | 17 | 1 |  |  |  |
| TYGaapByHourRunningTotalUSD | decimal | 17 | 1 |  |  |  |
| TYDayTotalSalesNative | decimal | 17 | 1 |  |  |  |
| TYDayTotalSalesUSD | decimal | 17 | 1 |  |  |  |
| LYGaapByHourNative | decimal | 17 | 1 |  |  |  |
| LYGaapByHourUSD | decimal | 17 | 1 |  |  |  |
| LYGaapByHourRunningTotalNative | decimal | 17 | 1 |  |  |  |
| LYGaapByHourRunningTotalUSD | decimal | 17 | 1 |  |  |  |
| LYDayTotalSalesNative | decimal | 17 | 1 |  |  |  |
| LYDayTotalSalesUSD | decimal | 17 | 1 |  |  |  |
| TYTransCountByHour | int | 4 | 1 |  |  |  |
| TYDayTotalTrans | int | 4 | 1 |  |  |  |
| TYTransCountRunningTotal | int | 4 | 1 |  |  |  |
| TYNetUnitsByHour | int | 4 | 1 |  |  |  |
| TYDayTotalUnits | int | 4 | 1 |  |  |  |
| TYNetUnitsRunningTotal | int | 4 | 1 |  |  |  |
| CompStatus | int | 4 | 1 |  |  |  |
| Jurisdiction | varchar | 8000 | 1 |  |  |  |
| TradingGroup | varchar | 8000 | 1 |  |  |  |
| DaySalesPlan | decimal | 9 | 1 |  |  |  |
| CurrentStoreTime | datetime2 | 8 | 1 |  |  |  |
| CurrentHour | int | 4 | 1 |  |  |  |
