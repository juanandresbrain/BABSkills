# dbo.TmpOrdersTie

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RetailTransactionId | varchar | 44 | 1 |  |  |  |
| RetailReceiptId | varchar | 18 | 1 |  |  |  |
| TransDate | date | 3 | 1 |  |  |  |
| Entity | varchar | 10 | 1 |  |  |  |
| GrossAmount | decimal | 9 | 1 |  |  |  |
| PaymentTotal | decimal | 9 | 1 |  |  |  |
| Variance | decimal | 9 | 1 |  |  |  |
