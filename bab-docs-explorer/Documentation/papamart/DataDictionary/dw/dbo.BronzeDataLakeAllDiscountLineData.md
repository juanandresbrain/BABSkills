# dbo.BronzeDataLakeAllDiscountLineData

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionDate | date | 3 | 1 |  |  |  |
| InventLocationId | nvarchar | 20 | 1 |  |  |  |
| Amount | numeric | 9 | 1 |  |  |  |
| DiscountCost | numeric | 9 | 1 |  |  |  |
| DiscountOriginType | nvarchar | 16 | 1 |  |  |  |
| RetailTerminalId | nvarchar | 20 | 1 |  |  |  |
| RetailTransactionId | nvarchar | 88 | 1 |  |  |  |
| LineNum | int | 4 | 1 |  |  |  |
| RetailStoreId | nvarchar | 20 | 1 |  |  |  |
| SaleLineNum | int | 4 | 1 |  |  |  |
| PeriodicDiscountOfferId | nvarchar | 40 | 1 |  |  |  |
| Entity | nvarchar | 8 | 1 |  |  |  |
