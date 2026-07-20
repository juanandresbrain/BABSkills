# dbo.flashgaapemailstage

**Database:** LH_Staging_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BusinessDate | date | 3 | 1 |  |  |  |
| StoreKey | varchar | 8000 | 1 |  |  |  |
| StoreName | varchar | 8000 | 1 |  |  |  |
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
| DaySalesPlan | decimal | 9 | 1 |  |  |  |
| Jurisdiction | varchar | 8000 | 1 |  |  |  |
| TradingGroup | varchar | 8000 | 1 |  |  |  |
| SortOrder | int | 4 | 1 |  |  |  |
