# dbo.dynamicstransactionheaderfacts

**Database:** LH_Mart_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DynamicsTransactionHeaderFactsId | int | 4 | 1 |  |  |  |
| RetailTerminalId | varchar | 8000 | 1 |  |  |  |
| CustAccount | varchar | 8000 | 1 |  |  |  |
| InventLocationId | varchar | 8000 | 1 |  |  |  |
| RetailReceiptId | varchar | 8000 | 1 |  |  |  |
| RetailStaffId | varchar | 8000 | 1 |  |  |  |
| RetailTransactionId | varchar | 8000 | 1 |  |  |  |
| BABIntRetailOperatingUnitNumber | varchar | 8000 | 1 |  |  |  |
| TransDate | date | 3 | 1 |  |  |  |
| RetailTransactionType | varchar | 8000 | 1 |  |  |  |
| BABIntRetailProcessed | varchar | 8000 | 1 |  |  |  |
| Entity | varchar | 8000 | 1 |  |  |  |
| DiscAmount | decimal | 9 | 1 |  |  |  |
| TotalDiscAmount | decimal | 9 | 1 |  |  |  |
| IsCurrent | int | 4 | 1 |  |  |  |
| IsNegatedCurrent | int | 4 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| CurrentSentDate | datetime2 | 8 | 1 |  |  |  |
| NegativeSentDate | datetime2 | 8 | 1 |  |  |  |
| BatchID | varchar | 8000 | 1 |  |  |  |
| IsInDynamics | int | 4 | 1 |  |  |  |
| IsInDynamicsStaging | int | 4 | 1 |  |  |  |
| TransactionNumber | int | 4 | 1 |  |  |  |
