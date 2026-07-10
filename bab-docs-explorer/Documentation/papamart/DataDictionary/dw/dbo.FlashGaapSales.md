# dbo.FlashGaapSales

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_key | int | 4 | 0 |  |  |  |
| local_date_key | int | 4 | 0 |  |  |  |
| local_time_key | int | 4 | 0 |  |  |  |
| business_date_key | int | 4 | 0 |  |  |  |
| flash_gaap_sales | decimal | 17 | 0 |  |  |  |
| TransactionCount | int | 4 | 0 |  |  |  |
| source | varchar | 20 | 0 |  |  |  |
| Jurisdiction | varchar | 20 | 0 |  |  |  |
| CurrencyCode | char | 3 | 0 |  |  |  |
| INS_DT | datetime | 8 | 0 |  |  |  |
| UPD_DT | datetime | 8 | 1 |  |  |  |
| ETLLogID | int | 4 | 0 |  |  |  |
| TradingGroup | varchar | 15 | 1 |  |  |  |
| NetUnits | int | 4 | 1 |  |  |  |
