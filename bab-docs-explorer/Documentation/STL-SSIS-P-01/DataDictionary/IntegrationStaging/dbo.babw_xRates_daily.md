# dbo.babw_xRates_daily

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| rateDescription | nvarchar | 510 | 1 |  |  |  |
| fromCurrency | nvarchar | 100 | 1 |  |  |  |
| toCurrency | nvarchar | 100 | 1 |  |  |  |
| startDate | datetime | 8 | 1 |  |  |  |
| endDate | datetime | 8 | 1 |  |  |  |
| rate | decimal | 5 | 1 |  |  |  |

