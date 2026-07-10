# dbo.DynamicsSalesTransactionExceptions

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RetailTransactionId | varchar | 44 | 1 |  |  |  |
| Reason | varchar | 50 | 1 |  |  |  |
| ItemId | varchar | 50 | 1 |  |  |  |
| Price | numeric | 9 | 1 |  |  |  |
| LineObject | int | 4 | 1 |  |  |  |
| LineObjectDescription | varchar | 50 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| IsCurrent | varchar | 2 | 1 |  |  |  |
| RetailReceiptId | varchar | 18 | 1 |  |  |  |
| VarianceValue | numeric | 9 | 1 |  |  |  |
