# dbo.LoyaltyTransactionFactStage

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | int | 4 | 0 |  |  |  |
| StoreKey | int | 4 | 0 |  |  |  |
| DateKey | int | 4 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| LoyaltyTransactionType | varchar | 6 | 0 |  |  |  |
| POSTransactionNumber | int | 4 | 1 |  |  |  |
| POSRegisterNumber | int | 4 | 1 |  |  |  |
| CustomerNumber | varchar | 20 | 1 |  |  |  |
| GaapSales | decimal | 17 | 1 |  |  |  |
| GaapUnits | decimal | 17 | 1 |  |  |  |
| matchedByEmail | int | 4 | 0 |  |  |  |
