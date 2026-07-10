# dbo.FranchiseeTransactionHeader

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FranchiseeTransactionHeaderID | int | 4 | 0 | YES |  |  |
| Franchisee | varchar | 2 | 0 |  |  |  |
| TransactionID | varchar | 20 | 0 |  |  |  |
| TransactionDateTime | datetime | 8 | 0 |  |  |  |
| StoreID | varchar | 10 | 1 |  |  |  |
| InsertDate | datetime | 8 | 0 |  |  |  |
| BatchID | varchar | 52 | 0 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| time_key | int | 4 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
