# dbo.fgsummary

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreID | int | 4 | 1 |  |  |  |
| StoreName | varchar | 8000 | 1 |  |  |  |
| FiscalYear | int | 4 | 1 |  |  |  |
| FiscalMonth | int | 4 | 1 |  |  |  |
| BusinessDate | date | 3 | 1 |  |  |  |
| BusinessHour | int | 4 | 1 |  |  |  |
| TYGaapByHourNative | decimal | 17 | 1 |  |  |  |
| TYGaapByHourUSD | decimal | 17 | 1 |  |  |  |
| TYGaapByHourRunningTotalNative | decimal | 17 | 1 |  |  |  |
| TYGaapByHourRunningTotalUSD | decimal | 17 | 1 |  |  |  |
| TYTransCountByHour | int | 4 | 1 |  |  |  |
| TYTransCountByHourRunningTotal | int | 4 | 1 |  |  |  |
| TYDayTotalSalesNative | decimal | 17 | 1 |  |  |  |
| TYDayTotalSalesUSD | decimal | 17 | 1 |  |  |  |
| TYDayTotalTrans | int | 4 | 1 |  |  |  |
| CurrencyCode | varchar | 8000 | 1 |  |  |  |
| CompStatus | int | 4 | 1 |  |  |  |
| Jurisdiction | varchar | 8000 | 1 |  |  |  |
| TradingGroup | varchar | 8000 | 1 |  |  |  |
| DaySalesPlan | decimal | 9 | 1 |  |  |  |
| LYGaapByHourNative | decimal | 17 | 1 |  |  |  |
| LYGaapByHourUSD | decimal | 17 | 1 |  |  |  |
| LYGaapByHourRunningTotalNative | decimal | 17 | 1 |  |  |  |
| LYGaapByHourRunningTotalUSD | decimal | 17 | 1 |  |  |  |
| LYTransCountByHour | int | 4 | 1 |  |  |  |
| LYTransCountByHourRunningTotal | int | 4 | 1 |  |  |  |
| LYDayTotalSalesNative | decimal | 17 | 1 |  |  |  |
| LYDayTotalSalesUSD | decimal | 17 | 1 |  |  |  |
| LYDayTotalTrans | int | 4 | 1 |  |  |  |
| SalesPercentToLYRunningTotal | decimal | 17 | 1 |  |  |  |
| SalesPercentToLYDayTotal | decimal | 17 | 1 |  |  |  |
