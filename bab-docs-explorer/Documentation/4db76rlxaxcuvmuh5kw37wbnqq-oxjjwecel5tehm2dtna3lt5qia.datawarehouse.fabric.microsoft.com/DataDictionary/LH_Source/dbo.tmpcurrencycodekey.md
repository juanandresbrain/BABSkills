# dbo.tmpcurrencycodekey

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| From_Currency_key | int | 4 | 1 |  |  |  |
| To_Currency_key | int | 4 | 1 |  |  |  |
| Actual_Date | datetime2 | 8 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| MonthEndRate | decimal | 9 | 1 |  |  |  |
| DailyRate | decimal | 9 | 1 |  |  |  |
| AverageRate | decimal | 9 | 1 |  |  |  |
| FromCurrency | varchar | 8000 | 1 |  |  |  |
| ToCurrency | varchar | 8000 | 1 |  |  |  |
