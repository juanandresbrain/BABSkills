# dbo.DynamicsDiscountLineStage

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionKey | varchar | 145 | 1 |  |  |  |
| Amount | numeric | 9 | 1 |  |  |  |
| DiscountCost | numeric | 9 | 1 |  |  |  |
| DiscountOriginType | varchar | 8 | 0 |  |  |  |
| RetailTerminalId | varchar | 53 | 1 |  |  |  |
| RetailTransactionId | varchar | 147 | 1 |  |  |  |
| BABIntRetailOperatingUnitNumber | varchar | 14 | 0 |  |  |  |
| LineNum | bigint | 8 | 1 |  |  |  |
| Percentage | int | 4 | 1 |  |  |  |
| RetailStoreId | varchar | 50 | 1 |  |  |  |
| SaleLineNum | varchar | 50 | 1 |  |  |  |
| CustomerDiscountType | varchar | 4 | 0 |  |  |  |
| BABIntRetailProcessed | int | 4 | 1 |  |  |  |
| ManualDiscountType | varchar | 19 | 0 |  |  |  |
| PeriodicDiscountOfferId | varchar | 11 | 1 |  |  |  |
| BabRetailDiscountTransUniqueLineNum | bigint | 8 | 1 |  |  |  |
| Entity | varchar | 4 | 1 |  |  |  |
| CreateTime | datetime | 8 | 1 |  |  |  |
| Barcode | varchar | 50 | 1 |  |  |  |
| InventLocationId | varchar | 50 | 1 |  |  |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: dbo.spBabDynamics1_BuildDiscountStagingTable](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics1_BuildDiscountStagingTable.md)
- [WebOrderProcessing: dbo.spBabDynamics1_BuildDiscountStagingTable_BAK20240617](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics1_BuildDiscountStagingTable_BAK20240617.md)
- [WebOrderProcessing: dbo.spBabDynamics3_BuildSalesLineStagingTable](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics3_BuildSalesLineStagingTable.md)
- [WebOrderProcessing: dbo.spBabDynamics7_ShippingLineInserts](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics7_ShippingLineInserts.md)

