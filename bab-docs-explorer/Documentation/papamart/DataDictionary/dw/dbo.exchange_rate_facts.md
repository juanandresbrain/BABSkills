# dbo.exchange_rate_facts

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| exchange_rate_facts_key | int | 4 | 0 | YES |  |  |
| date_key | int | 4 | 0 |  |  |  |
| from_currency_key | int | 4 | 0 |  |  |  |
| to_currency_key | int | 4 | 0 |  |  |  |
| actual_date | datetime | 8 | 1 |  |  |  |
| from_currency_code | varchar | 3 | 1 |  |  |  |
| to_currency_code | varchar | 3 | 1 |  |  |  |
| bbw_rate | decimal | 9 | 1 |  |  |  |
| actual_rate | decimal | 9 | 1 |  |  |  |
| fiscal_month_ave_rate | decimal | 9 | 1 |  |  |  |
| fiscal_month_end_rate | decimal | 9 | 1 |  |  |  |
| calendar_month_ave_rate | decimal | 9 | 1 |  |  |  |
| calendar_month_end_rate | decimal | 9 | 1 |  |  |  |
