# dbo.StagingExchangeRate

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ConversionFactor | varchar | 50 | 1 |  |  |  |
| EndDate | datetime | 8 | 1 |  |  |  |
| FromCurrency | varchar | 3 | 1 |  |  |  |
| Rate | decimal | 9 | 1 |  |  |  |
| RateTypeDescription | varchar | 100 | 1 |  |  |  |
| RateTypeName | varchar | 50 | 1 |  |  |  |
| StartDate | datetime | 8 | 1 |  |  |  |
| ToCurrency | varchar | 3 | 1 |  |  |  |
