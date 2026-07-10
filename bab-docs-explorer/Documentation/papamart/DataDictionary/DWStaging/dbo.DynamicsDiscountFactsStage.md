# dbo.DynamicsDiscountFactsStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Amount | numeric | 9 | 1 |  |  |  |
| DiscountCost | numeric | 9 | 1 |  |  |  |
| DiscountOriginType | varchar | 10 | 1 |  |  |  |
| RetailTerminalId | varchar | 10 | 1 |  |  |  |
| RetailTransactionId | varchar | 44 | 1 |  |  |  |
| BABIntRetailOperatingUnitNumber | varchar | 8 | 1 |  |  |  |
| LineNum | bigint | 8 | 1 |  |  |  |
| Percentage | numeric | 9 | 1 |  |  |  |
| RetailStoreId | varchar | 8 | 1 |  |  |  |
| SaleLineNum | bigint | 8 | 1 |  |  |  |
| CustomerDiscountType | varchar | 10 | 1 |  |  |  |
| BABIntRetailProcessed | varchar | 10 | 1 |  |  |  |
| Entity | varchar | 10 | 1 |  |  |  |
| RetailReceiptId | varchar | 18 | 1 |  |  |  |
| DiscountTransUniqueLineNum | int | 4 | 1 |  |  |  |
| ManualDiscountType | varchar | 20 | 1 |  |  |  |
| PeriodicDiscountOfferId | varchar | 20 | 1 |  |  |  |
