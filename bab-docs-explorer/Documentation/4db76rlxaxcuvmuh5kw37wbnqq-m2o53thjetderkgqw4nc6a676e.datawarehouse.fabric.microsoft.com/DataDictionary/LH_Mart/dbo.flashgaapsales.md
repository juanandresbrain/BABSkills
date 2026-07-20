# dbo.flashgaapsales

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_key | int | 4 | 1 |  |  |  |
| local_date_key | int | 4 | 1 |  |  |  |
| local_time_key | int | 4 | 1 |  |  |  |
| business_date_key | int | 4 | 1 |  |  |  |
| flash_gaap_sales | decimal | 17 | 1 |  |  |  |
| TransactionCount | int | 4 | 1 |  |  |  |
| source | varchar | 8000 | 1 |  |  |  |
| Jurisdiction | varchar | 8000 | 1 |  |  |  |
| CurrencyCode | varchar | 8000 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
| UPD_DT | datetime2 | 8 | 1 |  |  |  |
| ETLLogID | int | 4 | 1 |  |  |  |
| TradingGroup | varchar | 8000 | 1 |  |  |  |
| NetUnits | int | 4 | 1 |  |  |  |
