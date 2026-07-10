# dbo.FlashGaapSalesStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_key | int | 4 | 0 |  |  |  |
| local_date_key | int | 4 | 0 |  |  |  |
| local_time_key | int | 4 | 0 |  |  |  |
| local_hour | int | 4 | 0 |  |  |  |
| flash_gaap_sales | decimal | 17 | 0 |  |  |  |
| source | varchar | 20 | 0 |  |  |  |
| Jurisdiction | varchar | 20 | 0 |  |  |  |
| TransactionCount | int | 4 | 0 |  |  |  |
| insert_datetime | datetime | 8 | 0 |  |  |  |
| ETLLogID | int | 4 | 0 |  |  |  |
| CurrencyCode | char | 3 | 1 |  |  |  |
| TradingGroup | varchar | 15 | 1 |  |  |  |
| NetUnits | int | 4 | 1 |  |  |  |
