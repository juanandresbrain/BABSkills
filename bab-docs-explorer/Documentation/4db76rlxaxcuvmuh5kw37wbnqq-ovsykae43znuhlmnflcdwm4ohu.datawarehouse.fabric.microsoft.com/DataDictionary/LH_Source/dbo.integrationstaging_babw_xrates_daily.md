# dbo.integrationstaging_babw_xrates_daily

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| rateDescription | varchar | 8000 | 1 |  |  |  |
| fromCurrency | varchar | 8000 | 1 |  |  |  |
| toCurrency | varchar | 8000 | 1 |  |  |  |
| startDate | datetime2 | 8 | 1 |  |  |  |
| endDate | datetime2 | 8 | 1 |  |  |  |
| rate | decimal | 5 | 1 |  |  |  |
