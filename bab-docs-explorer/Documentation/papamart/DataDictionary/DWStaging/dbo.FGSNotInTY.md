# dbo.FGSNotInTY

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreKey | varchar | 4 | 1 |  |  |  |
| StoreName | varchar | 100 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| BusinessDate | date | 3 | 1 |  |  |  |
| LYSalesDayTotalLocal | decimal | 17 | 1 |  |  |  |
| LYSalesDayTotalUSD | decimal | 17 | 1 |  |  |  |
| CompLYSalesDayTotalLocal | decimal | 17 | 1 |  |  |  |
| CompLYSalesDayTotalUSD | decimal | 17 | 1 |  |  |  |
| LYDayTotalTrans | int | 4 | 1 |  |  |  |
| DaySalesPlan | money | 8 | 0 |  |  |  |
| CompStatus | int | 4 | 1 |  |  |  |
| CurrencyCode | varchar | 52 | 1 |  |  |  |
| TradingGroup | varchar | 52 | 1 |  |  |  |
| Jurisdiction | varchar | 52 | 1 |  |  |  |
