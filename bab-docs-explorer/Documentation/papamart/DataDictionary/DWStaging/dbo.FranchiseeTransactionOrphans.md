# dbo.FranchiseeTransactionOrphans

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Franchisee | varchar | 2 | 1 |  |  |  |
| TransactionID | varchar | 100 | 1 |  |  |  |
| HeaderRecords | varchar | 3 | 1 |  |  |  |
| PaymentRecords | varchar | 3 | 1 |  |  |  |
| MerchandiseRecords | varchar | 3 | 1 |  |  |  |
| GiftCardRecords | varchar | 3 | 1 |  |  |  |
| OrphanMessage | varchar | 50 | 1 |  |  |  |
| EmptyColumnsFound | varchar | 3 | 1 |  |  |  |
