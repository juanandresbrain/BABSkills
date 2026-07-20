# dbo.azure_currency_exchange_fact

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FiscalYear | int | 4 | 1 |  |  |  |
| FiscalMonth | int | 4 | 1 |  |  |  |
| FromCurrencyCode | varchar | 8000 | 1 |  |  |  |
| ToCurrencyCode | varchar | 8000 | 1 |  |  |  |
| ExchangeRate | decimal | 9 | 1 |  |  |  |
| Fiscal_Month_key | datetime2 | 8 | 1 |  |  |  |
| Currency_Fiscal_Month | varchar | 8000 | 1 |  |  |  |
