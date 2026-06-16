# WMstg.UKstgTransactions

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | int | 4 | 1 |  |  |  |
| TransactionNum | varchar | 22 | 0 |  |  |  |
| ClientID | varchar | 64 | 0 |  |  |  |
| TransactionDateTime | datetime | 8 | 0 |  |  |  |
| TaxAmount | money | 8 | 1 |  |  |  |
| TaxJurisdiction | varchar | 50 | 1 |  |  |  |
| TaxAuthority | varchar | 50 | 1 |  |  |  |
| TaxType | int | 4 | 1 |  |  |  |
| tmpTransID | int | 4 | 1 |  |  |  |

