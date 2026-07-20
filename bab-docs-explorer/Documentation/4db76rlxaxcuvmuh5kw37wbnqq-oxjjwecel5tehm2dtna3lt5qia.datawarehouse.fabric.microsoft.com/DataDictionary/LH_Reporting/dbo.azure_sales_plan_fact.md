# dbo.azure_sales_plan_fact

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreKey | varchar | 8000 | 1 |  |  |  |
| CalendarDate | datetime2 | 8 | 1 |  |  |  |
| CurrencyCode | varchar | 8000 | 1 |  |  |  |
| NativeSalesPlan | decimal | 13 | 1 |  |  |  |
| CurrencyCodeFiscalMonth | varchar | 8000 | 1 |  |  |  |
| ExchangeRate | decimal | 9 | 1 |  |  |  |
| SalesPlan | decimal | 17 | 1 |  |  |  |
