# dbo.exchange_rate_facts

**Database:** LH_Mart_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| exchange_rate_facts_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| from_currency_key | int | 4 | 1 |  |  |  |
| to_currency_key | int | 4 | 1 |  |  |  |
| actual_date | datetime2 | 8 | 1 |  |  |  |
| from_currency_code | varchar | 8000 | 1 |  |  |  |
| to_currency_code | varchar | 8000 | 1 |  |  |  |
| bbw_rate | decimal | 9 | 1 |  |  |  |
| actual_rate | decimal | 9 | 1 |  |  |  |
| fiscal_month_ave_rate | decimal | 9 | 1 |  |  |  |
| fiscal_month_end_rate | decimal | 9 | 1 |  |  |  |
| calendar_month_ave_rate | decimal | 9 | 1 |  |  |  |
| calendar_month_end_rate | decimal | 9 | 1 |  |  |  |
