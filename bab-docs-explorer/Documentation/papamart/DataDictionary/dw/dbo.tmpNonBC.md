# dbo.tmpNonBC

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| country | varchar | 50 | 1 |  |  |  |
| PurchaseChannel | nvarchar | 40 | 1 |  |  |  |
| transaction_ID | int | 4 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| KeyStory | nvarchar | 60 | 1 |  |  |  |
| GaapUnits | int | 4 | 1 |  |  |  |
| GaapSales | numeric | 17 | 1 |  |  |  |
| isWeb | int | 4 | 1 |  |  |  |
| isRetail | int | 4 | 1 |  |  |  |
| 2ndPurchase | nvarchar | 60 | 1 |  |  |  |
| 3rdPurchase | nvarchar | 60 | 1 |  |  |  |
| 4thPurchase | nvarchar | 60 | 1 |  |  |  |
