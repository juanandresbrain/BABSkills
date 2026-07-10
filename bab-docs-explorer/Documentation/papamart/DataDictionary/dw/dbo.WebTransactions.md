# dbo.WebTransactions

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | int | 4 | 1 |  |  |  |
| TransactionNum | varchar | 22 | 1 |  |  |  |
| TransactionDateTime | datetime | 8 | 1 |  |  |  |
| TaxAmount | money | 8 | 1 |  |  |  |
| TaxJurisdiction | varchar | 50 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
