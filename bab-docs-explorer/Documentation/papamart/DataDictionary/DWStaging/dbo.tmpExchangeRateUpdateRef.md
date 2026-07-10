# dbo.tmpExchangeRateUpdateRef

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PREVasOfDate_key | int | 4 | 1 |  |  |  |
| THISasOfDate_key | int | 4 | 1 |  |  |  |
| frmCurrency_key | int | 4 | 1 |  |  |  |
| toCurrency_key | int | 4 | 1 |  |  |  |
| bbw_rate | decimal | 9 | 1 |  |  |  |
