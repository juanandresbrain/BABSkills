# dbo.tmpaddrates

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Actual_Date | datetime2 | 8 | 1 |  |  |  |
| FromCurrency | varchar | 8000 | 1 |  |  |  |
| ToCurrency | varchar | 8000 | 1 |  |  |  |
| MonthEndRate | decimal | 9 | 1 |  |  |  |
| DailyRate | decimal | 9 | 1 |  |  |  |
| AverageRate | decimal | 9 | 1 |  |  |  |
