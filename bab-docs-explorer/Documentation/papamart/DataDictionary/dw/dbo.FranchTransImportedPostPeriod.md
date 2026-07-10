# dbo.FranchTransImportedPostPeriod

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Franchisee | varchar | 2 | 1 |  |  |  |
| TransactionID | varchar | 20 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| ImportDate | date | 3 | 1 |  |  |  |
| PreviousPeriodCutOffDate | date | 3 | 1 |  |  |  |
| TransactionPayment | numeric | 17 | 1 |  |  |  |
| GrossSales | numeric | 17 | 1 |  |  |  |
| GiftCardAmount | numeric | 17 | 1 |  |  |  |
| OriginalGrossSales | numeric | 17 | 1 |  |  |  |
| OriginalGiftCardAmount | numeric | 17 | 1 |  |  |  |
| OriginalInsertDate | date | 3 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| StoreID | varchar | 10 | 1 |  |  |  |
