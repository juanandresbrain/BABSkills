# dbo.FranchiseeTransactionGiftCardIMPORT

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | varchar | 20 | 1 |  |  |  |
| Units | int | 4 | 0 |  |  |  |
| GiftCardAmount | numeric | 5 | 0 |  |  |  |
| Discount | numeric | 5 | 0 |  |  |  |
| InsertDate | datetime | 8 | 0 |  |  |  |
| Franchisee | varchar | 2 | 1 |  |  |  |
