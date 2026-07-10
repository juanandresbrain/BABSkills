# dbo.DynamicsDiscountFacts

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DynamicsDiscountFactsId | int | 4 | 0 | YES |  |  |
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
| BabRetailDiscountTransUniqueLineNum | int | 4 | 1 |  |  |  |
| ManualDiscountType | varchar | 20 | 1 |  |  |  |
| PeriodicDiscountOfferId | varchar | 20 | 1 |  |  |  |
| IsCurrent | int | 4 | 1 |  |  |  |
| IsNegatedCurrent | int | 4 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| CurrentSentDate | datetime | 8 | 1 |  |  |  |
| NegativeSentDate | datetime | 8 | 1 |  |  |  |
| BatchID | nvarchar | 200 | 1 |  |  |  |
