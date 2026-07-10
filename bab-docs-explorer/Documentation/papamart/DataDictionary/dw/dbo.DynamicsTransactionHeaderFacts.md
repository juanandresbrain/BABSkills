# dbo.DynamicsTransactionHeaderFacts

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DynamicsTransactionHeaderFactsId | int | 4 | 0 | YES |  |  |
| RetailTerminalId | varchar | 10 | 1 |  |  |  |
| CustAccount | varchar | 20 | 1 |  |  |  |
| InventLocationId | varchar | 4 | 1 |  |  |  |
| RetailReceiptId | varchar | 18 | 1 |  |  |  |
| RetailStaffId | varchar | 20 | 1 |  |  |  |
| RetailTransactionId | varchar | 44 | 1 |  |  |  |
| BABIntRetailOperatingUnitNumber | varchar | 8 | 1 |  |  |  |
| TransDate | date | 3 | 1 |  |  |  |
| RetailTransactionType | varchar | 10 | 1 |  |  |  |
| BABIntRetailProcessed | varchar | 10 | 1 |  |  |  |
| Entity | varchar | 4 | 1 |  |  |  |
| DiscAmount | numeric | 9 | 1 |  |  |  |
| TotalDiscAmount | numeric | 9 | 1 |  |  |  |
| IsCurrent | int | 4 | 1 |  |  |  |
| IsNegatedCurrent | int | 4 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| CurrentSentDate | datetime | 8 | 1 |  |  |  |
| NegativeSentDate | datetime | 8 | 1 |  |  |  |
| BatchID | nvarchar | 200 | 1 |  |  |  |
| IsInDynamics | int | 4 | 1 |  |  |  |
| IsInDynamicsStaging | int | 4 | 1 |  |  |  |
| TransactionNumber | int | 4 | 1 |  |  |  |
