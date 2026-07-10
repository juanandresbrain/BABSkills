# dbo.FranchiseeTransactionDupes

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Franchisee | varchar | 2 | 1 |  |  |  |
| TransactionID | varchar | 100 | 1 |  |  |  |
| HeaderRecords | int | 4 | 1 |  |  |  |
| PaymentRecords | int | 4 | 1 |  |  |  |
| MerchandiseRecords | int | 4 | 1 |  |  |  |
| GiftCardRecords | int | 4 | 1 |  |  |  |
