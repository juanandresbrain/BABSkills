# dbo.tmpDatoRamaKeyStoryStoreChannel

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionDate | date | 3 | 1 |  |  |  |
| KeyStoryCode | nvarchar | 60 | 1 |  |  |  |
| Channel | varchar | 5 | 0 |  |  |  |
| KeyStorySales | decimal | 17 | 0 |  |  |  |
| KeyStoryUnitSales | int | 4 | 0 |  |  |  |
| KeyStoryTransactionCount | int | 4 | 0 |  |  |  |
| TransactionCount | int | 4 | 0 |  |  |  |
| KeyStoryBcSales | decimal | 17 | 0 |  |  |  |
| KeyStoryBcUnitSales | int | 4 | 0 |  |  |  |
| KeyStoryBcTransactionCount | int | 4 | 0 |  |  |  |
| FulfillmentCountry | varchar | 50 | 1 |  |  |  |
