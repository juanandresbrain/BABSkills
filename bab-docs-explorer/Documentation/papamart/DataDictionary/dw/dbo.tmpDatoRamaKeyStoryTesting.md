# dbo.tmpDatoRamaKeyStoryTesting

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionDate | date | 3 | 1 |  |  |  |
| KeyStoryCode | nvarchar | 100 | 1 |  |  |  |
| Channel | varchar | 5 | 1 |  |  |  |
| KeyStorySales | numeric | 17 | 1 |  |  |  |
| KeyStoryUnitSales | int | 4 | 1 |  |  |  |
| KeyStoryTransactionCount | int | 4 | 1 |  |  |  |
| TransactionCount | int | 4 | 1 |  |  |  |
| KeyStoryBcSales | numeric | 17 | 1 |  |  |  |
| KeyStoryBcUnitSales | int | 4 | 1 |  |  |  |
| KeyStoryBcTransactionCount | int | 4 | 1 |  |  |  |
| FulfillmentCountry | varchar | 50 | 1 |  |  |  |
