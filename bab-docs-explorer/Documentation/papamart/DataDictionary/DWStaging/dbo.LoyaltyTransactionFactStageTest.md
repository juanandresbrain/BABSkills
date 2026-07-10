# dbo.LoyaltyTransactionFactStageTest

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | int | 4 | 0 |  |  |  |
| StoreKey | int | 4 | 1 |  |  |  |
| DateKey | int | 4 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| LoyaltyTransactionType | varchar | 6 | 1 |  |  |  |
| POSTransactionNumber | varchar | 20 | 1 |  |  |  |
| POSRegisterNumber | int | 4 | 1 |  |  |  |
| CustomerNumber | varchar | 20 | 0 |  |  |  |
| GaapSales | numeric | 17 | 1 |  |  |  |
| GaapUnits | int | 4 | 1 |  |  |  |
| matchedByEmail | bit | 1 | 1 |  |  |  |
