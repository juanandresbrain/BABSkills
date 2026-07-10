# dbo.FlashGaapEmailStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BusinessDate | date | 3 | 1 |  |  |  |
| StoreKey | varchar | 4 | 1 |  |  |  |
| StoreName | varchar | 100 | 1 |  |  |  |
| FlashGaapSalesUSD | decimal | 17 | 1 |  |  |  |
| FlashGaapSalesLocal | decimal | 17 | 1 |  |  |  |
| CompFlashGaapSalesUSD | decimal | 17 | 1 |  |  |  |
| CompFlashGaapSalesLocal | decimal | 17 | 1 |  |  |  |
| LYGaapSalesDayTotalUSD | decimal | 17 | 1 |  |  |  |
| LYGaapSalesDayTotalLocal | decimal | 17 | 1 |  |  |  |
| CompLYGaapSalesDayTotalUSD | decimal | 17 | 1 |  |  |  |
| CompLYGaapSalesDayTotalLocal | decimal | 17 | 1 |  |  |  |
| LYSalesThisHourLocal | decimal | 17 | 1 |  |  |  |
| LYSalesThisHourUSD | decimal | 17 | 1 |  |  |  |
| CompLYSalesThisHourLocal | decimal | 17 | 1 |  |  |  |
| CompLYSalesThisHourUSD | decimal | 17 | 1 |  |  |  |
| DaySalesPlan | money | 8 | 0 |  |  |  |
| Jurisdiction | varchar | 52 | 1 |  |  |  |
| TradingGroup | varchar | 52 | 1 |  |  |  |
| SortOrder | int | 4 | 1 |  |  |  |
