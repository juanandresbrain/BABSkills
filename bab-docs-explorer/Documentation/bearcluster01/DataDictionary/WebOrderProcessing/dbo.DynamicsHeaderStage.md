# dbo.DynamicsHeaderStage

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionKey | varchar | 136 | 1 |  |  |  |
| RetailTerminalId | varchar | 53 | 1 |  |  |  |
| CustAccount | int | 4 | 1 |  |  |  |
| InventLocationId | varchar | 50 | 1 |  |  |  |
| RetailReceiptId | varchar | 50 | 1 |  |  |  |
| RetailStaffId | varchar | 50 | 1 |  |  |  |
| RetailTransactionId | varchar | 138 | 1 |  |  |  |
| BABIntRetailOperatingUnitNumber | varchar | 14 | 0 |  |  |  |
| TransDate | date | 3 | 1 |  |  |  |
| RetailTransactionType | varchar | 5 | 0 |  |  |  |
| BABIntRetailProcessed | int | 4 | 1 |  |  |  |
| Entity | varchar | 4 | 1 |  |  |  |
| DiscAmount | numeric | 17 | 0 |  |  |  |
| TotalDiscAmount | numeric | 17 | 0 |  |  |  |
| CreateTime | datetime | 8 | 1 |  |  |  |
| Barcode | varchar | 50 | 1 |  |  |  |
| CustomerNumber | varchar | 100 | 1 |  |  |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: dbo.spBabDynamics2_BuildHeaderStagingTable](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics2_BuildHeaderStagingTable.md)
- [WebOrderProcessing: dbo.spBabDynamics5_BuildTenderStagingTable](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics5_BuildTenderStagingTable.md)

