# dbo.fgsnotinty

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreKey | varchar | 8000 | 1 |  |  |  |
| StoreName | varchar | 8000 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| BusinessDate | date | 3 | 1 |  |  |  |
| LYSalesDayTotalLocal | decimal | 17 | 1 |  |  |  |
| LYSalesDayTotalUSD | decimal | 17 | 1 |  |  |  |
| CompLYSalesDayTotalLocal | decimal | 17 | 1 |  |  |  |
| CompLYSalesDayTotalUSD | decimal | 17 | 1 |  |  |  |
| LYDayTotalTrans | int | 4 | 1 |  |  |  |
| DaySalesPlan | decimal | 9 | 1 |  |  |  |
| CompStatus | int | 4 | 1 |  |  |  |
| CurrencyCode | varchar | 8000 | 1 |  |  |  |
| TradingGroup | varchar | 8000 | 1 |  |  |  |
| Jurisdiction | varchar | 8000 | 1 |  |  |  |
