# dbo.flashgaapsalesstage

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_key | int | 4 | 1 |  |  |  |
| local_date_key | int | 4 | 1 |  |  |  |
| local_time_key | int | 4 | 1 |  |  |  |
| local_hour | int | 4 | 1 |  |  |  |
| flash_gaap_sales | decimal | 17 | 1 |  |  |  |
| source | varchar | 8000 | 1 |  |  |  |
| Jurisdiction | varchar | 8000 | 1 |  |  |  |
| TransactionCount | int | 4 | 1 |  |  |  |
| insert_datetime | datetime2 | 8 | 1 |  |  |  |
| ETLLogID | int | 4 | 1 |  |  |  |
| CurrencyCode | varchar | 8000 | 1 |  |  |  |
| TradingGroup | varchar | 8000 | 1 |  |  |  |
| NetUnits | int | 4 | 1 |  |  |  |
